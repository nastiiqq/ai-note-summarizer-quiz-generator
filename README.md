# 🧠 **AI Note Summarizer & Quiz Generator**

### Turn your notes into knowledge — instantly.

An elegant Streamlit app that transforms raw lecture notes into concise summaries or auto-generates quizzes to reinforce learning. Whether you're a student, educator, or lifelong learner, this tool helps you study smarter with the power of AI.

### ✨ **What Is This?**  

#### The Ultimate Study Companion
* 📚 **Summarize Notes**: Paste your notes and get a clean, AI-generated summary 
* 📝 **Generate Quizzes**: Create multiple-choice questions based on your content 
* 🤖 **Powered by LiteLLM**: Fast, secure access to OpenAI models

### 🛠️ **Tech Stack**


| Tool         | Purpose                              |
|--------------|---------------------------------------|
| Python       | Core programming language             |
| Streamlit    | UI framework for interactive apps     |
| LiteLLM      | Lightweight wrapper for OpenAI APIs   |
| CSS          | Custom styling for UI elements        |
| Git & GitHub | Version control and project sharing   |


### 🧩 **Architecture**

```
project-root/
├── app.py                      # Main Streamlit app
└── .streamlit/
    └── config.toml            # Theme configuration
```

### 🔧 **Streamlit Theme** (.streamlit/config.toml)   

```
[theme]  
base="dark"  
primaryColor="#4da1af"  
backgroundColor="#164650"  
secondaryBackgroundColor="#195b67"  
textColor="fafafa"
```

### 🚀 **Quick Start**    
1. Clone the repo
2. Create and activate a virtual environment
3. Install Streamlit and LiteLLM
4. Add your API key
5. Launch the app with `streamlit run app.py`

### 🎮 **How It Works**   
1. **Paste Your Notes**: Drop lecture content or study material into the text box
2. **Choose Your Task**: Select "Summarize Notes" or "Generate Quiz"
3. **Click Start**: The AI processes your input and returns a summary or quiz
4. **Review & Save**: Copy the output or use it to study and test yourself

