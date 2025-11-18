import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


from agents import Agent, Runner, function_tool
from ddgs import DDGS

# ① 뉴스 검색 도구 정의
@function_tool
def news_search(query: str) -> str:
    """DuckDuckGo를 사용하여 최신 뉴스 검색"""
    try:
        # DuckDuckGo 검색 수행
        results = DDGS().text(query, max_results=5)

        # 결과 포맷팅
        if results:
            return f" '{query}' 검색결과 : \n {results}"
        else:
            return f"'{query}'에 대한 뉴스를 찾을 수 없습니다."

    except Exception as e:
        return f"뉴스 검색 중 오류 발생: {str(e)}"

# ② 뉴스 검색 에이전트 정의
news_agent = Agent(
    name="NewsSearchAgent",
    model="gpt-5-mini",
    instructions=(
        "당신은 한국어 뉴스 리포터입니다."
        "덕덕고를 사용하여 최신 뉴스를 검색하고 요약합니다."
        "3개의 기사 URL을 함께 알려주세요"
    ),
    tools=[news_search]
)


if __name__ == "__main__":
    # ③ 에이전트 실행 예시
    query = "KLPGA 골프 대회 관련 뉴스"
    result = Runner.run_sync(news_agent, query)
    print(result.final_output)