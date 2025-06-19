import json
import os

class SaveFile:

    def __init__(self):
        # 파일 경로를 인스턴스 변수로 저장해두면 편리합니다.
        self.file_path = "animalUser.txt"

    # 계정 목록을 파일에 저장
    def save_all_accounts(self, accounts_list):
        """
        주어진 계정 목록(리스트)을 파일에 저장합니다.
        기존 파일 내용은 이 목록으로 완전히 덮어씌워집니다.
        """
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(accounts_list, f, ensure_ascii=False, indent=2)

    # 계정 목록을 파일에서 불러오기
    def 목록불러오기(self):
        if not os.path.exists(self.file_path) or os.path.getsize(self.file_path) == 0:
            return []  # 파일이 없거나 비어있으면 빈 리스트 반환
        
        with open(self.file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                # 불러온 데이터가 리스트가 아닐 경우 (예전 단일 계정 형식)를 대비하여 처리
                if not isinstance(data, list):
                    # 이전 단일 계정 형식이라면 리스트로 변환하여 반환
                    print("기존 단일 계정 형식을 여러 계정 리스트로 변환합니다.")
                    return [data]
                return data
            except json.JSONDecodeError:
                # JSON 형식이 아닐 경우 오류 처리
                print(f"Error: {self.file_path} 파일의 JSON 형식이 올바르지 않습니다. 빈 리스트를 반환합니다.")
                return []


    # 특정 계정 정보 업데이트 또는 새 계정 추가
    def tray(self, aniname, password, level, exp):
    
        all_accounts = self.목록불러오기() # 현재 모든 계정 불러오기
        
        # 기존 계정 찾기
        found = False
        for i, account in enumerate(all_accounts):
            if account.get("name") == aniname:
                # 계정이 이미 존재하면 정보 업데이트
                all_accounts[i]["pw"] = password
                all_accounts[i]["level"] = level
                all_accounts[i]["경험치"] = exp
                found = True
                break
        
        if not found:
            # 새 계정 추가
            new_user = {
                "name" : aniname,
                "pw" : password,
                "level" : level,
                "경험치" : exp
            }
            all_accounts.append(new_user)
        
        self.save_all_accounts(all_accounts) # 변경된 목록 저장


    # 특정 계정 정보 불러오기(로그인)
    def 특정불러오기(self, aniname):
        """
        특정 이름의 계정 정보를 찾아 반환합니다.
        계정이 없으면 None을 반환합니다.
        """
        all_accounts = self.목록불러오기()
        for account in all_accounts:
            if account.get("name") == aniname:
                return account
        return None

    # '로그인 성공 후' 계정 데이터 업데이트
    def 업데이트(self, aniname, new_level, new_exp):
        """
        로그인한 특정 계정의 레벨과 경험치만 업데이트합니다.
        """
        all_accounts = self.목록불러오기()
        updated = False
        for i, account in enumerate(all_accounts):
            if account.get("name") == aniname:
                all_accounts[i]["level"] = new_level
                all_accounts[i]["경험치"] = new_exp
                updated = True
                break
        
        if updated:
            self.save_all_accounts(all_accounts) # 변경된 목록 저장
            return True
        return False
    
    def 삭제하기(self, aniname, level, exp):
        all_accounts = self.목록불러오기()
        
        # 삭제 기준에 맞는 계정을 제거
        new_accounts = [
            account for account in all_accounts
            if not (account.get("name") == aniname and
                    account.get("level") == level and
                    account.get("경험치") == exp)
        ]
        
        # 삭제 전과 후 리스트 길이 비교로 삭제 성공 여부 확인
        if len(new_accounts) < len(all_accounts):
            self.save_all_accounts(new_accounts)
            print(f"[삭제됨] '{aniname}' 계정이 삭제되었습니다.")
            return True
        else:
            print(f"[실패] '{aniname}' 계정을 찾지 못했습니다.")
            return False
