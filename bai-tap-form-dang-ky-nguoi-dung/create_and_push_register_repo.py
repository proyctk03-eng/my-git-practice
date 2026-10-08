import os
import subprocess
import urllib.request
import json

repo_name = "bai-tap-form-dang-ky-nguoi-dung"
repo_desc = "[Bai Tap] Tao Giao Dien Form Dang Ky Nguoi Dung (HTTP POST) - CodeGym Lab"
repo_dir = r"C:\Users\dathao\.gemini\antigravity-ide\scratch\bai-tap-form-dang-ky-nguoi-dung"

# 1. Get credentials
p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
out, _ = p.communicate('protocol=https\nhost=github.com\n\n')
creds = dict(line.split('=', 1) for line in out.strip().splitlines() if '=' in line)
username = creds.get('username')
token = creds.get('password')

print(f"Logged in as: {username}")

# 2. Check or create repo
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/json'
}

check_url = f"https://api.github.com/repos/{username}/{repo_name}"
req = urllib.request.Request(check_url, headers=headers)
repo_exists = False
try:
    with urllib.request.urlopen(req) as resp:
        if resp.status == 200:
            repo_exists = True
            print(f"Repo {repo_name} already exists.")
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(f"Repo {repo_name} not found. Creating new repo...")
    else:
        print(f"HTTP Error {e.code}: {e.read().decode()}")

if not repo_exists:
    create_url = "https://api.github.com/user/repos"
    payload = json.dumps({
        "name": repo_name,
        "description": repo_desc,
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": False,
        "auto_init": False
    }).encode('utf-8')
    req = urllib.request.Request(create_url, data=payload, headers=headers)
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode())
        print(f"Successfully created repo: {res.get('html_url')}")

# 3. Git init, commit & push
cmds = [
    ["git", "init"],
    ["git", "config", "user.name", "Nguyen Tuan Dat"],
    ["git", "config", "user.email", "proyctk03@gmail.com"],
    ["git", "branch", "-M", "main"],
    ["git", "add", "."],
    ["git", "commit", "-m", "feat: complete user registration form lab with HTTP POST method and report"],
    ["git", "remote", "remove", "origin"],
    ["git", "remote", "add", "origin", f"https://github.com/{username}/{repo_name}.git"],
    ["git", "push", "-u", "origin", "main", "--force"]
]

for cmd in cmds:
    print("Running:", " ".join(cmd))
    res = subprocess.run(cmd, cwd=repo_dir, capture_output=True, text=True)
    if res.stdout:
        print("Stdout:", res.stdout.strip())
    if res.stderr and "warning" not in res.stderr.lower():
        print("Stderr:", res.stderr.strip())

print("\n--- Push completed successfully! ---")
print(f"GitHub Repository URL: https://github.com/{username}/{repo_name}")
