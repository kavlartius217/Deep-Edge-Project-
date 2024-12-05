import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import SerpAPIWrapper
from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# Page config with custom CSS for dark green background with vignette effect
st.markdown("""
    <style>
        .stApp {
            background: radial-gradient(circle at center, #0A2615 0%, #061510 100%);
        }
        
        /* Make text white */
        .stMarkdown, .stText, div[data-testid="stText"] {
            color: white;
        }
        
        /* Style for text input */
        .stTextInput input {
            color: white;
            background-color: rgba(255, 255, 255, 0.1);
            border-color: rgba(255, 255, 255, 0.2);
        }
        
        /* Title color */
        .stTitle {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Get API keys from secrets
groq_api_key = st.secrets["GROQ_API_KEY"]
serp_api_key = st.secrets["SERP_API_KEY"]

# importing the llm
llm = ChatGroq(model_name="mixtral-8x7b-32768", api_key=groq_api_key, temperature=0.3)

# creating the search tool
search = SerpAPIWrapper(serpapi_api_key=serp_api_key)
search_tool = Tool.from_function(
    name="search_tool",
    func=search.run,
    description="does a google search and returns current data"
)

# creating a prompt for the llm
prompt = hub.pull("hwchase17/react-chat")

# now creating a chatbot using agents
agent = create_react_agent(llm=llm, tools=[search_tool], prompt=prompt)

# executing the agent
agent_exec = AgentExecutor(agent=agent, llm=llm, tools=[search_tool], verbose=True, handle_parsing_errors=True)

# Chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def response(user_input):
    llm_response = agent_exec.invoke({"input": user_input, "chat_history": st.session_state.chat_history})
    st.session_state.chat_history.append(llm_response['input'])
    st.session_state.chat_history.append(llm_response['output'])
    return llm_response

# Streamlit UI
st.title("🔍Langchain Research Assistant")
user_input = st.text_input("💭 Ask a question:")
if user_input:
    with st.spinner('🤔 Searching and thinking...'):
        bot_response = response(user_input)
        st.write("🤖:", bot_response['output'])
