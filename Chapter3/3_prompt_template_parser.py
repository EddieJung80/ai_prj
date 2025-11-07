from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(model="gpt-5-mini", openai_api_key=api_key)
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 친절한 AI도우미입니다. 사용자의 질문에 최대 3줄로 답하세요"),
        ("human", "{question}"),
    ]
)

string_output_parser = StrOutputParser()

result: AIMessage = chat_model.invoke(
    chat_prompt_template.format_messages(question="파이썬에서 리스트를 정렬하는 방법은?"),
)

print(type(result))
print("---- Example with direct model invocation ----")

parsed_result = string_output_parser.parse(result)
print(type(parsed_result.content))

print("---- Example with previous response id tracking ----")

chain = chat_prompt_template | chat_model | string_output_parser
print(type(chain))

result = chain.invoke({"question": "파이썬에서 딕셔너리를 정렬하는 방법은?"})

print(type(result))
print(result)

