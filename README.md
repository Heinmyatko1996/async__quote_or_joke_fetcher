---
# Joke and Quote Fetcher

This project fetches and displays a random joke and a random inspirational quote using asynchronous programming in Python. It leverages the `jokeapi` library for jokes and the ZenQuotes API for quotes.
This project demonstrates how to asynchronously fetch and display data from multiple external APIs using Python. While the current example uses a joke and quote API, the underlying principles and patterns are directly applicable to building scalable data ingestion pipelines for **Big Data Engineering** scenarios.

---
## Features

* **Fetches Random Jokes**: Retrieves a diverse range of jokes using the JokeAPI.
* **Fetches Inspirational Quotes**: Gets random quotes from the ZenQuotes API.
* **Asynchronous Operations**: Uses `asyncio` and `aiohttp` for concurrent fetching, ensuring efficient execution.
* **Detailed Logging**: Provides clear logs for API invocation start/end times and any potential errors.

---
## Prerequisites

Before you run this application, make sure you have the following installed:

* **Python 3.13+**
* **uv** (optional)
* **virtual environment**

---
## Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone https://github.com/Heinmyatko1996/async__quote_or_joke_fetcher.git
    cd async__quote_or_joke_fetcher
    ```

2.  **Install the required libraries:**
    ```
    pip install -r requirements.txt
    ```
    (or if you have uv installed, make sure you have virtual environment setup before installing it.)
    ```
    uv pip install -r requirements.txt
    ```

---
## How to Run

Simply execute the main Python file:

```bash
python main.py
```
or
```
uv run main.py