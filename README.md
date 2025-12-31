# Anuvaad – Multilingual Chatbot Backend
# Live Website
https://sakshi241712.github.io/Multilingual-Chatbot-Using-GenAI/
Backend services for a multilingual chatbot using Generative AI, designed to support Indian regional languages through a translation and LLM-based pipeline.

Project Overview

This repository contains the backend implementation of the Multilingual Chatbot Using Generative AI project.
The backend processes user messages, translates Indian regional languages into English, generates AI-powered responses using a Large Language Model (LLM), and translates the response back into the user’s language.

The backend communicates with the frontend chatbot (Chatling) using REST APIs.

Features

REST API for chatbot interaction

Automatic language detection

Translation pipeline (Indian language ↔ English)

Generative AI–based responses

Prompt engineering for controlled AI output

CORS-enabled backend for frontend integration

Backend Workflow
User Message
   ↓
Language Detection
   ↓
Translate to English
   ↓
Prompt Engineering
   ↓
LLM Response
   ↓
Translate to User Language
   ↓
Final Reply

Technologies Used

Python

Flask

Flask-CORS

Generative AI (LLM)

Translation APIs / Language Models

Git & GitHub

Folder Structure
anuvaad-backend/
│
├── app.py              # Flask application entry point
├── translation.py      # Language translation logic
├── prompt.py           # Prompt templates and rules
├── llm.py              # LLM integration
├── requirements.txt    # Project dependencies
├── .gitignore
└── README.md

API Endpoint
POST /chat

Request

{
  "message": "नमस्ते"
}


Response

{
  "reply": "नमस्ते! मैं आपकी कैसे सहायता कर सकता हूँ?",
  "detected_language": "hi"
}
