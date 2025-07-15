# 🧠 Gemini-Powered Linux SSH Dashboard

A beautiful, secure, and AI-powered web interface built with **Streamlit** for executing remote **Linux commands over SSH**. It supports **50+ categorized commands** and integrates **Google Gemini AI** to convert natural language into shell commands.

---

## 🚀 Features

### 🔐 Secure SSH Remote Execution  
- Execute Linux commands on any remote server over SSH.

### 📂 50+ Built-in Commands  
Organized into intuitive categories:
- 🖥️ System Info  
- 📁 File & Directory  
- 🔍 Processes & Logs  
- 🌐 Network  
- 📦 Package Management  
- 👤 User & Permissions  
- 🔧 Services & Firewall  
- 🧩 Miscellaneous

### 💡 Gemini AI Command Generator  
- Describe your task in simple English and let Gemini suggest the correct Linux command.

### 🧾 Command History Logging  
- Export executed commands and their results to a `.txt` file.

### 🎨 Elegant UI  
- Gradient background  
- Responsive layout  
- Sidebar-based SSH authentication

---

## 📦 Installation

1. **Clone the Repository**
```bash
git clone https://github.com/Pradeeprawat-01/linux-ssh-dashboard.git
cd linux-ssh-dashboard
```

2. **Install Dependencies**
```bash
pip install streamlit google-generativeai
```

3. **Set Gemini API Key**

#### Option 1: Hardcode in script
```python
GEMINI_API_KEY = "your_api_key_here"
```

#### Option 2: Use Environment Variable
```bash
export GEMINI_API_KEY="your_api_key_here"
```
And in your code:
```python
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
```

---

## 🧑‍💻 Usage

Run the dashboard:
```bash
streamlit run app2.py
```

### 💡 Steps:
1. Enter SSH credentials in the sidebar.
2. Choose a category and a command.
3. Hit **Run Command**.
4. Or enter a plain English prompt, and let Gemini suggest & execute a command.
5. Click **Export** to save your session history.



---

## ✅ Requirements
- Python 3.8+
- Internet access for Gemini API
- SSH access to the target machine
- Gemini API Key

---

## 🛡️ Security Notes
- SSH credentials are never stored.
- Gemini only generates safe, single-line commands.
- Command logs are saved only on user export.

---

## 📁 Project Structure

```bash
linux-ssh-dashboard/
├── app2.py             # Main Streamlit app
├── README.md

```

---

## 🧠 Powered By
- [Streamlit](https://streamlit.io/)
- [Google Gemini API](https://ai.google.dev/)
- [OpenSSH](https://www.openssh.com/)

---

## 🙌 Author
**Pradeep Singh Rawat**  
 Cloud & DevOps Enthusiast  
🔗 [LinkedIn](https://www.linkedin.com/in/pradeep-singh-rawat-9707ard)  
🔗 [GitHub](https://github.com/Pradeeprawat-01)

---

## 📄 License
MIT License — Free to use and modify with attribution.

---

> ⭐ Don’t forget to **star** the repo if you like it!
