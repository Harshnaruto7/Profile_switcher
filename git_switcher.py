from dotenv import load_dotenv
import os
import subprocess
import sys

load_dotenv()  # Load .env variables

profiles = {
    "personal": {
        "name": os.getenv("GIT_NAME"),
        "email": os.getenv("GIT_EMAIL")
    },
    "work": {
        "name": os.getenv("GIT_USER"),
        "email": os.getenv("GIT_Gmail")
    }
}

profile = sys.argv[1] if len(sys.argv) > 1 else None

if profile not in profiles:
    print("❌ Invalid profile. Use 'personal' or 'work'.")
    sys.exit(1)

selected = profiles[profile]

# Run git config commands
subprocess.run(["git", "config", "--global", "user.name", selected["name"]])
subprocess.run(["git", "config", "--global", "user.email", selected["email"]])

print(f"✅ Switched to {profile} profile:")
print(f"   Name: {selected['name']}")
print(f"   Email: {selected['email']}")
