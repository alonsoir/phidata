from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
import requests

load_dotenv()

insert_code_here = None
url = "https://raw.githubusercontent.com/alonsoir/psychic-octo-umbrella/main/chat.py"  # Reemplaza con la URL del repositorio
with requests.get(url) as response:
    if response.status_code == 200:
        insert_code_here = response.text
        print(f"This is the code to review: {insert_code_here}")
        print("\n")
    else:
        print("Error al acceder a la URL:", response.status_code)
'''
    ChatGPT can provide some really good feedback about your code.
    You may or may not implement all those feedbacks but it can certainly be a good starting point.
'''
code_review_assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their peer review needs of code goals. Be honest and constructive in your feedback.",
    instructions=[f"I’ve written a new feature. Can you review my code and provide feedback on potential improvements? Here is the code : {insert_code_here}"]
)
# -*- Print a response to the cli
code_review_assistant.print_response(f"please help the best you can me with this code:{insert_code_here}, "
                                                         f"provide me the best and honest peer review you can provide.", markdown=True)
