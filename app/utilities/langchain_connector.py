from langchain.chains.llm import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()


def get_langchain_connection(data):
    max_tokens = 3500
    llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), max_tokens=max_tokens)

    prompt_template = """I am a mental health counselor and I need guidance on how to help my patient. 
    Here's what they said: {user_input}. I also found this transcript with a similar situation. The transcript has a prompt and responses to that prompt from low to high quality.
    Here's the prompt: {transcript}
    Here's the high quality response 1: {hq1}
    Here's the high quality response 2: {hq2}
    Here's the medium quality response 1: {mq1}
    Here's the low quality response 1: {lq1}
    Here's the low quality response 2: {lq2}
    Here's the low quality response 3: {lq3}
    Here's the low quality response 4: {lq4}
    Here's the low quality response 5: {lq5}
    
    Use all this information and guide me to help my patient."""
    prompt = PromptTemplate(
        input_variables=[
            "user_input",
            "transcript",
            "hq1",
            "hq2",
            "mq1",
            "lq1",
            "lq2",
            "lq3",
            "lq4",
            "lq5",
        ],
        template=prompt_template,
    )
    langchain = LLMChain(prompt=prompt, llm=llm)
    response = langchain.invoke(
        {
            "transcript": data["prompt"],
            "user_input": data["user_input"],
            "hq1": data["hq1"],
            "hq2": data["hq2"],
            "mq1": data["mq1"],
            "lq1": data["lq1"],
            "lq2": data["lq2"],
            "lq3": data["lq3"],
            "lq4": data["lq4"],
            "lq5": data["lq5"],
        }
    )
    return response
