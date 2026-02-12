# ✍️ 30 Days of AI — Day 5  
### Build a LinkedIn Post Generator App

The **#30DaysOfAI** challenge is about turning AI capabilities into real, useful applications using **Streamlit** and **Snowflake Cortex**.

On **Day 5**, we build a practical AI app that generates **professional LinkedIn posts** based on user input such as content source, tone, and length.

---

## 🎯 Objective

- Build a Streamlit web app for content generation
- Call a Snowflake Cortex LLM from the app
- Generate a LinkedIn post using structured user inputs
- Display the generated post in a clean, readable format

---

## ✅ Prerequisites

Before starting Day 5, ensure you have:

### 1. Completed Day 1–4
- Working Streamlit ↔ Snowflake connection
- Experience calling Cortex LLMs
- Understanding of caching with `st.cache_data`

### 2. Snowflake Account with Cortex Enabled
- Snowflake trial or paid account
- Role with access to **Cortex AI functions**

### 3. Required Python Libraries
- `streamlit`
- `snowflake-snowpark-python`
- `snowflake-ml-python`

---

## 🧠 Key Concepts Explained

### 1. Real-World AI Use Case
Instead of a generic chatbot, this app solves a **real professional problem**:
> Writing consistent, high-quality LinkedIn posts.

This demonstrates how LLMs can be embedded into **productivity tools**.

---

### 2. Cached Cortex LLM Calls
The LLM call is wrapped in a function decorated with `@st.cache_data`.

Benefits:
- Prevents repeated calls for the same prompt
- Reduces latency and compute cost
- Improves app responsiveness

Caching is especially important when generating long-form content.

---

### 3. Prompt Engineering with User Inputs
The prompt is dynamically constructed using:
- Selected **tone**
- Desired **word count**
- Provided **content URL**

The model is instructed to act as an **expert social media manager**, which helps:
- Improve output quality
- Maintain professional language
- Produce platform-appropriate content

This shows how **prompt design directly affects results**.

---

### 4. Structured and Simple UI
The app UI includes:
- A text input for the content URL
- A dropdown for tone selection
- A slider for approximate word count
- A single button to generate the post

This keeps the interface intuitive while giving users meaningful control.

---

### 5. Markdown-Based Output Rendering
The generated post is rendered using Markdown, allowing:
- Bullet points
- Clean formatting
- Readable layout suitable for LinkedIn

This makes the output immediately usable with minimal editing.

---

## 🟢 Expected Output

When the app runs:
- The user enters a URL
- Selects tone and length
- Clicks **Generate Post**
- A polished LinkedIn post appears below

This confirms:
- Cortex LLM integration works
- Prompt engineering is effective
- The app delivers real value

---

## 🛠 Troubleshooting

- Ensure Cortex access is enabled for your Snowflake role
- Verify required libraries are installed
- Remember: cached results are reused if inputs don’t change
- If output formatting looks off, adjust prompt instructions

---

## 📚 Resources

- Snowflake Cortex LLM Functions  
- Streamlit Input Widgets Documentation  
- Prompt Engineering Best Practices  

---

## 🚀 What’s Next?

With content generation mastered, upcoming days will focus on:
- Stateful AI apps
- Conversational workflows
- Tool-augmented LLMs
- Building end-to-end AI products

**Day 5 complete — you’ve built a real AI content generator! 🎉**
