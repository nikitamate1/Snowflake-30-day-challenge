# 💬 30 Days of AI — Day 10  
## Your First Chatbot (with State)

The **#30DaysOfAI** challenge is designed to help you build real-world AI applications using **:contentReference[oaicite:0]{index=0}**.

On **Day 10**, we combine everything learned so far—**chat UI elements** and **session state**—to build our **first working chatbot** that remembers the conversation across user interactions.

This marks the transition from *static demos* to *stateful, conversational AI apps*.

---

## 🎯 Objective

- Build a chatbot UI using Streamlit chat components
- Store conversation history using Session State
- Render past messages on every rerun
- Generate AI responses using **:contentReference[oaicite:1]{index=1} Cortex LLMs**
- Create a chatbot that **does not forget** previous messages

---

## ✅ Prerequisites

Before starting Day 10, you should be familiar with:

### 1. Streamlit Basics
- Creating interactive apps with Streamlit
- Understanding that Streamlit reruns the script on every interaction

### 2. Chat UI Elements (Day 8)
- `st.chat_message` for chat bubbles
- `st.chat_input` for user input

### 3. Session State (Day 9)
- Why normal variables reset
- How `st.session_state` persists data
- The initialization pattern (`if key not in st.session_state`)

### 4. Snowflake Cortex (Optional but Recommended)
- Basic idea of calling LLMs using `ai_complete`
- Understanding that the model response is returned as JSON

---

## 🧠 Core Concept: Chatbot Memory

A chatbot is simply a loop of messages:

1. User sends a message  
2. Assistant responds  
3. Both messages are saved  
4. Entire conversation is re-rendered on every interaction  

Without **Session State**, steps 3 and 4 are impossible.

---

## 🗂️ Message Storage Format

Messages are stored as a list of dictionaries, where each message contains:

- `role`: who sent the message (`user` or `assistant`)
- `content`: the text of the message

This structure is **industry standard** and used by most chat-based LLM APIs, making it highly transferable beyond Streamlit.

---

## 🔑 Important Building Blocks

### 1️⃣ Initializing Chat Memory (Once)

The chatbot creates a message list inside Session State **only if it does not already exist**.

Why this matters:
- Prevents the conversation from resetting
- Ensures messages persist across reruns
- This is the same initialization pattern learned on Day 9

---

### 2️⃣ Rendering Chat History

On every rerun:
- The app loops through all stored messages
- Each message is rendered using its stored role
- The UI reconstructs the entire conversation

This makes the chatbot *feel continuous*, even though the script reruns every time.

---

### 3️⃣ Handling New User Input

When the user submits a message:
- The input is captured from the chat input box
- The message is immediately added to Session State
- The message is rendered in a user chat bubble

This ensures the user sees their message instantly.

---

### 4️⃣ Generating and Storing AI Responses

After receiving user input:
- The app calls Snowflake Cortex using `ai_complete`
- The AI-generated response is displayed
- The response is stored in Session State using the same format

This completes **one full conversation turn**.

---

## 🤔 Why Use SQL-based `ai_complete`?

This app uses Snowflake’s **SQL-based Cortex function** instead of a Python SDK because:

- It works consistently across:
  - Streamlit in Snowflake
  - Streamlit Community Cloud
  - Local development
- Avoids SSL and environment issues
- Provides a single, reliable deployment strategy

This makes the chatbot more **portable and production-friendly**.

---

## ⚠️ Current Limitations (By Design)

This chatbot is intentionally simple. It currently lacks:

- Loading indicators or typing animation
- Streaming responses
- Error handling
- Reset / clear chat button
- Message counters or analytics
- Visual personality or customization

These gaps are **intentional** and will be addressed in upcoming days.

---

## 🚀 Why Day 10 Is Important

Day 10 is a **major milestone** in the challenge.

You now have:
- A stateful application
- A real chatbot architecture
- A reusable message format
- The foundation for RAG, tools, and agents

Everything built from here will extend this core pattern.

---

## 🔜 What’s Next?

Upcoming improvements will include:
- Streaming responses
- Status indicators
- Chat reset functionality
- Better UX and error handling
- Smarter, context-aware AI behavior

**Day 10 complete — you’ve built your first real chatbot 💬🤖**

---

## 📚 Resources

- Streamlit Chat Elements Documentation  
- Streamlit Session State Guide  
- Snowflake Cortex Complete Function  
