# 📝 Text Summarization using Fine-Tuned T5 Transformer

An end-to-end Natural Language Processing (NLP) application that automatically generates concise summaries from long text using a fine-tuned T5 Transformer model. The project covers the complete machine learning lifecycle—from dataset preprocessing and model training to deployment with FastAPI and a responsive web interface.

# 🚀 Project Highlights

- ✅ Built and fine-tuned a Transformer-based T5 model for abstractive text summarization.
- ✅ Trained the model on the SAMSum dialogue summarization dataset.
- ✅ Evaluated training performance and selected the best-performing epoch based on validation           results.
- ✅ Saved the trained model and tokenizer for inference.
- ✅ Deployed the trained model as a production-ready inference service using FastAPI.
- ✅ Developed a clean, interactive web interface using HTML, CSS, and JavaScript.
- ✅ Implemented efficient preprocessing, tokenization, and summary generation pipeline.
- ✅ Designed RESTful API endpoints for seamless frontend-backend communication.

---


# ✨ Features

- 📄 Generate concise summaries from lengthy text.
- 🤖 Uses a custom fine-tuned Transformer model instead of relying on third-party hosted summarization APIs.
- ⚡ Fast inference using FastAPI.
- 🎯 High-quality abstractive summarization.
- 💻 Responsive web interface.
- 🔄 Real-time summarization.

---

# 🏗️ System Architecture

```text
Dataset (SAMSum)
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Tokenization
        │
        ▼
Fine-tuning T5 Transformer
        │
        ▼
Model Evaluation
        │
        ▼
Best Epoch Selection
        │
        ▼
Saved Model (.bin + tokenizer)
        │
        ▼
FastAPI Backend
        │
        ▼
REST API
        │
        ▼
HTML | CSS | JavaScript UI
```

---

# 🛠 Tech Stack

## Machine Learning

- Python
- Hugging Face Transformers
- T5 Transformer
- PyTorch

## Backend
- FastAPI
- Pydantic

## Frontend
- HTML5
- CSS3
- JavaScript

## Dataset

- SAMSum Dialogue Summarization Dataset

# 📂 Project Workflow

## 1. Data Collection

- Loaded the SAMSum dataset.
## 2. Data Preprocessing

- Removed HTML tags.
- Removed extra spaces.
- Normalized text.
- Tokenized input and summaries.
## 3. Model Training

- Fine-tuned the pretrained T5 Transformer.
- Monitored training and validation loss.
- Selected the best-performing epoch.
## 4. Model Saving

- Saved the trained model and tokenizer for deployment.
## 5. Model Deployment

- Loaded the saved model inside FastAPI.
- Exposed REST API endpoints.
- Connected backend with frontend.

---

# 🌐 API Endpoints

## Home
GET /

Returns the web interface.

### Summarize Text
POST /summarize

### Input

{
  "dialogue":"Your long text..."
}

### Output

{
   "summary":"Generated concise summary."
}


# 📁 Project Structure

```text
Text-Summarization/
│
├── Dataset/
│     └── samsum-train.csv
│
├── saved_summary_model/
│
├── templates/
│     └── index.html
│
├── static/
│     └── style.css
│
├── app.py
├── requirements.txt
├── README.md
└── Text_Summarization.ipynb
```

---


# 🎯 Key Skills Demonstrated

- Deep Learning
- Natural Language Processing (NLP)
- Transformer Models
- T5 Architecture
- Hugging Face Transformers
- PyTorch
- Model Fine-tuning
- Model Evaluation
- Text Preprocessing
- Tokenization
- FastAPI
- REST API Development
- HTML
- CSS
- JavaScript
- Model Deployment

---

# 🔮 Future Enhancements

- PDF Summarization
- Multi-document Summarization
- Batch Processing
- Speech-to-Text Summarization
- Multilingual Summarization
- User Authentication
- Docker Deployment
- Cloud Deployment (AWS/Azure/GCP)

---

# 👩‍💻 Author

**Anusha R**

**Aspiring AI/ML Engineer | Python Developer | NLP Enthusiast**

**GitHub:
https://github.com/anusharajanna027-git-in**

---
## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub.
