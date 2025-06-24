# 📦 Amharic E-Commerce Data Extractor

This project is part of the 10 Academy Week 4 challenge. It builds an end-to-end pipeline to:

1. Scrape Amharic Telegram e-commerce messages 📩
2. Label entities (Product, Price, Location) for NER 📌
3. Fine-tune a multilingual transformer for Amharic NER 🧠
4. Score vendors based on business activity and engagement 📊

---

## 📁 Project Structure

│B5W4
├── data/
│ └── labeled/
│ └── labeled.conll # Labeled data in CoNLL format
│
├── notebooks/
│ ├── preprocessed.ipynb # Data preprocessing steps
│ └── run_training.ipynb # Fine-tuning the NER model
│
├── src/
│ ├── data_loader.py # Load data into proper format
│ ├── main.py # Main pipeline runner
│ ├── model.py # Model loading and architecture
│ ├── preprocessing.py # Text cleaning and preprocessing
│ ├── tg_scraper.py # Telegram scraper using Telethon
│ ├── tokenizer.py # Tokenizer setup for multilingual model
│ ├── trainer.py # Model training logic
│ └── utils.py # Utility functions (label mappings, metrics, etc.)
│
├── .env # Telegram API keys and config (not tracked)
├── .gitignore # Ignore notebooks checkpoints, data, .env
├── README.md # Project documentation (this file)
└── requirements.txt # Python dependencies
