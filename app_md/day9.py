# 🧠 30 Days of AI — Day 9  
## Understanding Session State

The **#30DaysOfAI** challenge helps you build modern AI applications using **:contentReference[oaicite:0]{index=0}**.

On **Day 9**, we solve one of the most important problems in Streamlit app development:

> ❓ Why does my app forget everything after I click a button?

This issue is commonly called the **Amnesia Problem**, and today’s goal is to understand *why it happens* and *how Session State fixes it*.

---

## 🎯 Objective

- Understand why normal Python variables reset in Streamlit
- Learn how Streamlit reruns scripts on every interaction
- Use **Session State** to persist values across reruns
- Build a counter that actually remembers its value

This concept is **foundational** for:
- Chatbots
- Multi-step workflows
- Stateful AI applications

---

## ✅ Prerequisites

Before starting Day 9, you should be comfortable with:

### 1. Streamlit Fundamentals
- Creating buttons and layout elements
- Understanding that Streamlit reruns the script on every user interaction

### 2. Python Basics
- Variables and conditionals
- Dictionaries (important for understanding Session State)

### 3. Completed Day 8
- Familiarity with Streamlit’s chat UI
- Awareness that messages disappear without stored state

---

## 🧠 Key Concept: Why State Is Lost

Streamlit works differently from traditional web frameworks.

### Important Rule:
📌 **Every button click reruns your entire Python script from top to bottom.**

That means:
- All normal variables are recreated
- Previous values are lost
- Your app appears to “forget” everything

This is expected behavior — not a bug.

---

## ❌ The Wrong Way: Standard Variables

A regular Python variable is recreated on every rerun.

What happens:
- The variable is reset to its initial value
- Increment or decrement happens *after* the reset
- The value never grows beyond `+1` or `-1`

**Key takeaway:**  
Standard variables **cannot store memory** in Streamlit apps.

---

## ✅ The Right Way: Session State

Streamlit provides **Session State** to persist data across reruns.

Think of it as:
> 🧠 A dictionary that survives script reruns for a user session

### The Session State Pattern

There are **three essential steps**:

#### 1️⃣ Initialization (Run Once)
- Create the state variable only if it does not already exist

#### 2️⃣ Modification
- Update the value stored in Session State
- Changes persist across reruns

#### 3️⃣ Reading
- Display the value directly from Session State

This pattern ensures:
- The value is not reset
- Each click builds on the previous state

---

## 🔑 Why the Initialization Check Matters

The condition:

> “Only create the value if it doesn’t exist”

is the **most important rule** of Session State.

Without it:
- The value would reset on every rerun
- Session State would behave like a normal variable

With it:
- The value is created once
- Future reruns reuse the stored value

---

## 📊 Visual Comparison (What You Observe)

| Approach | Behavior |
|--------|---------|
| Standard Variable | Resets on every click |
| Session State | Remembers previous value |
| User Experience | Broken | Predictable & correct |

This side-by-side comparison makes it clear **why Session State is essential**.

---

## 🚀 Why This Matters for AI Apps

Session State is the backbone of:
- Chat history in chatbots
- Multi-turn AI conversations
- Form wizards and workflows
- Any app that needs memory

Without Session State:
- Chatbots forget messages
- AI apps feel broken
- User experience degrades

With Session State:
- Apps feel intelligent and consistent

---

## 🔜 What’s Next?

Now that we understand **how memory works in Streamlit**, we’re ready to:

- Store chat messages
- Build a chatbot that remembers context
- Connect Session State with LLM responses

**Day 9 complete — your app now has a memory 🧠**

---

## 📚 Resources

- Streamlit Session State Documentation  
- Streamlit Session State Guide  
