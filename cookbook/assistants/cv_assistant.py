from dotenv import load_dotenv

from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

load_dotenv()

position_name = Job_Name = "Software Engineer"
company_Name = "Apple Inc."
Required_Skills_and_Experience = ["Python", "Machine Learning", "Computer Vision", "Natural"]
job_description = None
"""
    ChatGPT can analyze project requirements, dependencies, and deadlines
    to generate a prioritized task list, helping you effectively manage project timelines and deliverables.
"""
instructions = (f"Suggest candidates for the position of {position_name}\n "
                f"Recommends qualified candidates for the {Job_Name} vacancy at {company_Name}.\n"
                f"Identify the best candidates for a position that requires {Required_Skills_and_Experience}.\n"
                f"More specific prompts: Based on the job description: {job_description}\n for {Job_Name}, which candidates in your vector database\n "
                f"do you think would be the best fit?. Create a list with full candidate's name, email and linkedin profile. Maximum ten of them.\n"
                f"Considering each one of those candidate's Names, with their skills and experience, what other similar positions might be "
                "of interest to him or her?. Their gender or their race, or their age is irrelevant.\n"
                f"Compare the profiles of every candidate from the generated candidates list for the position of {Job_Name} and highlight "
                "their strengths and weaknesses. Update the existent list with that info.\n"
                f"In addition to the skills and experience mentioned in the job description {job_description} if provided,\n"
                f"what other characteristics or qualities do you think would be important to a successful candidate in this role?\n"
                f"Given the culture and work environment at {company_Name}, what type of candidates from the created list do you think would be the best fit?\n"
                f"If you had to select only one candidate for the position of {position_name}, who would it be and why?\n"

                f"Use natural language and avoid technicalities, your recommendation should be easy to understand. Provide additional context if necessary. \n"
                f"If there is any relevant information about the company {company_Name}, the team or the selection process, \n"
                f"search it using the web search engine, linkedin and use it so that they can better understand your needs. Evaluate the answers critically.\n"
                f"If you have more than once candidate, create a ranking based on strengths and weaknesses. Finally, show your sources, how do you created that ranking?")
cvassistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You help people with their programming needs of code goals.",
    instructions=[
        f"follow the best you can the {instructions}"
        f"\nRecommends qualified candidates for the [Job_Name] vacancy at [Company Name]"
        "Identify the best candidates for a position that requires [Required Skills and Experience]"
    ],
)
# -*- Print a response to the cli
cvassistant.print_response(
    f"please help the best you can me with these instructions:{instructions}",
    markdown=True,
)
