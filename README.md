# 🤖 Rule-Based AI Chatbot

A simple **rule-based AI chatbot** with a modern web UI, powered by a **Flask backend**.  
The chatbot responds to predefined user inputs using dictionary-based logic (no machine learning).

---

## 🌐 Live Demo

🔗 https://rule-based-ai-chatbot-decodelabs.onrender.com/

> ⚠️ Note: This app is hosted on Render (free tier). It may take a few seconds to load after inactivity.

---

## 🚀 Features

- 💬 Interactive chatbot UI
- 🌗 Dark / Light theme (stored in browser)
- 🔁 Continuous chat interaction
- 🧠 Rule-based responses (dictionary lookup)
- 🧹 Input preprocessing (lowercase + trim)
- ❓ Fallback response for unknown inputs
- ⛔ Exit command to end session
- 🔌 Flask API (`POST /api/chat`)
- 📱 Responsive design

---

## 🛠️ Technologies Used

- Python (Flask)
- HTML5
- CSS3
- JavaScript
- Gunicorn (for deployment)

---

## ⚙️ How It Works

The chatbot follows the **Input → Process → Output (IPO)** model:

1. **Input**  
   User sends a message from the UI.

2. **Processing**  
   - Input is cleaned (`lowercase + trim`)
   - Checked against predefined responses (dictionary)

3. **Output**  
   - Matching response is returned via Flask API
   - If no match → fallback message

---
## 📂 Project Structure


.
├── app.py # Flask backend and chatbot logic
├── index.html # Frontend UI
├── requirements.txt # Dependencies (flask, gunicorn)
├── README.md


---

## 🧪 API Endpoint

### `POST /api/chat`

🎯Learning Outcomes

This project helps to understand:

Rule-based AI systems
Control flow and decision making
Client-server communication (Frontend ↔ Backend)
REST API basics
UI/UX design for chat applications

📌 Conclusion

This project demonstrates the foundation of AI systems using rule-based logic and Flask-based API integration.
It serves as a stepping stone for building more advanced intelligent applications.


