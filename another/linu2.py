import streamlit as st
import subprocess

# ----- Page Configuration -----
st.set_page_config(page_title="Linux SSH Dashboard", layout="wide")
st.markdown("""
    <style>
        /* ==== ATTRACTIVE GRADIENT BACKGROUND ==== */
        .stApp {
            background: linear-gradient(135deg, #74ebd5 0%, #acb6e5 100%);
            min-height: 100vh;
            background-attachment: fixed;
        }
        .main .block-container {
            background-color: rgba(255,255,255,0.82);
            border-radius: 14px;
            box-shadow: 0 8px 24px 0 rgba(31,119,180,0.08);
            padding: 2.5em 2em;
            margin-top: 1.5em;
        }
        .sidebar .sidebar-content {
            background: #f1f7fa;
            border-radius: 6px;
            padding: 1em 0.5em;
        }
        .title {
            text-align: center;
            font-size: 2.5em;
            color: #1f77b4;
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            font-size: 12px;
            color: gray;
            margin-top: 30px;
        }
        .command-box {
            background-color: #ffffff;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ----- Header -----
st.markdown("<div class='title'>💻 Remote Linux Command Dashboard</div>", unsafe_allow_html=True)

# ----- Sidebar for SSH credentials -----
with st.sidebar:
    st.title("🔐 SSH Credentials")
    username = st.text_input("👤 Username", placeholder="e.g., root")
    ip = st.text_input("🌐 IP Address", placeholder="e.g., 192.168.1.100")

# ----- Command Categories -----
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

# ----- Command Panel -----
st.markdown("---")
st.markdown("### 🧰 Command Center")

for category, cmds in commands.items():
    with st.expander(f"📂 {category}", expanded=False):
        for label, command in cmds.items():
            st.markdown(f"**{label}**")
            if st.button(f"🚀 Run '{label}'", key=f"{category}_{label}"):
                if username and ip:
                    ssh_cmd = f'ssh {username}@{ip} "{command}"'
                    st.info(f"⏳ Executing: `{command}` on `{ip}`")
                    try:
                        output = subprocess.getoutput(ssh_cmd)
                        st.success("✅ Execution complete!")
                        st.code(output, language="bash")
                    except Exception as e:
                        st.error(f"❌ Failed: {e}")
                else:
                    st.warning("⚠️ Please enter SSH credentials in the sidebar.")

# ----- Footer -----
st.markdown("<div class='footer'>🌟 Built with ❤️ using Python & Streamlit - Secure and Simple SSH Management</div>", unsafe_allow_html=True)
