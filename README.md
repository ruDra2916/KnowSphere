---
title: KnowSphere – Agentic AI Research Assistant
app_file: deep_research.py
sdk: gradio
sdk_version: 5.33.1
---

# 🧠 KnowSphere – Autonomous Deep Research Assistant Using Agentic AI

**KnowSphere** is an AI-powered research assistant that uses a multi-agent system to generate deep, high-quality research reports on any topic you input. It automates the entire process—from planning, searching, and synthesizing results, to writing detailed markdown reports and emailing them to a recipient—all in a few seconds.

---

## 🚀 Project Highlights

- **Agent-based architecture** using simulated Runner, trace, and OpenAI-powered agents.
- **Multi-phase pipeline**: planning → web search → report writing → email delivery.
- Uses `gradio` for an interactive and beautifully themed UI interface.
- Custom `agents.py` enables modular and reusable agent behaviors.
- Deploy-ready on Hugging Face Spaces or local environments.

---

## 🧠 Research Pipeline Breakdown

### 1. 🔮 Planning
- The `PlannerAgent` suggests 3 search queries for a given topic.
- Powered by OpenAI models (`gpt-4o-mini`).

### 2. 🌐 Web Searching
- The `SearchAgent` simulates retrieval of real-time data and summarizes findings concisely.
- Multiple search queries are processed in parallel using `asyncio`.

### 3. 📝 Report Writing
- The `WriterAgent` converts search summaries into a structured markdown report.
- Includes follow-up questions and a short summary.

### 4. 📧 Email Delivery
- The `EmailAgent` uses the SendGrid API to send the report via email in HTML format.

---

## 🖼️ User Interface (Gradio)

| Component         | Description                              |
|------------------|------------------------------------------|
| Textbox          | Input your research topic                |
| Run Button       | Triggers the agent pipeline              |
| Markdown Output  | Displays the generated markdown report   |

Custom UI theming with:
- 🎨 Gen-Z pastel styling
- ✨ Animated trace ID log links
- 💡 Bright dark-mode-friendly output panels

---

## 🖼️ Interface Preview

<div align="center">
  <img src="images/knowsphere_ui_1.png" alt="KnowSphere UI – Input Panel" width="48%" style="margin-right: 1%;">
  <img src="images/knowsphere_ui_2.png" alt="KnowSphere UI – Report Output" width="48%">
</div>

<sub><p align="center">Fig: The left panel accepts your research query; the right panel displays the generated markdown report in a styled dark-mode UI.</p></sub>

---

## 📂 File Overview

| Filename             | Description                                            |
|----------------------|--------------------------------------------------------|
| `deep_research.py`   | Main Gradio app with styled UI and async flow          |
| `research_manager.py`| Orchestrates the full research workflow                |
| `agents.py`          | Core logic: trace, Runner, Agent, decorators (you create this) |
| `search_agent.py`    | Agent to simulate real-world search summarization       |
| `planner_agent.py`   | Agent that generates 3 query plans                      |
| `writer_agent.py`    | Agent that formats and structures report content        |
| `email_agent.py`     | Sends the generated report to the specified recipient   |

---

## 📬 Example Workflow

1. User inputs: **"Role of AI in sustainable agriculture"**
2. Agents plan relevant queries
3. Agents simulate summarizing real web search results
4. Writer agent formats a detailed markdown report
5. The report is emailed to the predefined address

---

## 🛠 Setup & Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your environment variables

Create a `.env` file with:

```env
SENDGRID_API_KEY=your-sendgrid-key
```

### 3. Run the app locally

```bash
python deep_research.py
```

### 4. Or deploy on Hugging Face:

```bash
gradio deploy
```

---

## 📌 Requirements

- Python 3.10+
- Gradio >= 4.x
- OpenAI API (for GPT agents, if extended)
- SendGrid (for email sending)

---

## 💡 Future Enhancements

- Real-time web scraping agent integration
- Dynamic topic summarization with graph plots
- Export reports as `.pdf` or `.docx`
- Voice input and TTS report playback

---

> Crafted with ❤️ by an autonomous agent crew to make research effortless.
