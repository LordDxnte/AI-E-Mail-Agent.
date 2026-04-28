# 🚀 Umais Jafry | Portfolio & AI Email Agent

This repository houses my custom-built AI Email Automation Agent.

## 📁 Project Structure

- **`/ai-email-agent`**: Python-based AI Agent that summarizes Gmail threads and sends daily briefs to Discord.

---

## 🤖 AI Email Agent (Backend)

The Email Agent is a Python script designed to solve "inbox fatigue." It connects to the Gmail API, fetches the latest unread emails, uses LLMs to summarize them, and pushes a clean digest to a Discord channel via Webhooks.

### 🛠️ Tech Stack
- **Language:** Python 3.12
- **APIs:** Gmail API, OpenAI/Gemini API (LLM)
- **Notifications:** Discord Webhooks
- **Environment:** Managed via `python-dotenv` for security.

### 🚀 Setup & Usage
1. Navigate to the agent directory:
   ```bash
   cd ai-email-agent
