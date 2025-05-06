import pyperclip
import time
import subprocess
import os

FILENAME = "F:\Python Info Github\Python Basic\python_Basic2.py"

# Step 1: Read clipboard content once
clipboard_content = pyperclip.paste()
lines = clipboard_content.splitlines()

# Step 2: Initialize git if not already a git repo
if not os.path.exists(".git"):
    subprocess.run(["git", "init"])
    print("✅ Git repo initialized.")

# Step 3: Loop over each line
for line in lines:
     # Wait for 5 seconds
    
    # Append line to file
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    
    # Git add and commit
    subprocess.run(["git", "add", FILENAME])
    commit_msg = f"Add line: {line}"
    subprocess.run(["git", "commit", "-m", commit_msg])
    print(f"✅ Committed line: {line}")
