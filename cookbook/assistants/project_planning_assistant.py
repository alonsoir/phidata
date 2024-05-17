from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

load_dotenv()

insert_project_requirements_or_constraints = None # Add any relevant project requirements or constraints here

'''
    ChatGPT can analyze project requirements, dependencies, and deadlines
    to generate a prioritized task list, helping you effectively manage project timelines and deliverables.
'''
project_planning_assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their programming needs of code goals.",
    instructions=[f"I’m planning my project roadmap. Can you suggest a prioritized list of tasks based on []?"]
)
# -*- Print a response to the cli
project_planning_assistant.print_response(f"please help the best you can me with this functionality:{insert_project_requirements_or_constraints}",
                                          markdown=True)
