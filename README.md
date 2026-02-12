# Storybook Generator

Welcome to the **Storybook Generator** project! This tool leverages state-of-the-art LLMs to help you generate creative writing, storybooks, and more.

## 🚀 Quickstart: Development Environment Setup

Follow these steps to launch your development workspace:

### 1. Install Python 3.11 or newer

Check your python version:
```sh
python --version
```

### 2. Create the Project Directory and Virtual Environment

```sh
python -m venv venv
```

Activate your virtual environment:

- **macOS/Linux:**
  ```sh
  source venv/bin/activate
  ```
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```

### 3. Install Python Dependencies

Install required packages (you can update `requirements.txt` as needed for your project):

```sh
pip install -r requirements.txt
```

### 4. Add your API Keys (never commit this!)

Create a `.env` file in the root of your project, and add your keys:
```env
ANTHROPIC_API_KEY=sk-ant-your-key-here
# Add other API keys as needed
```

### 5. Create a `.gitignore` Before Committing

Ensure you never commit sensitive files:
This will prevent .env file to publish on github and we can store API Secerets locally, all ignored files wont be published to github, its a smart way to exclude the files we dont want to upload on github.

```
.env
venv/
__pycache__/
*.pyc
```

---

You’re ready to start developing!  
See project source files for further documentation and usage instructions.
