import asyncio
import os
import random

from data import config
from pyrogram import Client
from utils.core import logger, load_from_json, save_list_to_file, save_to_json, get_all_lines


class Accounts:
    def __init__(self):
        self.workdir = config.WORKDIR
        self.api_id = config.API_ID
        self.api_hash = config.API_HASH

    @staticmethod
    def parse_proxy(proxy):
        return {
            "scheme": config.PROXY['TYPE']['TG'],
            "hostname": proxy.split(":")[1].split("@")[1],
            "port": int(proxy.split(":")[2]),
            "username": proxy.split(":")[0],
            "password": proxy.split(":")[1].split("@")[0]
        }

    @staticmethod
    def get_available_accounts(sessions: list):
        available_accounts = []

        if config.PROXY['USE_PROXY_FROM_FILE']:
            proxys = get_all_lines(config.PROXY['PROXY_PATH'])
            for session in sessions:
                available_accounts.append({
                    'session_name': session,
                    'phone_number': '+0',
                    'proxy': proxys.pop(proxys.index(random.choice(proxys))) if proxys else None
                })

        else:
            accounts_from_json = load_from_json('sessions/accounts.json')

            if not accounts_from_json:
                raise ValueError("Chưa có tài khoản trong Sessions/accounts.json")

            for session in sessions:
                for saved_account in accounts_from_json:
                    if saved_account['session_name'] == session:
                        available_accounts.append(saved_account)
                        break

        return available_accounts

    def pars_sessions(self):
        sessions = [file.replace(".session", "") for file in os.listdir(self.workdir) if file.endswith(".session")]

        logger.info(f"Phiên tìm kiếm: {len(sessions)}.")
        return sessions

    async def check_valid_account(self, account: dict):
        session_name, phone_number, proxy = account.values()

        try:
            proxy_dict = {
                "scheme": config.PROXY['TYPE']['TG'],
                "hostname": proxy.split(":")[1].split("@")[1],
                "port": int(proxy.split(":")[2]),
                "username": proxy.split(":")[0],
                "password": proxy.split(":")[1].split("@")[0]
            } if proxy else None

            client = Client(name=session_name, api_id=self.api_id, api_hash=self.api_hash, workdir=self.workdir,
                            proxy=proxy_dict)

            connect = await asyncio.wait_for(client.connect(), timeout=config.TIMEOUT)
            if connect:
                await client.get_me()
                await client.disconnect()
                return account
            else:
                await client.disconnect()
        except:
            pass

    async def check_valid_accounts(self, accounts: list):
        logger.info(f"Kiểm tra tài khoản hợp lệ...")

        tasks = []
        for account in accounts:
            tasks.append(asyncio.create_task(self.check_valid_account(account)))

        v_accounts = await asyncio.gather(*tasks)

        valid_accounts = [account for account, is_valid in zip(accounts, v_accounts) if is_valid]
        invalid_accounts = [account for account, is_valid in zip(accounts, v_accounts) if not is_valid]
        logger.success(f"Tài khoản hợp lệ: {len(valid_accounts)}; Không hợp lệ: {len(invalid_accounts)}")

        return valid_accounts, invalid_accounts

    async def get_accounts(self):
        sessions = self.pars_sessions()
        available_accounts = self.get_available_accounts(sessions)

        if not available_accounts:
            raise ValueError("Không có sẵn tài khoản!")
        else:
            logger.success(f"Tìm kiếm tài khoản có sẵn: {len(available_accounts)}.")

        valid_accounts, invalid_accounts = await self.check_valid_accounts(available_accounts)

        if invalid_accounts:
            save_list_to_file(f"{ config.WORKDIR}invalid_accounts.txt", invalid_accounts)
            logger.info(f"Đã lưu {len(invalid_accounts)} (các) tài khoản không hợp lệ trong { config.WORKDIR}invalid_accounts.txt")

        if not valid_accounts:
            raise ValueError("Không có phiên hợp lệ")
        else:
            return valid_accounts

    async def create_sessions(self):
        while True:
            session_name = input('\nNhập tên phiên làm việc (nhấn Enter để thoát): ')
            if not session_name: return

            if config.PROXY['USE_PROXY_FROM_FILE']:
                proxys = get_all_lines(config.PROXY['PROXY_PATH'])
                proxy = random.choice(proxys) if proxys else None
            else:
                proxy = input("Nhập proxy theo dạng login:password@ip:port (nhấn Enter để sử dụng không cần proxy): ")

            dict_proxy = self.parse_proxy(proxy) if proxy else None

            phone_number = (input("Nhập số điện thoại của tài khoản: ")).replace(' ', '')
            phone_number = '+' + phone_number if not phone_number.startswith('+') else phone_number

            client = Client(
                api_id=self.api_id,
                api_hash=self.api_hash,
                name=session_name,
                workdir=self.workdir,
                phone_number=phone_number,
                proxy=dict_proxy,
                lang_code='vn'
            )

            async with client:
                me = await client.get_me()

            save_to_json(f'{ config.WORKDIR}accounts.json', dict_={
                "session_name": session_name,
                "phone_number": phone_number,
                "proxy": proxy
            })
            logger.success(f'Đã thêm tài khoản {me.username} ({me.first_name}) | {me.phone_number}')