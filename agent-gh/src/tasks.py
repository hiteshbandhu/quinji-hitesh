from crewai import Task
from agents import qa_agent, cheif_qa, planning_agent, code_agent
from textwrap import dedent


review_task = Task(description=dedent(f"""\

			Using the code you got, check for errors. Check for logic errors,
			syntax errors, missing imports, variable declarations, mismatched brackets,
			and security vulnerabilities.

			Your Final answer must be the full python code, only the python code and nothing else.
			"""),
			agent=qa_agent
		)

evaluate_task = Task(description=dedent(f"""
			You will look over the code to insure that it is complete and
			does the job that it is supposed to do.

			Your Final answer must be the full python code, only the python code and nothing else.
			"""),
			agent=cheif_qa
		)


code_task = Task(description=dedent(f"""
			Your Final answer must be the full python code, only the python code and nothing else.
			"""),
			agent=code_agent
		)

plan_task = Task(description=dedent(f"""
			You have to find the relavant issues to the {domain} and give the full description and a full plan to the coder agent to fix this issue and nothing else.
			"""),
			agent=code_agent
		)
