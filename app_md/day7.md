# 🎨 30 Days of AI — Day 7  
## Theming and Layout with Streamlit

The **#30DaysOfAI** challenge helps developers get hands-on experience building real-world AI applications using **:contentReference[oaicite:0]{index=0}** and **:contentReference[oaicite:1]{index=1}**.

On **Day 7**, we focus on **visual design and user experience**.  
Building on the functional app from Day 6, we transform it into a **polished, branded, dark-mode application** using Streamlit’s theming and layout tools.

---

## 🎯 Objective

- Enhance the Day 6 LinkedIn Post Generator
- Apply a **global dark theme** using Streamlit configuration
- Improve layout using a **clean sidebar navigation**
- Create a more **professional, production-ready UI**
- Maintain clear progress feedback for long-running AI tasks

---

## ✅ Prerequisites

Before starting Day 7, you should have:

### 1. Completed Day 1–6
- Working Streamlit application
- Snowflake connection established
- Experience calling Snowflake Cortex LLMs
- Familiarity with `st.status()` for progress feedback

### 2. Snowflake with Cortex Enabled
- Snowflake trial or paid account
- Role with access to Cortex AI functions
- Supported LLM available (e.g., Claude 3.5 Sonnet)

### 3. Local Setup
- Python 3.9+
- Required libraries:
  - `streamlit`
  - `snowflake-snowpark-python`
  - `snowflake-ml-python`

---

## 🧠 Key Concepts Explained

### 1. Global Styling with Streamlit Theming

Instead of writing custom CSS, Streamlit allows **app-wide theming** using a configuration file:

`.streamlit/config.toml`

This enables:
- Dark mode across the entire app
- Custom accent colors
- Rounded buttons and consistent spacing
- Styled sidebar separate from the main content

**Why this matters:**  
A consistent theme instantly makes your app feel **intentional, branded, and professional**, which is critical for production AI apps.

---

### 2. Dark Mode as a First-Class Feature

By setting the theme base to dark:
- The UI becomes easier on the eyes
- Contrast improves for code and AI-generated text
- The app aligns with modern developer tooling aesthetics

Dark mode is not just visual preference—it improves usability for long sessions.

---

### 3. Layout Optimization Using Sidebar

Configuration controls (tone, word count, app description) are moved into the sidebar.

**Benefits:**
- Keeps the main workspace focused on the task
- Reduces visual clutter
- Matches standard SaaS and AI tool layouts

Using `st.sidebar` allows the app to feel more like a real product than a demo.

---

### 4. Status-Based UX for Long-Running Tasks

The app uses a **status container** to guide users through the AI workflow:

- Thinking → Analyzing prompt and constraints  
- Generating → Calling Snowflake Cortex  
- Completed → Displaying final output  

**Why this is important:**
- Prevents the UI from feeling frozen
- Builds trust during LLM execution
- Makes AI behavior transparent to users

This pattern is essential for any AI app that performs blocking operations.

---

### 5. Visual Hierarchy for Output

The generated LinkedIn post is displayed inside a **bordered container**.

This:
- Clearly separates output from inputs and logs
- Makes the AI result feel like a “final deliverable”
- Improves readability and focus

Good visual hierarchy is just as important as model quality.

---

## 🟢 Expected Outcome

When the app runs, you’ll see:

- A sleek **dark-themed interface**
- Clean sidebar navigation for configuration
- Real-time progress updates during AI execution
- Final LinkedIn post displayed in a bordered output card

This confirms:
- Streamlit theming is correctly applied
- Layout improvements enhance usability
- The app is moving toward production quality

---

## 📚 Resources

- Streamlit Theming Guide  
- `config.toml` Configuration Documentation  
- Streamlit Sidebar API  
- Material Icons in Streamlit  

---

## 🚀 What’s Next?

With theming and layout complete, upcoming days will focus on:
- Multi-step AI workflows
- Conversational memory
- Tool-using AI agents
- End-to-end production AI UX patterns

**Day 7 complete — your AI app now looks as good as it works! 🎉**
