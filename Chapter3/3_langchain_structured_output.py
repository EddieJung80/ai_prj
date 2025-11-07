import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model

llm = init_chat_model(model="gpt-5-mini")

class MovieReview(BaseModel):
    """Schema for a movie review structured output"""
    title: str = Field(description="The title of the movie")
    rating: float = Field(description="Rating of the movie from 1 to 10")
    review: str = Field(description="A brief review of the movie, 3~4 sentences long")

structured_llm = llm.with_structured_output(MovieReview)

result: MovieReview = structured_llm.invoke(
    "영화 '라스트 갓파더'에 대한 리뷰를 작성해 주세요."
)

print(type(result))

print("제목:", result.title)
print("평점:", result.rating)
print("리뷰:", result.review)
