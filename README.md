PLEASE RELOAD IF THE AGENT HITS ITERATION LIMIT.
This is project completely based on langchain components.
The search tool has the access to google and retrieves the the top results.
This tool retrieves the top results preprocesses them and makes it available fro the llm.
The function of the agent is to determine whether to use the tool (google search) or to use the llm's existing data on which it has has been trained.
In case we have multiple tools such as a wikipedia tool or an arxiv tool the agent will choose which one to use and it will do so based on the user query.
Here we have used the react agent there are several type of agents.
React stands for reasoning and action as a result it is good at conversations.
Chat history has also been initialized.
