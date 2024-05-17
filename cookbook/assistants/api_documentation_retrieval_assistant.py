from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

load_dotenv()

api_name = "apache spark"
api_doc_retrieval_assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people providing the most relevant documentation or usage examples for their needs of code goals."
                "\n You will be looking for first in the official docs and the most popular online resources to find the best "
                "information to help the user. "
                "Use the most starred projects from github and gitlab, besides, look for samples in medium.com,"
                "stackoverflow.com and daily.dev. ",
    instructions=[f"I’m working with the {api_name} API. Can you provide me with relevant documentation or usage examples?"],
)
# -*- Print a response to the cli
api_doc_retrieval_assistant.print_response(f"i am working with :\n{api_name}", markdown=True)
