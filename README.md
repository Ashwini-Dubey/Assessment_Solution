# Star Wars Automation Project

This repo has basic tests for the **Star Wars** frontend and the **SWAPI-Node** API.

---

## Prerequisites

* Node.js ≥ 18
* Python ≥ 3.10
* Chrome (latest)

Make sure Chrome is installed. Selenium uses it via `webdriver-manager`.

---

## Run the Frontend

```bash
# clone and enter project
git clone https://github.com/MindfulMichaelJames/star-wars
cd star-wars

# install dependencies
npm install

# build and start
npm run build
npm start
```

The app runs on: [http://localhost:3000](http://localhost:3000)

Keep it running while UI tests are executed.

---

## Run the Tests

Test files:

* `test_ui.py` → UI tests using Selenium
* `test_api.py` → API tests using requests

### 1. Setup virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the tests

```bash
python test_ui.py
python test_api.py
```

You can also use `pytest` if installed.

---

## Project Structure

```
star-wars-automation/
├── README.md
├── requirements.txt
├── test_ui.py
├── test_api.py
└── star-wars/
```

---
