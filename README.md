


# 🌟 Building a LLM Chatbot using Google's Gemini-Pro with Streamlit (Python)

🚀 **Mini Chatbot** is a real-time, interactive chatbot powered by **Google's Gemini-Pro API** and built with **Streamlit**. The chatbot allows users to interact with generative AI directly through a user-friendly web interface.

🌐 **Live Demo**: [Try it here!](https://mini-chatbot.streamlit.app/)

---

## 📜 **About the Project**
This project demonstrates how to build and deploy an **LLM-based chatbot** using Google's **Gemini-Pro API**. It features:
- A polished **Streamlit interface** for user interaction.
- Secure management of API keys using **Streamlit Secrets**.
- Integration with **Google's Generative Language Model** for real-time AI responses.

---

## 🛠️ **Features**
- 🔑 **Secure API Key Management**: Environment variables stored securely using `st.secrets`.
- 💬 **Interactive Chat**: Supports real-time user queries with intelligent responses.
- ⚙️ **Customizable**: Easy to adapt for specific use cases or industries.
- 🌍 **Deployed Online**: Accessible globally through Streamlit Cloud.

---


## 🚀 **Getting Started**
Follow these steps to set up the project locally or deploy it online.

### **Prerequisites**
1. Python 3.8 or higher.
2. A Google Cloud account with the **Generative Language API** enabled.
3. Streamlit installed (use the `requirements.txt` file to set it up).

---

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/bopitien/Building-a-LLM-Chatbot-using-Google-s-Gemini-Pro-with-Streamlit-Python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Building-a-LLM-Chatbot-using-Google-s-Gemini-Pro-with-Streamlit-Python
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file to store your Google API Key:
   ```plaintext
   GOOGLE_API_KEY=your_actual_api_key
   ```

---

### **Usage**
1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. Open the app in your browser:
   - The app will run on `http://localhost:8501` by default.

3. Enter a prompt in the input box and interact with the chatbot in real time.

---

## 🌐 **Deployment**
### **Deploy on Streamlit Cloud**
1. Push your code to GitHub (excluding `.env`).
2. Add your Google API Key securely in Streamlit Cloud Secrets:
   ```toml
   GOOGLE_API_KEY = "your_actual_api_key"
   ```
3. The app will automatically use `st.secrets` to retrieve the API Key.

---

## ⚙️ **Built With**
- [Python](https://www.python.org/) - The core programming language.
- [Streamlit](https://streamlit.io/) - For creating the interactive web interface.
- [Google Gemini-Pro API](https://cloud.google.com/) - For generative AI capabilities.

---

## 📂 **File Structure**
```plaintext
Building-a-LLM-Chatbot-using-Google-s-Gemini-Pro-with-Streamlit-Python/
│
├── .devcontainer/          # Development container setup (if applicable)
├── streamlit/              # Additional Streamlit assets (e.g., themes or images)
├── .env                    # Local API key file (excluded in GitHub via .gitignore)
├── .gitattributes          # Git configuration
├── .gitignore              # Excludes sensitive files
├── README.md               # Documentation
├── main.py                 # Main Streamlit chatbot application
├── requirements.txt        # Python dependencies
└── test_gemini_api.py      # Script for testing API connectivity
```

---

## 🌟 **Live Demo**
You can try the live chatbot here:
[https://mini-chatbot.streamlit.app/](https://mini-chatbot.streamlit.app/)

---

## 💡 **Future Improvements**
- Add **user authentication** for personalized experiences.
- Enable **conversation history downloads**.
- Explore **other use cases** like customer support or education assistants.

---

## 🤝 **Contributing**
Contributions are welcome! Feel free to:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## 🧑‍💻 **Author**
👤 **Brume Pascal Opitien**

- GitHub: [@bopitien](https://github.com/bopitien)
- LinkedIn: [Brume Pascal Opitien](https://www.linkedin.com/in/brumetheanalyst)

---

## 🌟 **Acknowledgments**
Special thanks to:
- The **Google Cloud team** for providing the Gemini API.
- The **Streamlit community**
