from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

load_dotenv()

insert_functionality = "data manipulation"
insert_programming_language = "Java"
'''
    This is not only limited to algorithms but you can use some code as well.
    In short, this prompt will help you optimize the algorithm/code.
'''
library_recommendations_assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their programming needs of code goals.",
    instructions=[f"I’m starting a new project. Can you recommend a suitable {insert_programming_language} library or framework for {insert_functionality}"]
)
# -*- Print a response to the cli
library_recommendations_assistant.print_response(f"please help the best you can me with this functionality :{insert_functionality}, "
                                                         f"provide me the best sample you can using this language {insert_programming_language}.", markdown=True)
