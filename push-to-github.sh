#!/bin/bash
# Push ActiveLog Technical Repository to GitHub
# Run this from Git Bash or WSL

echo "Pushing ActiveLog-TechnicalRepo to GitHub..."

# Navigate to repository directory
cd "$(dirname "$0")"

# Check if repository exists
if [ ! -d ".git" ]; then
    echo "Error: Not a git repository"
    exit 1
fi

# Show status
echo -e "\nRepository Status:"
git status

# Show what will be pushed
echo -e "\nCommit to be pushed:"
git log -1 --oneline

# Push to GitHub
echo -e "\nPushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo -e "\n✅ Successfully pushed to GitHub!"
    echo "Repository: https://github.com/ctothed/SuperInstance"
else
    echo -e "\n❌ Push failed. Please check your GitHub credentials."
    echo "Try running: gh auth login"
    exit 1
fi
