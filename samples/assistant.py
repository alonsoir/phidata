from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()
assistant = Assistant(tools=[DuckDuckGo()], show_tool_calls=True)
assistant.print_response("Whats happening in France?", markdown=True)
