from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

load_dotenv()

algorithm_name = "Fast Fourier Transform (FFT) in java"

'''
    This is not only limited to algorithms but you can use some code as well.
    In short, this prompt will help you optimize the algorithm/code.
'''
design_patterns_recommendations_assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their refactor needs of code goals.",
    instructions=[f"I’m implementing the algorithm named {algorithm_name}. Are there any optimization techniques or best practices I should consider?"]
)
# -*- Print a response to the cli
design_patterns_recommendations_assistant.print_response(f"please help the best you can me with :{algorithm_name}, provide me the best sample you can.", markdown=True)
