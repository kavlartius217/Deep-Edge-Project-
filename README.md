PLEASE RELOAD IF THE AGENT HITS ITERATION LIMIT.
This is a project completely based on langchain components.
The search tool can access google and retrieve the top results.
This tool retrieves the top results preprocesses them and makes it available for the llm.
The function of the agent is to determine whether to use the tool (google search) or to use the llm's existing data on which it has been trained.
In case we have multiple tools such as a Wikipedia tool or an arxiv tool the agent will choose which one to use and it will do so based on the user query.
Here we have used the react agent there are several types of agents.
React stands for reasoning and action as a result it is good at conversations.
Chat history has also been initialized.
