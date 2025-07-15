import os
import streamlit as st
import subprocess
import datetime
import google.generativeai as genai

# ===================== CONFIG =====================
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"  # 🔐 Replace with your Gemini API key
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ===================== PAGE STYLE =====================
st.set_page_config(page_title="Linux SSH Dashboard", layout="centered")
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
    }
    .main > div {
        background: linear-gradient(to bottom right, #eef2f3, #8e9eab);
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    .stSelectbox > div > div, .stTextInput > div > div input {
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Gemini-Powered Linux SSH Dashboard")
st.markdown("---")

# ===================== SIDEBAR =====================
st.sidebar.title("🔐 SSH Connection")
username = st.sidebar.text_input("👤 Username", key="username")
ip = st.sidebar.text_input("🌐 Server IP", key="ip")

if "command_log" not in st.session_state:
    st.session_state.command_log = []

# ===================== GEMINI AI HELPER =====================
def get_linux_command(prompt):
    query = f"You are a Linux expert. Convert this to a single safe Linux command only: '{prompt}'"
    response = model.generate_content(query)
    return response.text.strip()

# ===================== CATEGORIZED COMMANDS =====================
commands = {
    "System Info": {
        "📅 Show Date": "date",
        "🧠 Memory Usage": "free -h",
        "💽 Disk Usage": "df -h",
        "🧮 CPU Info": "lscpu",
        "⏱️ Uptime": "uptime",
        "🐧 Kernel Version": "uname -r",
        "🧾 OS Info": "cat /etc/os-release",
        "👥 Logged In Users": "who",
        "🖥️ Hostname": "hostname",
        "🧰 System Architecture": "uname -m"
    },
    "File & Directory": {
        "📁 List Files": "ls",
        "📂 Present Working Directory": "pwd",
        "📦 Create Directory": "mkdir testdir",
        "🗑️ Remove Directory": "rmdir testdir",
        "📄 Create File": "touch testfile.txt",
        "🧹 Remove File": "rm testfile.txt",
        "📤 Copy File": "cp testfile.txt copy.txt",
        "📥 Move File": "mv copy.txt moved.txt",
        "📖 View File Content": "cat testfile.txt",
        "🔎 Find File by Name": "find / -name testfile.txt"
    },
    "Processes & Logs": {
        "🔍 Running Processes": "ps aux",
        "📊 Top Processes": "top -b -n 1",
        "📜 System Logs": "journalctl -xe",
        "🔁 Process Tree": "pstree",
        "🚀 Background Jobs": "jobs"
    },
    "Network": {
        "🌐 IP Address": "ip a",
        "📡 IP Route": "ip r",
        "🔒 Open Ports": "ss -tuln",
        "📥 Download File": "wget https://example.com",
        "📤 Upload File (scp)": "scp testfile.txt user@ip:/path"
    },
    "Package Management": {
        "🌳 Install Package": "sudo dnf install -y tree",
        "🗑️ Remove Package": "sudo dnf remove -y tree",
        "🔁 System Update": "sudo dnf update -y",
        "🔍 Search Package": "dnf search tree",
        "📦 List Installed Packages": "dnf list installed"
    },
    "User & Permissions": {
        "➕ Add User": "sudo adduser newuser",
        "➖ Delete User": "sudo deluser newuser",
        "🔐 File Permissions": "chmod 755 testfile.txt",
        "👤 File Ownership": "chown user:user testfile.txt",
        "🔄 Switch User": "su - newuser"
    },
    "Services & Firewall": {
        "▶️ Start SSHD": "sudo systemctl start sshd",
        "⏹️ Stop SSHD": "sudo systemctl stop sshd",
        "🔁 Restart SSHD": "sudo systemctl restart sshd",
        "📶 SSHD Status": "systemctl status sshd",
        "🛡️ Firewall Status": "sudo systemctl status firewalld",
        "🔥 Start Firewall": "sudo systemctl start firewalld",
        "🚫 Stop Firewall": "sudo systemctl stop firewalld",
        "🔐 SELinux Status": "sestatus",
        "🚨 Enable Service": "sudo systemctl enable sshd",
        "🚫 Disable Service": "sudo systemctl disable sshd"
    },
    "Miscellaneous": {
        "📅 Show Calendar": "cal",
        "🧬 Environment Variables": "printenv",
        "⏰ View Crontab": "crontab -l",
        "📝 Edit Crontab": "crontab -e",
        "📦 Mount FS": "mount /dev/sr0 /mnt",
        "📤 Unmount FS": "umount /mnt",
        "💾 Disk Partitions": "lsblk",
        "🧾 Show Aliases": "alias",
        "🔧 System Reboot": "sudo reboot",
        "🔒 Shutdown System": "sudo shutdown now"
    }
}

# ===================== COMMAND UI =====================
st.subheader("📂 Select Command Category")
category = st.selectbox("Category", list(commands.keys()))
st.subheader("📌 Select Command")
selected_cmd_label = st.selectbox("Command", list(commands[category].keys()))

if st.button("🚀 Run Command"):
    if username and ip:
        cmd = commands[category][selected_cmd_label]
        ssh_cmd = f'ssh {username}@{ip} "{cmd}"'
        st.info(f"Running: `{cmd}` on `{ip}`...")
        try:
            output = subprocess.getoutput(ssh_cmd)
            st.session_state.command_log.append((cmd, output))
            st.success("✅ Command executed successfully!")
            st.code(output, language="bash")
        except Exception as e:
            st.error(f"❌ Execution Failed: {e}")
    else:
        st.warning("⚠️ Please enter valid SSH credentials in the sidebar.")

# ===================== GEMINI COMMAND =====================
st.markdown("---")
st.subheader("💡 Generate Command with Gemini")
prompt = st.text_input("Describe your task in simple English:")
if st.button("🔮 Generate Command"):
    if prompt:
        ai_command = get_linux_command(prompt)
        st.success(f"Command from Gemini: `{ai_command}`")
        if st.button("🚀 Execute Gemini Command"):
            if username and ip:
                full_cmd = f"ssh {username}@{ip} \"{ai_command}\""
                output = subprocess.getoutput(full_cmd)
                st.session_state.command_log.append((ai_command, output))
                st.code(output)
            else:
                st.warning("Enter SSH credentials in sidebar.")

# ===================== COMMAND HISTORY =====================
if st.sidebar.button("📥 Export Command History"):
    filename = f"command_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        for cmd, result in st.session_state.command_log:
            f.write(f"$ {cmd}\n{result}\n{'-'*50}\n")
    st.sidebar.success(f"History saved as {filename}")
