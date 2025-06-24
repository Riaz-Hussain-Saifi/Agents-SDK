# Crypto Agent

A brief one-sentence description of what this project does.

## Description

A more detailed description of the project. Explain the problem it solves, its main purpose, and the technologies used. For example, is it a crypto price tracker, a trading bot, or an analysis tool?

## Features

*   **Feature 1:** Real-time cryptocurrency price tracking.
*   **Feature 2:** User authentication and portfolio management.
*   **Feature 3:** Data visualization with charts and graphs.

## Technologies Used

*   Python 3.x
*   Flask / FastAPI (or other framework)
*   Gunicorn
*   List any major libraries (e.g., requests, pandas, matplotlib)
*   List any APIs used (e.g., CoinGecko, Binance API)

## Getting Started

### Prerequisites

*   Python 3.8+
*   pip

### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/your-username/Crypto_Agent.git
    cd Crypto_Agent
    ```
2.  Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

```sh
gunicorn main:app
```
The application will be available at `http://127.0.0.1:8000`.

## Deployment on Railway

This project is configured for deployment on Railway. Simply connect your GitHub repository to a new Railway project, and it will be deployed automatically. Any required environment variables (like API keys) should be set in the project's "Variables" tab on the Railway dashboard.