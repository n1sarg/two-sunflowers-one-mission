# 🌳 Git Guide — Your Code's Save Game System

> **Think of Git like the save system in a video game.**
> Every commit = a save point. Branches = parallel timelines.
> If you mess up? Just reload from a save. No stress.

---

## 🤔 What is Git and Why Should I Care?

Imagine you're writing a story. You write Chapter 1, love it. Start Chapter 2,
hate it, want to go back. Without Git, you'd need folders like:

```
story_v1.py
story_v2.py
story_v2_final.py
story_v2_final_ACTUALLY_final.py
story_v2_PLEASE_WORK.py     😭
```

With Git, you just have ONE file and Git remembers every version automatically.
You can jump to any point in time, see what changed, and undo anything.

**Git** = tracks changes on YOUR computer (local)
**GitHub** = stores your code online so you can share it and collaborate (remote)

Think of it this way: Git is your diary, GitHub is publishing it online.

---

## 🧱 Key Concepts (The Building Blocks)

| Concept | What It Means | Real-Life Analogy |
|---------|---------------|-------------------|
| **Repository (Repo)** | A project folder tracked by Git | A notebook with infinite pages |
| **Commit** | A saved snapshot of your changes | Pressing "Save Game" |
| **Stage** | Selecting which changes to save | Choosing which photos to put in an album |
| **Branch** | A parallel version of your code | An alternate timeline |
| **Merge** | Combining two branches together | Two timelines becoming one |
| **Clone** | Copying a remote repo to your computer | Downloading a game |
| **Push** | Uploading your commits to GitHub | Uploading your save to the cloud |
| **Pull** | Downloading the latest from GitHub | Syncing your cloud save |
| **Remote** | The online version (GitHub) | The cloud backup |

---

## 🎮 Level 1: Solo Basics (Your First Day with Git)

These are the commands you'll use 90% of the time. Master these and you're golden.

### Starting a New Project

```bash
# Turn any folder into a Git-tracked project
git init

# What just happened?
# Git created a hidden .git/ folder — that's where all the magic lives
# Your folder is now a "repository" (repo for short)
```

### The Save Game Loop (you'll do this 100 times)

```bash
# Step 1: Check what's changed
git status
# 🔍 This shows you which files are modified, new, or deleted
# Red files = changed but not staged
# Green files = staged and ready to commit

# Step 2: Stage your changes (pick what to save)
git add .
# The dot (.) means "everything" — stage all changes
# Want to be specific? Use: git add filename.py

# Step 3: Commit (actually save it!)
git commit -m "your message here"
# The -m flag lets you add a message describing what you did
# GOOD: git commit -m "✨ Added temperature control to playlist namer"
# BAD:  git commit -m "stuff"
# BAD:  git commit -m "update"

# Step 4: See your save history
git log --oneline
# Shows a compact list of all your saves (commits)
# Each one has a unique ID (hash) like: a1b2c3d
```

### ✍️ Writing Good Commit Messages

Your commit messages are your learning journal! Make them useful:

```bash
# 🎉 For new features or milestones
git commit -m "🎉 First API call works! Learned about system prompts"

# 🐛 For bug fixes
git commit -m "🐛 Fixed API key error — .env file wasn't loading"

# ✨ For improvements
git commit -m "✨ Added Rich panels — terminal output looks beautiful now"

# 📝 For documentation
git commit -m "📝 Added comments explaining temperature parameter"

# 🔧 For configuration
git commit -m "🔧 Added .gitignore to protect API keys"

# 🧪 For experiments
git commit -m "🧪 Testing different temperatures — 0.9 is wild!"
```

### 🚨 The Golden Rule

**NEVER commit your `.env` file or API keys!**

Your `.gitignore` file tells Git to ignore certain files:

```
# .gitignore — files Git should pretend don't exist
.env              # API keys — TOP SECRET!
venv/             # Virtual environment — too big, anyone can recreate
__pycache__/      # Python cache — auto-generated junk
*.pyc             # Compiled Python files — also junk
.DS_Store         # Mac system file — nobody wants this
```

Always create `.gitignore` BEFORE your first commit. If you accidentally
commit a secret, it lives in Git history forever (well, it's fixable but painful).

---

## 🎮 Level 2: Going Online with GitHub

Now your code lives on your computer AND the internet. Collaboration unlocked!

### First-Time Setup (Do This Once)

```bash
# Tell Git who you are
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Connecting Your Local Repo to GitHub

```bash
# 1. Create a new repository on GitHub (use the website)
#    - DON'T check "Initialize with README" (you already have one)

# 2. Connect your local repo to GitHub
git remote add origin https://github.com/yourusername/storybook-generator.git
# "origin" is just a nickname for the GitHub URL
# Think of it as saving a contact in your phone

# 3. Push (upload) your code for the first time
git push -u origin main
# -u sets "origin main" as the default, so next time you just type: git push

# 4. From now on, your daily flow is:
git add .
git commit -m "your message"
git push
# That's it. Three commands. Every time.
```

### Getting Changes FROM GitHub

```bash
# Download the latest changes (when your partner pushed something)
git pull
# This fetches + merges changes into your local copy
```

---

## 🎮 Level 3: Branches (Parallel Timelines!)

This is where Git gets POWERFUL. Branches let you experiment without breaking
anything. Think of it as creating a parallel universe where you can try wild
ideas — if they work, merge them back. If not, delete the universe. No harm done.

```bash
# Create a new branch AND switch to it
git checkout -b experiment/crazy-feature
# You're now in a parallel timeline!
# Anything you do here won't affect "main"

# See all your branches
git branch
# The * shows which branch you're currently on

# Switch between branches
git checkout main            # Go back to main timeline
git checkout experiment/crazy-feature  # Go back to experiment

# When your experiment works — merge it into main!
git checkout main            # First, go to main
git merge experiment/crazy-feature     # Bring the changes in
# 🎉 Your experiment is now part of the main story!

# Clean up — delete the branch you merged
git branch -d experiment/crazy-feature
```

### Branch Naming Convention (for this project)

```bash
# Pattern: type/short-description
feature/add-streaming          # New feature
fix/api-key-loading            # Bug fix
experiment/try-langchain       # Just trying something
docs/update-readme             # Documentation
```

---

## 🎮 Level 4: Collaboration with Pull Requests

When working with a partner (or contributing to any project), Pull Requests (PRs)
are how you propose changes. It's like saying "Hey, I made these changes on my
branch — can you review them before we merge into main?"

### The PR Workflow

```bash
# 1. Create a branch for your work
git checkout -b feature/add-pdf-reader

# 2. Do your work, commit as you go
git add .
git commit -m "✨ Added PDF reader using PyMuPDF"

# 3. Push your branch to GitHub
git push origin feature/add-pdf-reader

# 4. Go to GitHub.com → Your Repo → Click "Compare & Pull Request"
#    Write a description of what you changed and why
#    Your partner reviews it, leaves comments, approves

# 5. Click "Merge Pull Request" on GitHub
#    🎉 Changes are now in main!

# 6. Back on your computer, update your local main
git checkout main
git pull
```

---

## 🚑 Git First Aid Kit (When Things Go Wrong)

Don't panic! Here's how to fix common mistakes:

```bash
# "I committed but forgot to add a file"
git add forgotten_file.py
git commit --amend
# This adds it to your LAST commit instead of making a new one

# "I want to undo my last commit but keep the changes"
git reset --soft HEAD~1
# Your changes are still there, just un-committed

# "I want to see what changed in a file"
git diff filename.py
# Shows line-by-line what was added (+) and removed (-)

# "I messed up this file and want the last saved version"
git checkout -- filename.py
# ⚠️ This DISCARDS your changes! Use carefully

# "I'm on the wrong branch!"
git stash                    # Temporarily hide your changes
git checkout correct-branch  # Switch to right branch
git stash pop                # Bring your changes back
```

---

## 🎓 Cheat Sheet (Print This!)

```
┌─────────────────────────────────────────────────────────┐
│                    GIT CHEAT SHEET                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  DAILY FLOW:                                            │
│    git status           → What changed?                 │
│    git add .            → Stage everything              │
│    git commit -m "msg"  → Save snapshot                 │
│    git push             → Upload to GitHub              │
│    git pull             → Download from GitHub          │
│                                                         │
│  BRANCHES:                                              │
│    git checkout -b name → Create + switch               │
│    git checkout main    → Switch to main                │
│    git merge name       → Merge branch into current     │
│                                                         │
│  CHECK STUFF:                                           │
│    git log --oneline    → See commit history            │
│    git diff             → See what changed              │
│    git branch           → List all branches             │
│                                                         │
│  OH NO:                                                 │
│    git reset --soft HEAD~1  → Undo last commit          │
│    git stash / git stash pop → Hide/restore changes     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## 🎮 Practice It!

The best way to learn Git is by doing. Here are two fun interactive tools:

### 🕹️ Oh My Git!
A game with playing cards that teaches Git visually.
Download it free: **https://ohmygit.org/**

### 🌳 Learn Git Branching
An interactive web tutorial that visualizes branches in real time.
Try it now: **https://learngitbranching.js.org/**

---

## 🏆 Your Git Milestones for This Course

- [ ] Weekend 1: First commit, push to GitHub
- [ ] Weekend 1: Create your first branch
- [ ] Weekend 2: Make a pull request, merge it
- [ ] Weekend 3: Resolve your first merge conflict (it's a rite of passage!)
- [ ] Weekend 4: Clean commit history telling the story of your project

*Your Git history is proof of your learning journey. Make it a good story!* 🌟