# EchoMind---AI-voice-assistant
EchoMind: A real-time AI voice assistant with task automation using speech, OpenAI, and LiveKit.

---

## 🚀 Features

- 🎤 Real-time voice interaction (Speech-to-Text + Text-to-Speech)
- 🧠 AI-powered conversation using OpenAI
- 🌐 Web search support
- 🌦️ Weather information retrieval
- 📧 Send emails via Gmail
- 🔇 Noise cancellation for better audio quality
- 🤖 Custom personality (sarcastic butler style assistant)

---

## 🛠️ Tech Stack

- Python
- LiveKit Agents
- OpenAI Realtime API
---

## 📂 Project Structure

echomind/
│── agent.py # Main assistant logic
│── tools.py # Functional tools (weather, search)
│── prompts.py # Assistant personality & instructions
│── .env # Environment variables 

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/echomind.git
cd echomind
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create a `.env` file in the root directory:

```
LIVEKIT_URL=your_livekit_url
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret
OPENAI_API_KEY=your_openai_key
```

⚠️ Never upload your `.env` file to GitHub.

---

## ▶️ Run the Project

```bash
python agent.py
```

---

## 🧠 How It Works

* Uses LiveKit Realtime Model for:

  * Speech-to-Text (STT)
  * AI processing (LLM)
  * Text-to-Speech (TTS)
* OpenAI handles conversation and responses
* Integrated tools:

  * Weather updates
  * Web search
---

## 🎭 Assistant Personality

Echo is a Jarvis-inspired assistant:

* Speaks like a classy butler
* Slightly sarcastic
* Always replies in one sentence
* Acknowledges tasks before executing

### Example

```
User: What is the weather today in bengaluru?
Echo: "The weather in bengaluru today is 27 degree celcius."
```

---

## 📌 Future Improvements

* Add GUI or web interface
* Add memory for conversations
* More integrations (calendar, reminders)

---

## 👩‍💻 Author

Brunda R 
Apeksha T R
Amrutha Mahesh Hegde
RNSIT – Information Science and Engineering

---

