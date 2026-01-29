# Jarvis_AI 🤖

Jarvis_AI is a Python-based **AI voice assistant** designed to perform daily tasks through **voice commands**. It uses speech recognition and text-to-speech technologies to interact with users and automate system operations, web searches, and information retrieval.

---

## 📌 Project Overview

This project aims to build a desktop voice assistant similar to *Jarvis*, capable of understanding user commands and executing predefined actions. It enhances productivity by enabling hands-free interaction with the system.

---

## ✨ Features

- Voice-based user interaction  
- Speech recognition (Speech-to-Text)  
- Text-to-speech responses  
- System automation (open applications, files, folders)  
- Web search and information retrieval  
- Weather and basic utility commands  
- Modular and easily extendable architecture  

---

## 🛠️ Technologies Used

- **Python**
- SpeechRecognition
- pyttsx3 (Text-to-Speech)
- OS & System libraries
- Web scraping libraries (if enabled)

---

## 📂 Project Structure

```
Jarvis_AI/
│
├── __pycache__/                 # Python cache files
│
├── .vscode/                     # VS Code workspace settings
│
├── engine/
│   ├── __pycache__/             # Engine module cache
│   ├── command.py               # Command parsing & execution logic
│   ├── config.py                # Configuration settings & constants
│   ├── cookies.json             # Stored cookies (web/session handling)
│   ├── db.py                    # Database operations & helpers
│   ├── features.py              # Core assistant features & actions
│   ├── helper.py                # Utility/helper functions
│   └── envdynamo                # Environment/config related file
│
├── www/
│   ├── assets/
│   │   ├── audio/
│   │   │   └── start_sound.mp3  # Startup sound for the assistant
│   │   ├── img/                 # Images/icons used in UI
│   │   └── vendors/             # Third-party frontend libraries
│   │
│   ├── cdns.txt                 # CDN references for frontend assets
│   ├── controller.js            # Frontend logic controller
│   ├── index.html               # Web UI entry point
│   ├── main.js                  # Main frontend JavaScript logic
│   ├── script.js                # Supporting JS functions
│   └── styles.css               # UI styling (CSS)
│
├── .gitignore                   # Git ignored files/folders
├── contacts.csv                 # Stored contacts data
├── device.bat                   # Windows batch file to start the assistant
├── dynamo.db                    # SQLite database file
├── main.py                      # Main application entry point
├── run.py                       # Alternate runner / development launcher
└── README.md                    # Project documentation (you’re writing this)
````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/om-thakur1504/Jarvis_AI.git
cd Jarvis_AI
````

### 2️⃣ Install Dependencies

Ensure **Python 3.7 or higher** is installed.

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Assistant

```bash
python main.py
```

or

```bash
python run.py
```

---

## 🎙️ Usage

After starting the program, the assistant listens for voice commands.

Example commands:

* “Open Chrome”
* “What is the time?”
* “Search Python tutorials”
* “Tell me the weather”

You can customize or add new commands by modifying the core logic inside the `engine` directory.

---

## 🔧 Customization

* Add new commands in the command handler module
* Integrate APIs for advanced features (news, weather, AI models)
* Improve NLP logic for better intent recognition

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute this project.

---

## 👨‍💻 Author

**Om Thakur**
GitHub: [@om-thakur1504](https://github.com/om-thakur1504)

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
