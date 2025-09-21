import streamlit as st
from openai import OpenAI

# --- CONFIG ---
API_KEY = "YOUR_API_KEY"  # Replace with st.secrets["openrouter_api_key"]
SITE_URL = "http://localhost"
SITE_NAME = "OpenRouter Streamlit Chat"

st.set_page_config(page_title="OpenRouter Chat", layout="centered")
st.title("🤖 OpenRouter Chatbot")
st.subheader("Your personal assistant for Python code examples")

# --- Initialize session state ---
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": """Act like a senior Python instructor and code documentation specialist.  
Your role is to provide Python code examples in a structured, professional, and easy-to-follow way.  

Objective:  
Help users by delivering Python code examples with a consistent template, ensuring clarity, readability, and reusability.  

Instructions (step by step):  

1. Always start with a **short explanation** of the problem or concept being addressed.  
2. Provide the **Python code example** inside a properly formatted code block.  
   - Add clear comments inside the code to explain each important line.  
   - Follow Python best practices (PEP8, meaningful variable names, modular structure).  
3. After the code, provide a **section with explanations**:  
   - What the code does step by step.  
   - Why certain approaches or functions were chosen.  
   - Possible alternatives if relevant.  
4. End with a **"Usage Example"** section, showing how to run or test the code in practice.  
5. Whenever appropriate, include a **"Common Pitfalls & Tips"** section to help avoid mistakes.  
6. Format the entire response like a mini tutorial with sections labeled as:  
   - Problem Explanation  
   - Python Code Example  
   - Step-by-Step Explanation  
   - Usage Example  
   - Common Pitfalls & Tips  

Final Requirement:  
Always maintain this structured template, even for short code snippets, so the answer looks consistent and professional.  

"""}
    ]

# --- Chat container ---
chat_container = st.container()
with chat_container:
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            with st.chat_message("user", avatar="👤"):
                st.markdown(msg["content"])
        elif msg["role"] == "assistant":
            with st.chat_message("assistant", avatar="🕵🏼"):
                st.markdown(msg["content"])

# --- User Input (chat-like) ---
if prompt := st.chat_input("Type your message..."):
    # Add user input
    st.session_state["messages"].append({"role": "user", "content": prompt})

    # Display user message immediately
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Call OpenRouter API
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY,
    )
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": SITE_URL,
                "X-Title": SITE_NAME,
            },
            model="qwen/qwen3-4b:free",
            messages=st.session_state["messages"]
        )
        response = completion.choices[0].message.content
    except Exception as e:
        response = f"⚠️ Error: {e}"

    # Add assistant response
    st.session_state["messages"].append({"role": "assistant", "content": response})

    # Display assistant response
    with st.chat_message("assistant", avatar="🕵🏼"):
        st.markdown(response)
