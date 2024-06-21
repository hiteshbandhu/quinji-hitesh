## This project implements a simple agent which queries the python-official-documentation to code a snake game.


### Part 1  : Setup

- make a virtual environment using the ```python -m venv env``` command
- activate it using ```source env/bin/activate```
- install the dependencies using ```pip install -r requirements.txt```
- move in to the src folder ``` cd src```
- run the file as specified using ```python -m {filename}```

### Part 2  : File Structure

- ```.env``` file has all the environment variables
- ```src/library.pdf``` is the python std library 
- ```snake-agent.py``` is the main agent file

### Part 3 : Running the code

#### 3.1 load_dotenv

- you can't depend on the shell to automatically detect the env variables, works in some, not in others, so we use the ```load_dotenv()``` function to load them in the file and any function can access it then 

```python
from dotenv import load_dotenv
load_dotenv()
```

#### 3.2 import crewai and dependencies

- now, we import the three things we need to run an agent 
    - Agents
    - Tasks
    - Tools

##### This is the code for agents part
```python
from crewai import Agent, Task, Crew
from crewai_tools import PDFSearchTool

code_agent = Agent(
  role='Programmer',
  goal='Code a Snake Game in Python',
  backstory="""You're a python developer specialising in developing small arcade games just using the python documentaion, and not using any internet. You just use the PDF you have access to - to read the documentation and code the games.""",
  verbose=True
)
```
- parameters explained : 
    - ```role``` : role the agent acts as if it were a human
    - ``goal`` : what is the end goal of the agent
    - `backstory` : explain who the agent is and what is it's work and persona

##### This is the code for tools and agents
```python
pdf_tool = PDFSearchTool("library.pdf")

task = Task(
  description='Code a Snake Game in Python',
  expected_output='Python Code for a simple Snake Game.',
  agent=code_agent,
  tools=[pdf_tool]
)
```

- parameters explained
    - ```pdf-tool``` : stores the file in a local db and then uses it to query later
    - ```descripion``` : what is the task to complete ?
    - ```expected output``` : what is the format/or how the output should look like ?
    - ```agent``` : which agent is assigned this task
    - `tools` : the tools the agent can use while performing this task


##### This is the code for kicking in the crew and performing the task

```python
crew = Crew(
    agents=[code_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff(output_token_usage=True)
print(result)
```

- parameters explained
    - `agents` : the agents to use in the crew
    - `tasks` : the tasks to perform
    - `verbose` : will explain everything it does in a terminal
    - `crew.kickoff` - runs the crew and tracks output usage of tokens


### Part 4 : Result in the terminal

- here is the result in a code block

```txt
 [2024-06-21 14:42:36][DEBUG]: == Working Agent: Programmer
 [2024-06-21 14:42:36][INFO]: == Starting Task: Code a Snake Game in Python


> Entering new CrewAgentExecutor chain...
I need to think about the main components and functionalities required to code a simple Snake Game in Python. Generally, a Snake Game will need:

1. A game window.
2. A snake that can move in four directions.
3. Food that the snake can eat to grow.
4. A mechanic to check for collisions (with the walls or itself).

To implement these components, I need to look for relevant information on how to create a game window, draw the snake and food, handle user input, and detect collisions using the Python standard library.

Thought: I should start by searching for information on creating a game window, which is a fundamental aspect of any graphical game.

Action: Search a PDF's content
Action Input: {"query": "create game window"}
 

Relevant Content:
Andafterawhile,itwillprobablyhelptoclearthewindowsowecanstartanew: clearscreen() 24.1. turtle—Turtlegraphics 1563

Screenobjectcreatedautomaticallywhen neededforthefirsttime. 1594 Chapter24. ProgramFrameworks

TurtlegraphicsinaTkwindow. 1616 Chapter25. GraphicalUserInterfaceswithTk

Thought: It appears that the PDF contains information related to creating a game window using the Turtle graphics library and possibly Tkinter (Tk) for creating graphical user interfaces. I should now look into how to draw objects on the screen, which would be the snake and food in our game.

Action: Search a PDF's content
Action Input: {"query": "draw objects with turtle graphics"}
 

Relevant Content:
closingtheturtlegraphicswindow. Useobject-orientedturtlegraphics See also: Explanation of the object-oriented interface Otherthanforverybasicintroductorypurposes,orfortryingthingsoutasquicklyaspossible,it’smoreusualandmuch morepowerfultousetheobject-orientedapproachtoturtlegraphics. Forexample,thisallowsmultipleturtlesonscreen atonce. In this approach, the various turtle commands are methods of objects (mostly of Turtleobjects). You canuse the object-orientedapproachintheshell,butitwouldbemoretypicalinaPythonscript. Theexampleabovethenbecomes: from turtle import Turtle from random import random t=Turtle() for iinrange (100): steps =int(random() *100) angle =int(random() *360) t.right(angle) t.fd(steps) t.screen .mainloop() 24.1. turtle—Turtlegraphics 1565

turtle—Turtlegraphics 1571

ThePythonLibraryReference,Release3.12.4 Basicdrawing Sendtheturtleforward100steps: forward( 100) You should see (most likely, in a new window on your display) a line drawn by the turtle, heading East. Change the directionoftheturtle,sothatitturns120degreesleft(anti-clockwise): left( 120) Let’scontinuebydrawingatriangle: forward( 100) left( 120) forward( 100) Noticehowtheturtle,representedbyanarrow,pointsindifferentdirectionsasyousteerit. Experimentwiththosecommands,andalsowith backward() andright(). Pencontrol Trychangingthecolor-forexample, color('blue') -andwidthoftheline-forexample, width(3) -andthen drawingagain. Youcanalsomovetheturtlearoundwithoutdrawing,byliftingupthepen: up()beforemoving. Tostartdrawingagain, usedown(). Theturtle’sposition Sendyourturtlebacktoitsstarting-point(usefulifithasdisappearedoff-screen): home() Thehomepositionisatthecenteroftheturtle’sscreen. Ifyoueverneedtoknowthem,gettheturtle’sx-ycoordinates with: pos() Homeisat (0, 0).

Thought: I now have enough information on creating a game window and drawing objects using the Turtle graphics library. I will proceed with coding the Snake Game using the standard Python library and Turtle graphics.

Final Answer: Here is the complete Python code for a simple Snake Game using the Turtle graphics library.

```python
import turtle
import time
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear the segments list
            segments.clear()

    time.sleep(0.1)
```

This code creates a simple Snake Game using the Turtle graphics library in Python. The game window is set up, the snake and food are drawn, and the snake can be controlled using the "w", "a", "s", and "d" keys. The game includes collision detection for the snake hitting the walls or itself.

> Finished chain.
 [2024-06-21 14:43:19][DEBUG]: == [Programmer] Task output: Here is the complete Python code for a simple Snake Game using the Turtle graphics library.

```python
import turtle
import time
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear the segments list
            segments.clear()

    time.sleep(0.1)
```

This code creates a simple Snake Game using the Turtle graphics library in Python. The game window is set up, the snake and food are drawn, and the snake can be controlled using the "w", "a", "s", and "d" keys. The game includes collision detection for the snake hitting the walls or itself.


Here is the complete Python code for a simple Snake Game using the Turtle graphics library.

```python
import turtle
import time
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            # Clear the segments list
            segments.clear()

    time.sleep(0.1)
```

This code creates a simple Snake Game using the Turtle graphics library in Python. The game window is set up, the snake and food are drawn, and the snake can be controlled using the "w", "a", "s", and "d" keys. The game includes collision detection for the snake hitting the walls or itself.






```
