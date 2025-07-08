import json
import os
import sys

try:
    from tkinter import messagebox
except ImportError:
    import tkMessageBox as messagebox

class SaveFile:
    def __init__(self):
        if getattr(sys, 'frozen', False):
            # PyInstaller로 패키징된 실행파일(.exe) 위치
            app_path = os.path.dirname(sys.executable)
        else:
            # 개발 중인 .py 파일 위치
            app_path = os.path.dirname(os.path.abspath(__file__))

        self.file_path = os.path.join(app_path, "animalUser.txt")
        
    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS  # PyInstaller 실행 시
        except Exception:
            base_path = os.path.abspath(".")  # 개발 중
        return os.path.join(base_path, relative_path)

    def save_all_accounts(self, accounts_list):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(accounts_list, f, ensure_ascii=False, indent=2)

    def 목록불러오기(self):
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            return []

        with open(self.file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                if not isinstance(data, list):
                    print("기존 단일 계정 형식을 여러 계정 리스트로 변환합니다.")
                    return [data]
                return data
            except json.JSONDecodeError:
                messagebox.showerror("형식 에러", f"{self.file_path} 파일의 JSON 형식이 올바르지 않습니다. 빈 리스트를 반환합니다.")
                return []

    # 계정 저장 (신규 또는 업데이트)
    def tray(self, aniname, password, level, exp, big, image_size=None):
        all_accounts = self.목록불러오기()
        found = False
        for i, account in enumerate(all_accounts):
            if account.get("name") == aniname:
                all_accounts[i]["pw"] = password
                all_accounts[i]["level"] = level
                all_accounts[i]["경험치"] = exp
                all_accounts[i]["동물덩치"] = big
                if image_size is not None:
                    all_accounts[i]["image_size"] = image_size
                found = True
                break

        if not found:
            new_user = {
                "name": aniname,
                "pw": password,
                "level": level,
                "경험치": exp,
                "동물덩치": big
            }
            if image_size is not None:
                new_user["image_size"] = image_size
            all_accounts.append(new_user)

        self.save_all_accounts(all_accounts)

    # 계정 불러오기 (image_size 기본값 처리)
    def 특정불러오기(self, aniname):
        all_accounts = self.목록불러오기()
        for account in all_accounts:
            if account.get("name") == aniname:
                if "image_size" not in account:
                    account["image_size"] = 50  # 기본 이미지 크기
                return account
        return None

    # 로그인 후 업데이트 (image_size 포함)
    def 업데이트(self, aniname, new_level, new_exp, new_big, new_image_size=None):
        all_accounts = self.목록불러오기()
        updated = False
        for i, account in enumerate(all_accounts):
            if account.get("name") == aniname:
                all_accounts[i]["level"] = new_level
                all_accounts[i]["경험치"] = new_exp
                all_accounts[i]["동물덩치"] = new_big
                if new_image_size is not None:
                    all_accounts[i]["image_size"] = new_image_size
                updated = True
                break

        if updated:
            self.save_all_accounts(all_accounts)
            return True
        return False

    # 삭제 함수 (생략 가능)
    def 삭제하기(self, aniname, level, exp):
        all_accounts = self.목록불러오기()
        new_accounts = [
            account for account in all_accounts
            if not (account.get("name") == aniname and
                    account.get("level") == level and
                    account.get("경험치") == exp)
        ]
        if len(new_accounts) < len(all_accounts):
            self.save_all_accounts(new_accounts)
            print(f"[삭제됨] '{aniname}' 계정이 삭제되었습니다.")
            return True
        else:
            print(f"[실패] '{aniname}' 계정을 찾지 못했습니다.")
            return False
