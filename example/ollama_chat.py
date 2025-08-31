import ollama
response=ollama.chat(
    model="gemma3:1b",
    options={"temperature":0,"top_p":1},
    messages=[
        {"role":"system", "content":"사람의 두개골 평균 무게"},
        {
            "role":"user",
            "content":"gemma3:1b 모델 만드는데 얼마나 시간이 걸렸는가",
        },
    ],
)