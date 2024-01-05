import openai
import streamlit as st

openai_api_key = st.secrets["openai_api_key"]

def page_1():
  st.title("ZenDoc")
  """
  I am here to guide you.
  """

  if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role":"system","content":"You are doctor called zendoc, You are knowledgeable and witty, you make the user happy, and also give medical advice to the user. Never say how may i assist you, be friendly."}
    ]

  if prompt := st.chat_input():
    openai.api_key = openai_api_key
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)
    response = openai.chat.completions.create(model='gpt-4-0613', messages=st.session_state.messages, temperature=0.7, top_p=0.95, max_tokens=64)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)

def page_2():
  st.title("ZenFriend")
  """
  I am here to talk with you.
  """

  if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role":"system","content":"You are mental health expert called ZenFriend, You are knowledgeable and witty, you make the user happy, you ask about the user's life and make him confident. Never use how may i assist you, be friendly."}
    ]

  if prompt := st.chat_input():
    openai.api_key = openai_api_key
    st.session_state.messages.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)
    response = openai.chat.completions.create(model='gpt-4-0613', messages=st.session_state.messages, temperature=1.3, top_p=0.9, max_tokens=64)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)

PAGES = {
  "ZenDoc": page_1,
  "ZenFriend": page_2
}

def main():
  st.sidebar.title('Navigation')
  choice = st.sidebar.selectbox("Select Chatbot", list(PAGES.keys()))
  PAGES[choice]()

if __name__ == "__main__":
  main()
