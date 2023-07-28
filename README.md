# GPT Todo List

Implementing a to-do list is an important rite of passage when learning a new
application development framework, so it woud be fitting to make one with GPT
and Langchain.

In this demo, we take a ToDoList class we've prepared in advanced (well ... we
had ChatGPT prepare it for us, of course), and we chain it to GPT-3.5 by
passing the methods for interacting with the list as Langchain tools.

When interacting with the chat, it figures how to use the tools to read and
modify the to-do list, thus becoming our UI.

This demo is a bit limited - as you'll see, the instructions we give the chat
are quite specific and there is not a lot of planning done by the chatbot,
beyond a couple of steps. Still it's pretty cool to be able to chat to a to-do
list and have an AI agent modify it on our behalf. And there's a challenge for
future iterations: to make the bot acceppt more absrtact requests and do more
of the planning itself.

See [gpt-todo.ipynb](gpt-todo.ipynb)

Another implementation relies on the native Open AI function calling API,
without relying on LangChain for orchestration. It works well for simple
requests, but fails in complex interactions that require chaining multiple
function calls.

See [gpt-todo-functions.ipynb](gpt-todo-functions.ipynb)
