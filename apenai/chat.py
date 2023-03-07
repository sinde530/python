import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

# 대화 기록 초기화
conversation_id = None

while True:
    # user input
    user_input = input("사용자: 안녕")

    # OpenAI API에 입력 전달하여 대화 실행
    response = openai.Completion.create(
        engine="davinci",
        prompt=(f"Conversation ID: {conversation_id}\nUser: {user_input}\nAI:"),
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # 대화 결과 출력
    message = response.choices[0].text.strip()
    print(f"AI: {message}")

    # 다음 대화를 위해 Conversation ID 업데이트
    conversation_id = response.conversation_id
