## initializing the environment

- ```source env/bin/activate```
- ```pip install -r requirements.txt```
- ```cd src```

-- the src directory has the main code, always run the code from this directory

## part 1 : flow and architecture of the agent

1. `INPUT` : Github Token, Github Repo Link and User-Preference
2. `Issues` : Selects the best issues based on the preference
3. `Parse` : Parses and reads the issue and finds the related to files to the issue
4. `Test cases` : Write test cases to check the issues
5. `Solve` : Solves the issues, and executes the code against the tests
6. `Result` : If tests are passed, then a pull request is made to the original codebase

-- this is very high-level overview, later we will have to add code execution, how to pull request and write comments from the command line etc.




