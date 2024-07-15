from gh_agents import qa_agent, cheif_qa, planning_agent, code_agent
from gh_tasks import review_task, code_task, evaluate_task, plan_task
from crewai import Crew

domain = input("What domain of issues you want to solve (frontent, backend, docker, etc.) :>   ")

crew = Crew(
    agents=[planning_agent, code_agent, qa_agent, cheif_qa],
    tasks=[review_task, code_task, evaluate_task, plan_task],
    verbose=10
)

result = crew.kickoff({"domain" : domain})

print(result)