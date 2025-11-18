# logging.py from langchain-teddynote 

# 먼저, .env 파일에 LangSmith 에서 발급받은 키와 프로젝트 정보를 입력합니다.

# LANGCHAIN_TRACING_V2: "true" 로 설정하면 추적을 시작합니다.
# LANGCHAIN_ENDPOINT: https://api.smith.langchain.com 변경하지 않습니다.
# LANGCHAIN_API_KEY: 이전 단계에서 발급받은 키 를 입력합니다.
# LANGCHAIN_PROJECT: 프로젝트 명 을 기입하면 해당 프로젝트 그룹으로 모든 실행(Run) 이 추적됩니다.

# import os

# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
# os.environ["LANGCHAIN_PROJECT"] = "LangChain 프로젝트명"
# os.environ["LANGCHAIN_API_KEY"] = "LangChain API KEY 입력"

# LangSmith 추적 시작 함수 정의
# logging.langsmith("원하는 프로젝트명")

# 추척을 원하지 않을 때
# # set_enable=False 로 지정하면 추적을 하지 않습니다.
# logging.langsmith("랭체인 튜토리얼 프로젝트", set_enable=False)

import os

def langsmith(project_name=None, set_enable=True):

    if set_enable:
        langchain_key = os.environ.get("LANGCHAIN_API_KEY", "")
        langsmith_key = os.environ.get("LANGSMITH_API_KEY", "")

        # 더 긴 API 키 선택
        if len(langchain_key.strip()) >= len(langsmith_key.strip()):
            result = langchain_key
        else:
            result = langsmith_key

        if result.strip() == "":
            print(
                "LangChain/LangSmith API Key가 설정되지 않았습니다. 참고: https://wikidocs.net/250954"
            )
            return

        os.environ["LANGSMITH_ENDPOINT"] = (
            "https://api.smith.langchain.com"  # LangSmith API 엔드포인트
        )
        os.environ["LANGSMITH_TRACING"] = "true"  # true: 활성화
        os.environ["LANGSMITH_PROJECT"] = project_name  # 프로젝트명
        print(f"LangSmith 추적을 시작합니다.\n[프로젝트명]\n{project_name}")
    else:
        os.environ["LANGSMITH_TRACING"] = "false"  # false: 비활성화
        print("LangSmith 추적을 하지 않습니다.")


def env_variable(key, value):
    os.environ[key] = value
