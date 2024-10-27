import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


def run_groq_api(prompt, model='llama3-8b-8192'):

    client = Groq(
        api_key=os.environ.get("GROQ_API"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )

    response = chat_completion.choices[0].message.content
    return response