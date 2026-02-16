# 💬 30 Days of AI — Day 11  
## Displaying Chat History

The **#30DaysOfAI** challenge helps you learn how to build real-world AI applications using **:contentReference[oaicite:0]{index=0}**.

On **Day 11**, we upgrade our chatbot from *“looks like it remembers”* to *“actually remembers”*.  
We enhance the chat experience by:

- Adding a welcome message
- Displaying conversation statistics
- Allowing users to clear chat history
- Passing **full conversation context** to the LLM
- Forcing UI updates for a smoother UX

This is the day your chatbot gains **true conversational memory**.

---

## 🎯 Objective

- Initialize the chatbot with a friendly welcome message
- Display conversation stats (user vs AI messages)
- Add a “Clear History” button
- Pass full chat history to the LLM for context
- Keep sidebar metrics in sync using `st.rerun()`

---

## ✅ Prerequisites

Before Day 11, you should be comfortable with:

### 1. Streamlit Fundamentals
- Understanding Streamlit’s rerun model
- Using columns, sidebar, and basic widgets

### 2. Chat UI Elements (Days 8–10)
- `st.chat_message`
- `st.chat_input`
- Rendering chat bubbles dynamically

### 3. Session State (Days 9–10)
- Persisting data using `st.session_state`
- Initialization patterns to avoid resets
- Storing messages as a list of dictionaries

### 4. LLM Calls with Snowflake Cortex
- Calling LLMs using `ai_complete`
- Parsing JSON responses
- Why SQL-based calls are reliable across environments

---

## 🧠 The Core Problem (From Day 10)

On Day 10:
- Messages were stored and displayed
- The UI showed chat history
- ❌ The LLM only saw the **latest message**

This caused confusing behavior where:
- Users could ask follow-up questions
- But the AI had no idea what came before

The chatbot *looked* stateful — but the AI wasn’t.

---

## ✅ The Key Fix (Day 11)

The solution is simple but powerful:

> **Send the entire conversation history to the LLM every time**

By rebuilding the conversation from Session State and passing it as a single prompt, the AI can:
- Answer follow-up questions
- Maintain context
- Reference earlier messages naturally

This is how real chatbots work.

---

## 🔑 Important Building Blocks

### 1️⃣ Welcome Message Initialization

Instead of starting with an empty chat:
- The chatbot initializes with an assistant greeting
- This improves UX and avoids a blank screen
- The message is stored in Session State like any other message

This also becomes the **reset state** when clearing history.

---

### 2️⃣ Sidebar Conversation Statistics

The sidebar displays:
- Number of user messages
- Number of assistant responses

Why this matters:
- Makes the app feel more interactive
- Gives users visibility into the conversation flow
- Demonstrates how Session State can power analytics

Metrics are computed by filtering messages by role.

---

### 3️⃣ Clear Chat History Button

Users can reset the conversation at any time.

When clicked:
- Session State is reset to the initial welcome message
- The app is immediately rerun

This mirrors the “New Chat” behavior seen in real AI products.

---

### 4️⃣ Rendering Message History

Every rerun:
- The app loops through stored messages
- Each message is rendered using its role
- Messages support rich formatting via Markdown

This reconstructs the full conversation visually on every interaction.

---

### 5️⃣ Loading Feedback with Spinner

While the LLM is generating a response:
- A spinner shows the assistant is “thinking”
- Prevents the app from feeling frozen
- Improves perceived performance

This will later be replaced by streaming responses.

---

### 6️⃣ Passing Full Conversation Context (Most Important)

This is the heart of Day 11.

Instead of sending only the latest user message:
- The entire conversation is rebuilt from Session State
- Messages are clearly labeled as `User:` and `Assistant:`
- The full conversation is sent to the LLM

This gives the AI **real memory**, not just UI memory.

---

### 7️⃣ Immediate UI Updates with `st.rerun()`

After adding the assistant’s response:
- The app forces a rerun
- Sidebar metrics update instantly
- No lag between messages and stats

Without this, the sidebar would always be one step behind.

---

## 🚀 Why Day 11 Matters

Day 11 transforms your chatbot into something realistic:

You now have:
- True conversational memory
- Context-aware AI responses
- Conversation analytics
- Chat reset functionality
- Production-style UX patterns

This is the foundation for:
- Streaming chat
- RAG-based assistants
- Tool-using agents
- Multi-turn reasoning

---

## 🔜 What’s Next?

Upcoming improvements include:
- Streaming responses instead of spinners
- Smarter prompt construction
- Token-efficient memory handling
- Advanced chat UX patterns

Your chatbot is officially **stateful, contextual, and user-friendly** 🎉

---

## 📚 Resources

- Streamlit Session State Documentation  
- `st.metric` Documentation  
- `st.rerun` Documentation  
- Snowflake Cortex LLM Functions  
