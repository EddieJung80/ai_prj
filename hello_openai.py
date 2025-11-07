# 챗봇 예시, previous id 기억

from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


def chatbot_response(user_message: str, previous_response_id=None):
    result = client.responses.create(
        model="gpt-5-mini",
        instructions="",
        input=user_message,
        # 이전 대화의 id값을 추가
        previous_response_id=previous_response_id,
    )
    return result

if __name__ == "__main__":
    # ② 사용자 메시지를 입력받고 응답을 출력합니다.
    previous_response_id = None
    while True:
        # ③ 사용자에게 메시지 입력 받기
        user_message = input("메시지: ")
        # ④ 'exit' 입력 시 대화 종료
        if user_message.lower() == "exit":
            print("대화를 종료 합니다.")
            break

        # ⑤ 챗봇 응답 받아오기
        result = chatbot_response(user_message, previous_response_id)
        # print(result)
        # print("Result id :" + result.id)
        previous_response_id = result.id

        print("챗봇 :" + result.output_text + " /// Result id :" + result.id)