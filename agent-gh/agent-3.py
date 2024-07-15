from crewai import Agent, Task, Crew
from crewai_tools import GithubSearchTool, CodeInterpreterTool, CodeDocsSearchTool, DirectoryReadTool, FileReadTool, RagTool
from os import getenv
from dotenv import load_dotenv
load_dotenv()

GH_REPO = "hiteshbandhu/notes-ai-and-tech"

code_interpreter_tool = CodeInterpreterTool()
code_docs_search_tool = CodeDocsSearchTool()
directory_read_tool = DirectoryReadTool()
file_read_tool = FileReadTool()
rag_tool = RagTool()
github_search_tool = GithubSearchTool(gh_token = getenv("GH_TOKEN"),content_types = ['code', 'issue'])

# Define agents
plan_agent = Agent(
    role='Researcher',
    goal='Produce Natural Language result. Make a plan to solve the github issue, use ragtool if githubtool is not working for making queries',
    backstory="""As a researcher at a tech startup, you specialize in understanding complex software issues and devising strategic plans to resolve them efficiently. Your role involves deep dives into GitHub repositories, analyzing code structures, and pinpointing precise areas for improvement. You collaborate closely with developers, providing them with comprehensive plans that outline the necessary changes and refer them to relevant files and issue details. Your insights and plans are crucial in streamlining the development process and ensuring robust solutions.""",
    verbose=True
)

code_writing_agent = Agent(
    role='Developer',
    goal='Write code solutions based on the plan given by the planner agent. You need to access the files, analyze the relevant code, implement fixes, and submit the modified code to the repository agent for integration and testing.',
    backstory="""As a developer immersed in solving real-world coding challenges, your expertise lies in translating detailed plans into actionable code solutions. You engage with GitHub repositories, retrieve specific files, and meticulously craft code modifications to address identified issues. Your role extends beyond coding to ensuring the integrity and functionality of the software. Collaboration with other agents, like the repository agent, is essential to seamlessly integrate your solutions and validate their effectiveness through rigorous testing.""",
    verbose=True
)


tester_agent = Agent(
    role='Tester',
    goal='Validate and test code solutions',
    backstory="""You are a meticulous tester dedicated to ensuring the quality and reliability of software solutions. Your role is pivotal in the development lifecycle, where you rigorously assess code modifications crafted by developers. Armed with a keen eye for detail and a robust understanding of testing methodologies, you meticulously execute test cases, scrutinize functionality, and validate that the implemented code meets stringent quality standards. Your insights and feedback play a crucial role in refining software solutions, ensuring they not only meet but exceed user expectations.""",
    verbose=True
)

# Define tasks
task_plan_agent = Task(
    description='make a plan to solve this issue in the repo. here is the issue link : https://github.com/hiteshbandhu/notes-ai-and-tech/issues/4 ',
    expected_output='A list of the changes to be made to the code to solve the issue.',
    agent=plan_agent,
    tools=[github_search_tool, rag_tool]
)

task_code_writing_agent = Task(
    description='Find the required files to modify and solve the issue.',
    expected_output='Code modifications that address the identified GitHub issue.',
    agent=code_writing_agent,
    tools=[github_search_tool, directory_read_tool]
)

task_tester_agent = Task(
    description='Clone the github repo in the parent directory you are, just assume you are in the correct directory to run the code,you have the link already using the repo, make sure the code your write for terminal is safe before running and use only commands that are safe, not dangeruous for system, you can use git and all the cmd-line tools you need, and then, mkae the changes given by the writing agent into the files and write them. Then, check if it working as expected, the logic and pass or fail it',
    expected_output='Test results confirming the functionality and quality of the code.',
    agent=tester_agent,
    tools=[code_interpreter_tool]
)

# Define the Crew
crew = Crew(
    agents=[plan_agent, code_writing_agent, tester_agent],
    tasks=[task_plan_agent, task_code_writing_agent, task_tester_agent],
    verbose=2  # Set verbose level to 2 for detailed output
)

# Execute the Crew's tasks
result = crew.kickoff()
print(result)
