# 🎨 30 Days of AI — Day 14  
## Adding Avatars and Error Handling

The **#30DaysOfAI** challenge helps you build real-world AI applications using **Streamlit**.

On **Day 14**, we transform our chatbot from functional → production-ready by adding:

- 🎭 Customizable avatars  
- ⚙️ System prompt customization  
- 🛡️ Robust error handling  
- 🧪 Debug mode for testing failures  
- 📊 Conversation statistics  

This is where UX polish meets production reliability.

---

## 🎯 Objective

- Allow users to customize chat avatars
- Handle LLM/API failures gracefully
- Prevent app crashes during errors
- Maintain clean conversation history
- Deliver a professional chatbot experience

---

## ✅ Prerequisites

Before starting Day 14, you should understand:

### 1️⃣ Streamlit Fundamentals
- `st.session_state`
- `st.sidebar`
- `st.chat_message`
- `st.chat_input`
- App rerun behavior

### 2️⃣ Stateful Chatbot (Days 8–11)
- Storing chat messages as a list of dictionaries
- Rendering messages dynamically
- Passing full conversation history to the LLM

### 3️⃣ Streaming Responses (Day 12)
- Custom generator functions
- `st.write_stream`
- Spinner feedback during generation

### 4️⃣ System Prompt Customization (Day 13)
- Using a configurable system instruction
- Injecting it into the final LLM prompt

---

# 🆕 What’s New in Day 14

Day 14 keeps everything from previous days and introduces **visual polish + reliability**.

---

## 🎭 1. Avatar Customization

Users can now personalize:

- Their own avatar (emoji)
- The assistant avatar (emoji)

### Why This Matters

- Makes the chatbot feel more interactive
- Adds personality to the interface
- Improves user engagement
- Demonstrates how UI state can be controlled dynamically

The avatar is selected in the sidebar and passed into:

`st.chat_message(role, avatar=selected_avatar)`


The avatar dynamically changes based on the message role (`user` vs `assistant`).

---

## ⚙️ 2. System Prompt Configuration

The sidebar includes a text area where users can define:

> “How the AI should behave”

This system instruction is injected before the conversation history when constructing the final prompt.

### Why This Matters

- Enables personality control
- Makes the assistant adaptable
- Mimics production AI applications

---

## 🧪 3. Debug Mode (Simulated Errors)

A checkbox in the sidebar allows you to:

- Simulate an API failure
- Trigger a test exception
- Validate your error handling logic

### Why This Is Powerful

In real-world deployments, APIs will fail.

Common reasons:
- Rate limits (429 errors)
- Network issues
- Model overload
- Safety filter triggers

Instead of waiting for a real failure, debug mode lets you test error handling instantly.

---

## 🛡️ 4. Error Handling with Try/Except

The entire streaming + LLM call process is wrapped inside a `try/except` block.

### If everything works:
- Response streams normally
- Message is added to chat history
- Sidebar metrics update

### If something fails:
- A red error message is shown
- A helpful tip is displayed
- The app continues running
- No broken messages are saved

This ensures:

- The app does NOT crash
- Users stay informed
- Conversation history remains clean

---

## 💬 5. Streaming with Protection

Day 14 continues using:

- Custom generator function
- Word-by-word streaming
- Spinner during processing

But now it’s protected by error handling.

This combination creates:

- Smooth UX
- Real-time feedback
- Safe execution

---

## 📊 6. Conversation Stats + Clear History

The sidebar displays:

- Total user messages
- Total AI responses

A **Clear History** button:
- Resets chat to the welcome message
- Forces a rerun
- Keeps UX consistent

This mimics real AI chat platforms.

---

# 🧠 Why Error Handling Is Critical

In production environments:

> LLM APIs WILL fail eventually.

Apps without error handling:
- Crash
- Lose state
- Frustrate users
- Look unprofessional

Day 14 introduces a **production-safe pattern**:

- Wrap risky logic in `try/except`
- Show meaningful error messages
- Guide the user
- Never store failed responses

This is a required pattern for:
- SaaS AI apps
- Enterprise deployments
- Client-facing tools
- Hackathon-ready demos

---

# 🧪 Try It Out

1. Enable **Simulate API Error** in the sidebar
2. Send a message
3. Observe:
   - Red error message
   - Helpful guidance
   - App does not crash
4. Disable debug mode
5. Test normal flow again

This demonstrates true production readiness.

---

# 🚀 What You’ve Built So Far

By Day 14, your chatbot now includes:

- Stateful memory  
- Full conversation context  
- Streaming responses  
- System prompt customization  
- Avatar personalization  
- Conversation analytics  
- Clear history functionality  
- Production-grade error handling  

This is no longer a demo chatbot.

This is a **deployable AI application foundation**.

---

# 🔜 What’s Next?

Upcoming improvements could include:

- Token-efficient memory management  
- RAG integration  
- Tool-using agents  
- Multi-model switching  
- Authentication layers  
- Deployment strategies  

You’re now building at production level. 🎯

---

# 📚 Key Concepts Used

- Streamlit Chat UI  
- Session State  
- Sidebar configuration  
- Streaming generators  
- Python exception handling  
- Safe LLM integration  

---

**Day 14 Complete — Visual polish + reliability unlocked. 🎉**
