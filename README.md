# Crypto Agent 🤖

Crypto Agent is an intelligent, conversational AI agent designed to assist with cryptocurrency-related tasks and queries. It leverages the power of Large Language Models (LLMs) from multiple providers to deliver accurate and timely information through an interactive chat interface.

This project is built with Python and utilizes the [Chainlit](https://chainlit.io) framework for its user interface.

## ✨ Features

- **Conversational Interface**: Interact with the agent using natural language thanks to the Chainlit UI.
- **Multi-Provider LLM Support**: Easily switch between different LLM providers like OpenAI, LiteLLM, and others.
- **Hugging Face Integration**: Leverages the `huggingface_hub` library for seamless interaction with models and resources on the Hugging Face Hub.
- **Extensible Agent Framework**: Built on a modular agent architecture that can be extended with new tools and capabilities.

## 🛠️ Technologies Used

- **Backend**: Python
- **UI Framework**: Chainlit
- **AI/LLM**:
    - `agents` library (custom or framework)
    - `huggingface_hub`
    - OpenAI
    - LiteLLM
- **And other Python libraries...**

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- A virtual environment tool like `venv` or `conda`.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd Crypto_Agent
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    (You should create a `requirements.txt` file for your project)
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root of the project and add your API keys:
    ```
    OPENAI_API_KEY="sk-..."
    # Add other necessary API keys or configurations
    ```

### Running the Application

To start the Crypto Agent, run the following command from the root of the project:

```bash
chainlit run app.py -w
```

This will start the Chainlit server, and you can access the application in your browser at `http://localhost:8000`.

---

*This README was generated based on the project structure and dependencies.*