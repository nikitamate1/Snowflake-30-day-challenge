# 💬 30 Days of AI — Day 8  
## Meet the Chat Elements

The **#30DaysOfAI** challenge is designed to help you build modern AI applications using **:contentReference[oaicite:0]{index=0}**.

Welcome to **Week 2** 🎉  
In Week 1, we focused on **linear apps**:

> Input → Process → Output

Starting Day 8, we move into **conversational AI interfaces**, where applications behave more like chatbots.  
Before adding memory or AI logic, today’s focus is purely on the **chat user interface (UI)**.

---

## 🎯 Objective

- Learn Streamlit’s native chat UI components
- Render user and assistant chat bubbles
- Accept user input through a chat-style textbox
- Understand why chat history disappears (and why that’s expected for now)

⚠️ This is **not a full chatbot yet** — it’s the **visual skeleton** of one.

---

## ✅ Prerequisites

Before starting Day 8, you should have:

### 1. Streamlit Basics
- Familiarity with `st.write`, layout, and widgets
- Understanding that Streamlit reruns the script on every interaction

### 2. Completed Week 1 (Days 1–7)
- Built basic Streamlit apps
- Used layout elements like sidebar and containers
- Worked with user inputs and outputs

### 3. Local Setup
- Python 3.9+
- Streamlit installed
- No Snowflake or LLM access required for Day 8

---

## 🧠 Key Concepts Explained

### 1. Chat Message Containers

Streamlit provides `st.chat_message()` to visually represent chat bubbles.

Each message is associated with a **role**:
- `user`
- `assistant`

Streamlit automatically:
- Aligns messages left/right
- Assigns avatars
- Styles bubbles appropriately

**Why this matters:**  
You no longer need to manually design chat layouts — Streamlit handles this natively.

---

### 2. Rich Content Inside Chat Bubbles

Chat messages are not limited to plain text.

They can include:
- Charts
- Tables
- Images
- Markdown
- Any Streamlit component

This makes chat-based AI apps far more expressive than simple text-only bots.

---

### 3. Chat Input Widget

`st.chat_input()` creates:
- A text box pinned to the bottom of the screen
- A natural chat-like typing experience

Unlike regular input widgets, it:
- Automatically manages layout
- Only returns a value when the user presses **Enter**

This mirrors real chat applications and improves UX significantly.

---

### 4. Reacting to User Input

Once a message is submitted:
- The user’s message is displayed in a chat bubble
- A mock assistant response is generated

At this stage:
- The app **does not remember previous messages**
- Each new interaction triggers a full script rerun

This behavior is intentional and highlights an important limitation we’ll fix next.

---

### 5. The “Disappearing Messages” Problem

You may notice:
- First message appears
- Second message removes the first

This happens because:
- Streamlit reruns the script from top to bottom
- No chat history is stored yet

📌 **Key takeaway:**  
To build real chatbots, we must store conversation history — which requires **Session State**.

This sets the stage perfectly for **Day 9**.

---

## 🟢 Expected Outcome

When you run the app:
- You see chat-style user and assistant bubbles
- Messages appear visually correct
- Input feels like a real chat interface
- Messages disappear on new input (expected behavior)

This confirms:
- Chat UI elements are working correctly
- The app is ready for memory integration

---

## 📚 Resources

- Streamlit `st.chat_message` Documentation  
- Streamlit `st.chat_input` Documentation  
- Building Chat Apps with Streamlit  

---

## 🚀 What’s Next?

In **Day 9**, we’ll introduce:
- Session State
- Persistent chat history
- The foundation for a real conversational AI app

**Day 8 complete — your chatbot now has a face, next it gets a memory 🧠💬**
