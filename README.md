# 📝 Text Summarization using Fine-Tuned T5 Transformer

An end-to-end Natural Language Processing (NLP) application that automatically generates concise summaries from long text using a fine-tuned T5 Transformer model. The project covers the complete machine learning lifecycle—from dataset preprocessing and model training to deployment with FastAPI and a responsive web interface.


# Builded a complete AI lifecycle:

- 📊 Prepared and preprocessed the dataset.
- 🤖 Fine-tuned a Transformer model.
- 💾 Saved the trained model.
- ☁️ Published the model on Hugging Face Hub.
- 🌐 Built a Flask inference application.
- 🚀 Deployed the application on Render.
- 📦 Used Git LFS and proper repository management for large model files.

## 🤗 Fine-Tuned Model

This project uses a fine-tuned **T5 Transformer** model hosted on Hugging Face Hub.

🔗 **Model Repository:**  
https://huggingface.co/anusharajanna/fine-tuned-t5-summarizer

The application automatically downloads the model from Hugging Face during startup, eliminating the need to store large model files in the GitHub repository.


# 🚀 Project Highlights

- ✅ Fine-tuned the T5 Transformer model for abstractive text summarization using the SAMSum dataset.
- ✅ Preprocessed and tokenized conversational text to prepare high-quality training data.
- ✅ Trained and evaluated the model using the Hugging Face Transformers library and PyTorch.
- ✅ Saved the trained model and tokenizer using the save_pretrained() API for reproducible inference.
- ✅ Hosted the fine-tuned model on Hugging Face Hub to separate model storage from application code.
- ✅ Developed a Flask-based web application with a clean user interface for real-time text summarization.
- ✅ Configured the application to automatically download the model from Hugging Face during startup, eliminating the need to store large model files in the GitHub repository.
- ✅ Deployed the application on Render with a production-style architecture using GitHub for source code and Hugging Face for model hosting.
- ✅ Optimized the project structure using Git LFS, .gitignore, and model hosting best practices to keep the repository lightweight and deployment-friendly.
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
- Hugging Face Hub
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

# Project Flow

                           ┌──────────────────────┐
                           │   SAMSum Dataset     │
                           └──────────┬───────────┘
                                      │
                                      ▼
                        ┌─────────────────────────┐
                        │ Data Preprocessing      │
                        │ • Clean text            │
                        │ • Tokenization          │
                        │ • Train/Test Split      │
                        └──────────┬──────────────┘
                                   │
                                   ▼
                     ┌────────────────────────────┐
                     │ Fine-Tune T5 Transformer   │
                     │ • Hugging Face             │
                     │ • PyTorch                  │
                     └──────────┬─────────────────┘
                                │
                                ▼
                  ┌──────────────────────────────┐
                  │ Model Evaluation             │
                  │ • Generate Summaries         │
                  │ • Validate Performance       │
                  └──────────┬───────────────────┘
                             │
                             ▼
               ┌──────────────────────────────────┐
               │ Save Model & Tokenizer           │
               │ save_pretrained()                │
               └──────────┬───────────────────────┘
                          │
                          ▼
            ┌─────────────────────────────────────┐
            │ Upload Model to Hugging Face Hub    │
            │ • config.json                       │
            │ • model.safetensors                 │
            │ • tokenizer files                   │
            └──────────┬──────────────────────────┘
                       │
                       ▼
          ┌────────────────────────────────────────┐
          │ Flask Web Application                  │
          │ • User enters text                     │
          │ • Loads model from Hugging Face Hub    │
          │ • Generates summary                    │
          └──────────┬─────────────────────────────┘
                     │
                     ▼
          ┌────────────────────────────────────────┐
          │ Deploy on Render                       │
          │ • GitHub (Application Code)            │
          │ • Hugging Face (Model Storage)         │
          └──────────┬─────────────────────────────┘
                     │
                     ▼
          ┌────────────────────────────────────────┐
          │ End User                              │
          │ Receives AI-generated Summary         │
          └────────────────────────────────────────┘


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
