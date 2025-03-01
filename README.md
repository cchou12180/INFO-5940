# 📌 Chatbot File Q&A

Welcome to the **Chatbot File Q&A** repository! This guide will help you set up the development environment using **Docker** in **VS Code**, configure the **OpenAI API key**, and run the chatbot that allows users to upload `.txt` and `.pdf` documents and interact with their content.

---

## 🛠️ Prerequisites  

Before starting, ensure you have the following installed on your system:

- [Docker](https://www.docker.com/get-started) (Ensure Docker Desktop is running)
- [VS Code](https://code.visualstudio.com/)
- [VS Code Remote - Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Git](https://git-scm.com/)
- OpenAI API Key
- Python 3.11+

---

## 🚀 Setup Guide  

### 1️⃣ Clone the Repository  

Open a terminal and run:  

```bash
git clone https://github.com/your-repo/chatbot-file-qna.git
cd chatbot-file-qna
```

---

### 2️⃣ Open in VS Code with Docker  

1. Open **VS Code**, navigate to the `chatbot-file-qna` folder.  
2. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac) and search for:  
   ```
   Remote-Containers: Reopen in Container
   ```
3. Select this option. VS Code will build and open the project inside the container.  

📌 **Note:** If you don’t see this option, ensure that the **Remote - Containers** extension is installed.  

---

### 3️⃣ Configure OpenAI API Key  

Since `docker-compose.yml` expects environment variables, follow these steps:

#### ➤ Option 1: Set the API Key in `.env` (Recommended)  

1. Inside the project folder, create a `.env` file:  

   ```bash
   touch .env
   ```

2. Add your API key:  

   ```plaintext
   OPENAI_API_KEY=your-api-key-here
   ```

3. Modify `docker-compose.yml` to include this `.env` file:  

   ```yaml
   version: '3.8'
   services:
     devcontainer:
       container_name: chatbot-devcontainer
       build:
         dockerfile: Dockerfile
         target: devcontainer
       environment:
         - OPENAI_API_KEY=${OPENAI_API_KEY}
       volumes:
         - '.:/workspace'
       env_file:
         - .env
   ```

4. Restart the container:  

   ```bash
   docker-compose up --build
   ```

Now, your API key will be automatically loaded inside the container.  

---

## 💬 Running the Chatbot  

Once the environment is set up, run the chatbot using Streamlit:

```bash
streamlit run chatbot.py
```

This will start a **web application** where you can upload documents and chat with them.

---

## 🏗️ Features  

✅ **Upload .txt and .pdf files**
✅ **Ask questions based on document content**
✅ **Handles multiple documents**
✅ **Processes large files efficiently**
✅ **Interactive chat interface**

---

## 🛠️ Troubleshooting  

### **Container Fails to Start?**  
- Ensure **Docker Desktop is running**.  
- Run `docker-compose up --build` again.  
- If errors persist, delete existing containers with:  

  ```bash
  docker-compose down
  ```

  Then restart:  

  ```bash
  docker-compose up --build
  ```

### **OpenAI API Key Not Recognized?**  
- Check if `.env` is correctly created.  
- Ensure `docker-compose.yml` includes `env_file: - .env`.  
- Restart the container after making changes (`docker-compose up --build`).  

---

## 🎯 Next Steps  

- Improve the chatbot by fine-tuning responses.  
- Add support for more document types.  
- Enhance the UI for a better user experience.  




