# 🚀 Career Trajectory Engine  
An AI-powered career recommendation system that helps users understand their **next job role**, required **skills**, and a personalized **career roadmap** based on their current experience and skills.

---

## 📌 Project Overview  
Career Trajectory Engine is a full-stack web application designed to guide users in planning their future career path.  
Users enter details such as:

- 🎓 Current Position  
- 🧠 Years of Experience  
- 🔧 Technical & Soft Skills  
- 🎯 Career Interests  

The system then generates:

- 🔮 AI-driven next job role prediction  
- 📈 Skill gap analysis  
- 🛠 Personalized learning & upskilling recommendations  
- 🗺 Career growth roadmap  
- 💼 Domain-based career paths (Tech, Product, Data, etc.)

This project is designed as a strong portfolio piece for internships and junior developer roles.

---

## ✨ Features

### 🔹 AI-Based Role Prediction  
Suggests the most likely next job title using a rules-based engine (can be extended with ML).

### 🔹 Skill Gap Analysis  
Compares user skills with industry-required skills and shows missing areas.

### 🔹 Personalized Career Roadmap  
Shows the job progression path (e.g., **Junior Developer → Developer → Senior Developer → Tech Lead**).

### 🔹 Learning Resources  
Recommended courses, platforms, and tools for upskilling.

### 🔹 Clean & Modern UI  
Built with **React + TailwindCSS** for a fast and responsive user experience.

### 🔹 FastAPI Backend  
Handles the logic, role mapping, and recommendation engine.

### 🔹 Docker Support  
Both frontend & backend can be containerized and deployed easily.

---

## 🛠 Tech Stack

### **Frontend**
- React (Vite)
- TailwindCSS
- JavaScript / JSX

### **Backend**
- Python (FastAPI)
- Pydantic
- Uvicorn

### **Tools**
- Git & GitHub
- Docker
- VS Code

---

## 📁 Project Structure

```
career-trajectory-engine/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── engine.py
│   │   ├── models.py
│   │   ├── curd.py
│   │   └── static/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   └── tailwind.config.js
│
└── docker-compose.yml
```

---

## 🚀 Getting Started

### **1. Clone the Repository**
```
git clone https://github.com/sarika4444/career-trajectory-engine.git
cd career-trajectory-engine
```

---

### **2. Backend Setup**

#### Install dependencies:
```
cd backend
pip install -r requirements.txt
```

#### Run FastAPI server:
```
uvicorn app.main:app --reload
```

Backend runs on:
```
http://127.0.0.1:8000
```

---

### **3. Frontend Setup**

```
cd frontend
npm install
npm run dev
```

Frontend runs on:
```
http://localhost:5173/
```

---

## 🐳 Docker Setup (Optional)

Run both frontend and backend using Docker:

```
docker-compose up --build
```

---

## 📚 Future Enhancements

- 🤖 Add ML model for smarter career predictions  
- 🔍 Resume parser (upload PDF → extract skills → recommend roles)  
- 📊 Dashboard with analytics  
- 🔐 User authentication  
- 🎵 Mood-based recommendations  
- 🧠 AI chatbot for career guidance (OpenAI API / local model)

---

## 🤝 Contributing

Pull requests are welcome!  
Feel free to open issues or suggest new features.

---

## 📩 Contact

**Developer:** Sarika  
**GitHub:** https://github.com/sarika4444  
**Project Link:** https://github.com/sarika4444/career-trajectory-engine

---

### ⭐ If you like this project, give it a star on GitHub!

