# Prerequisites
1. Using `python 3.12.2` but see `pyproject.toml` for what's recommended
# Quickstart
1. Set up repo
    1. Navigate to workspace
    1. Clone repo
        ```bash
        git clone https://github.com/franktcao/babyarcdoodoodoodoo.git
        ```
    1. Go into repo directory
        ```bash
        cd babyarcdoodoodoodoo/
        ```
1. Set up environment
    1. Create virtual environment (**venv**)
        ```bash
        python -m venv .venv
        ```
    1. Activate **venv**
        ```bash
        source .venv/bin/activate
        ```
1. Install dependencies (pick one)
    1. Using pip: Simple but requires dev (me) to pip freeze whenever dependencies change
        ```bash
        pip install --upgrade pip
        pip install -r requirements.txt
        ```
    1. Use poetry: More robust but takes a little bit more effort
        1. Install poetry into **venv**
            ```bash
            pip install poetry
            ```
        1. Reactivate **venv**
            ```bash
            source .venv/bin/activate
            ```
        1. Install dependencies with `poetry`
            ```bash
            poetry install
            ```
1. Reactivate **venv** to ensure environment is updated
    ```bash
    source .venv/bin/activate
    ```
1. Add all ARC-AGI json files into `data/` directory
    1. Go to: https://www.kaggle.com/competitions/arc-prize-2025/data
    1. Scroll down to **Data Explorer**
    1. Click the **Download All** button
    1. Unzip and move contents to this repo's `data/` directory
1. Run app via `streamlit`
    ```bash
    streamlit run app.py
    ```
1. Enjoy.

