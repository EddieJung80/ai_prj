
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-5-mini", model_provider="openai")
result = model.invoke("랭체인이 뭔가요?")
print(type(result))
print("------------------------------------------")
print(result.content)  # 출력: 랭체인은 언어 모델을 활용한 애플리케이션 개발을 쉽게 해주는 프레임워크입니다.

