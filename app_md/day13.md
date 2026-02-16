# Day 13 – Adding a System Prompt 🎭  
## 30 Days of AI with Streamlit

Day 13 builds on the streaming chatbot from Day 12 and introduces **system prompts** to give the AI a **personality**.

By changing a single instruction, the same AI can behave like a **pirate**, **teacher**, **comedian**, or **robot**—showing how powerful prompt engineering can be in real applications.

---

## 🎯 What You’ll Learn

- What system prompts are and why they matter
- How to control AI behavior using instructions
- How to switch AI personas dynamically in Streamlit
- How to combine system prompts with streaming responses
- How to persist personality across reruns using session state

---

## 📌 Prerequisites

Before running this app, you should have:

- Basic knowledge of **Python**
- Familiarity with **Streamlit chat components**
- Completion of **Day 12 (Streaming Responses)**
- A **Snowflake account** with Cortex enabled

### Tools & Platforms
- **:contentReference[oaicite:0]{index=0}**
- **:contentReference[oaicite:1]{index=1}**
- Snowflake Cortex (`ai_complete`)

---

## 🧠 What’s Kept from Day 12

All core chatbot functionality remains unchanged:

- Streaming responses using `st.write_stream()`
- Custom Python generator for smooth streaming
- Conversation history stored in session state
- Sidebar conversation statistics
- Clear History button
- Spinner indicating processing status

---

## ✨ What’s New in Day 13

### 1. System Prompt (AI Personality)

A **system prompt** is an instruction that defines *how* the AI should behave, not just *what* it should answer.

Examples:
- Speak like a pirate
- Teach patiently like a professor
- Respond humorously like a comedian
- Act logically like a robot

This prompt is injected **before** the conversation history so it controls every response.

---

### 2. Early Initialization with Session State

The system prompt is initialized early using `st.session_state` so that:

- It persists across reruns
- Sidebar controls can update it safely
- The chatbot always stays in character

The welcome message is also aligned with the default personality to maintain consistency.

---

### 3. Preset Personality Buttons (Sidebar)

The sidebar includes **quick preset buttons** that instantly switch personas.

Why this matters:
- Improves user experience
- Demonstrates real-time prompt changes
- Allows rapid comparison of AI behavior

Each button updates the system prompt and triggers a rerun so changes take effect immediately.

---

### 4. Editable System Prompt Text Area

Below the presets is a text area bound directly to the system prompt.

Key benefits:
- Users can tweak preset personalities
- Fully custom prompts are supported
- No session state conflicts
- Encourages prompt experimentation

This turns the app into a **prompt engineering playground**.

---

### 5. Injecting System Prompt into Streaming Flow

When generating a response:
- The system prompt is placed **at the very top**
- Conversation history follows
- The AI is explicitly told to “stay in character”

The response is then streamed word-by-word using the same generator approach from Day 12.

This ensures:
- Personality consistency
- Real-time feedback
- Professional chat experience

---

## 🧠 Why System Prompts Matter

System prompts are critical because they:

- Define AI behavior and tone
- Enable role-based assistants
- Enforce style and constraints
- Make AI outputs predictable and controllable
- Power real-world applications like tutors, support bots, and domain experts

Changing the system prompt alone can completely transform how the AI responds to the **same input**.

---

## ✅ End Result

By the end of Day 13, you have:

- A streaming AI chatbot
- A personality selector in the sidebar
- Editable system instructions
- Persistent behavior across messages
- A strong foundation in prompt engineering

Ask the same question with different personas and see how dramatically the answers change.

---

## 📚 Helpful Resources

- Prompt Engineering Guide
- Streamlit `st.text_area()` Documentation
- System Prompt Best Practices

---

**Day 13 Complete 🎉**  
_System prompts turn a chatbot into a character-driven AI experience._
