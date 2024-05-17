from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

load_dotenv()

requirements = "apache kakfa latest version in java"
functionality = "exactly once delivery in java."

"""
    This prompt requires a good level of detail but it can help you recommend
    some of the best design patterns you should use for your problem set.
"""
design_patterns_recommendations_assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their refactor needs of code goals.",
    instructions=[
        f"I’m designing a new software component. These are the requirements: {requirements}. "
        f"\nWhat design pattern would you recommend for implementing {functionality}"
    ],
)
# -*- Print a response to the cli
design_patterns_recommendations_assistant.print_response(
    f"these are my requirements:{requirements} \n and this is the functionality: {functionality} i expect",
    markdown=True,
)
