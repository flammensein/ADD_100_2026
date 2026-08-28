# `GH007` refers to the email stored in your **Git commit metadata**, not your Python code. GitHub blocks pushes when that email is marked private.

# Check it with:

# ````powershell
git log -1 --format=fuller
git config --global user.email
git config user.email
# ````

# Use your GitHub-provided `noreply` email:

# ````powershell
git config --global user.email "29759055+flammensein@users.noreply.github.com"
git commit --amend --reset-author --no-edit
git push --force-with-lease
# ````

# You can find the correct noreply address under **GitHub → Settings → Emails**.