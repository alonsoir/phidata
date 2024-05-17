from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

load_dotenv()

insert_technology_or_concept = "data manipulation with python"

'''
    This is not only limited to algorithms but you can use some code as well.
    In short, this prompt will help you optimize the algorithm/code.
'''
library_recommendations_assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their programming needs of code goals.",
    instructions=[f"I need a summary of the [insert technology or concept] technical documentation. Can you provide a concise overview?"]
)
# -*- Print a response to the cli
library_recommendations_assistant.print_response(f"please help the best you can me with this functionality:{insert_technology_or_concept}, "
                                                         f"provide me the best sample you can using this technology or concept: {insert_technology_or_concept}.", markdown=True)
