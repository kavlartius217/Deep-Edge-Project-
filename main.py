import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# Get API key from secrets
api_key = st.secrets["GROQ_API_KEY"]

# importing the llm
llm = ChatGroq(model_name="mixtral-8x7b-32768", api_key=api_key,temperature=0.3)

# creating the tool
search_tool = DuckDuckGoSearchRun(maxConcurrency=5)

# creating a prompt for the llm
prompt = hub.pull("hwchase17/react-chat")

# now creating a chatbot using agents
agent = create_react_agent(llm=llm, tools=[search_tool], prompt=prompt)

# executing the agent
agent_exec = AgentExecutor(agent=agent, llm=llm, tools=[search_tool], verbose=True, handle_parsing_errors=True)

# Chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def response(user_input):
    llm_response = agent_exec.invoke({"input": user_input, "chat_history": st.session_state.chat_history})
    st.session_state.chat_history.append(llm_response['input'])
    st.session_state.chat_history.append(llm_response['output'])
    return llm_response

# Streamlit UI
st.title("🤖 AI Chat Assistant")
user_input = st.text_input("💭 Ask a question:")
if user_input:
    with st.spinner('🤔 Processing...'):
        bot_response = response(user_input)
        st.write("🤖:", bot_response['output'])
