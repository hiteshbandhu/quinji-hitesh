from crewai import Agent, Task, Crew
from crewai_tools import JSONSearchTool 

context = input("*** Enter Your Input Query >  \t")

research_agent = Agent(
  role='Researcher',
  goal=f"""Find me the best advice in 7 bullet points using the context. here is the context : {context}""",
  backstory="""You're a JSON reader, who can read data and summarize it bullet points, that are very comprehensive and full of insights""",
  verbose=True
)

json_tool = JSONSearchTool("content.json")

task = Task(
  description='Find me the best advice in 7 bullet points using the context',
  expected_output='7 Bullet points and one summary',
  agent=research_agent,
  tools=[json_tool]
)

crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=2
)

result = crew.kickoff()
print(result)