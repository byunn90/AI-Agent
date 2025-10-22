# 🧠 AI-Agent

An experimental AI-powered command-line agent built with Python and Google's **Gemini API**, following the Boot.dev *Build an AI Agent* course.  
This tool interacts with an LLM to perform local tasks such as reading files, listing directories, creating files with strict guidelines, and executing commands — while keeping strict security guardrails.

---

## 🚀 Features

- **Gemini API Integration** – Uses Google’s `google-genai` client to generate intelligent responses.
- **.env Configuration** – Loads your Gemini API key securely via environment variables.
- **Command-Line Prompts** – Accepts dynamic user input:
  ```bash
  uv run main.py "Why is Boot.dev great for backend learning?"
