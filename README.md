# 🤖 DynamoAI (Jarvis_AI)

DynamoAI is a personal AI assistant inspired by **Jarvis**, capable of executing commands, automating tasks, interacting through a web-based UI, managing data, and providing intelligent responses.  
The project combines a **Python backend** with a **browser-based frontend**, making it lightweight, modular, and cross-platform.
Note: It's not at all a Website, it's Desktop App which is consist of web-based UI.

---

## ✨ Features

- 🎙️ Voice-based AI assistant
- 🧠 Command parsing and intelligent task execution
- 🌐 Web-based user interface
- 🗄️ SQLite database for persistent storage
- 🔊 Audio feedback on startup
- 📇 Contact management
- ⚙️ Modular and extensible architecture
- 🖥️ Works on **Windows, Linux, and macOS**

---

## 🧩 Tech Stack

**Backend**
- Python 3.x
- SQLite
- Modular engine-based architecture

**Frontend**
- HTML5
- CSS3
- JavaScript
- Audio & asset management

---

## 📂 Project Structure

```

DynamoAI/
│
├── engine/
│   ├── command.py        # Command parsing & execution
│   ├── config.py         # Configuration & constants
│   ├── cookies.json      # Stored session cookies
│   ├── db.py             # Database operations
│   ├── features.py       # Core assistant features
│   ├── helper.py         # Utility/helper functions
│   └── envdynamo         # Environment configuration
│
├── www/
│   ├── assets/
│   │   ├── audio/
│   │   │   └── start_sound.mp3
│   │   ├── img/
│   │   └── vendors/
│   │
│   ├── cdns.txt
│   ├── controller.js
│   ├── index.html
│   ├── main.js
│   ├── script.js
│   └── styles.css
│
├── contacts.csv          # Contacts data
├── dynamo.db             # SQLite database
├── device.bat            # Windows launcher
├── main.py               # Main entry point
├── run.py                # Alternate runner
├── .gitignore
└── README.md

````

---

## 🚀 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/om-thakur1504/Jarvis_AI.git
cd Jarvis_AI
````

---

## 🧪 Environment Setup

### 🔹 Python Version

Ensure **Python 3.8 or higher** is installed.

Check version:

```bash
python --version
```

---

## 📦 Install Dependencies

> Install dependencies using `requirements.txt` (recommended)

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### 🪟 Windows

**Option 1: Using Python**

```bash
python main.py
```

**Option 2: Using Batch File**

```bash
device.bat
```

---

### 🐧 Linux

```bash
python3 main.py
```

If needed:

```bash
chmod +x main.py
```

---

### 🍎 macOS

```bash
python3 main.py
```

> If `python3` is not found, install via Homebrew:

```bash
brew install python
```

---

## 🗄️ Database

* Uses **SQLite**
* Database file: `dynamo.db`
* Managed via `engine/db.py`

---

## 🧠 Customization

* Add new commands in `engine/command.py`
* Extend assistant abilities in `engine/features.py`
* Modify UI in `www/`
* Update configuration via `engine/config.py`

---

## 🔐 Security Notes

* Do not expose cookies or API keys publicly
* Use `.gitignore` for sensitive files
* Avoid committing `cookies.json` with real sessions

---

## 🛠️ Troubleshooting

* Ensure microphone permissions are enabled
* Check Python path if command fails
* Verify all dependencies are installed correctly

---

## 📌 Future Enhancements

* Hotword detection
* Face recognition authentication
* Mobile automation integration
* Cloud-based AI processing
* Multi-language support

---

## 👨‍💻 Author

**Om Thakur**
GitHub: [om-thakur1504](https://github.com/om-thakur1504)

---

## 📜 License

This project is licensed under the **MIT License**.
