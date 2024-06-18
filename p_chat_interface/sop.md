
This README documents the step-by-step evolution of our chat interface HTML file, detailing the changes made from the initial version to the latest one.

---

```bash
for making requirements : ``` pip freeze > requirements.txt ```
for installing from txt : ``` pip install -r requirements.txt ```
```

#### **Change 1: Basic GET Request Form**
- **Added:**
  - Basic structure to send a GET request.
  - Input field for item ID.
  - Button to submit the form.
  - Container to display the response.
- **Removed:**
  - Initial placeholder text.

#### **Change 2: CORS Handling**
- **Added:**
  - Instructions to handle CORS in FastAPI backend.
- **Removed:**
  - N/A

#### **Change 3: Chat Interface Style**
- **Added:**
  - Dark-themed styling.
  - Container for chat messages.
  - Question and response styling.
- **Removed:**
  - Basic styling.

#### **Change 4: Session Storage**
- **Added:**
  - Functionality to save questions and responses in session storage.
  - Code to clear session storage on page refresh.
- **Removed:**
  - N/A

#### **Change 5: Markdown Rendering**
- **Added:**
  - Marked.js library for rendering markdown.
  - Function to replace newlines and render response as markdown.
- **Removed:**
  - Plain text rendering of responses.

#### **Change 6: Token-by-Token Streaming**
- **Added:**
  - Interval to simulate streaming of response word by word.
- **Removed:**
  - Immediate full response rendering.

#### **Change 7: Improved Scrolling**
- **Added:**
  - Automatic scrolling to the bottom of the chat container as new messages are added.
- **Removed:**
  - Manual scrolling.

#### **Change 8: Response Formatting**
- **Added:**
  - Rendering of response as HTML.
  - Adjusted margins between question and response.
- **Removed:**
  - Extra newline characters from the response.

---
