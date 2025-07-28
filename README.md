# 🐞 Bug Reporter: Automated UI Test with Screenshot and Markdown Report

This is a simple example of a UI test automation pipeline using **Selenium + Pytest**.
It tests an invalid login scenario on the website [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login), and generates:

- ❌ A bug screenshot (when the test fails)
- 📄 A bug report in Markdown format with the error message and screenshot link

---

## 🚀 Features

- ✅ Automated browser test using Selenium WebDriver
- 📸 Screenshot capturing on failure
- 📝 Bug report auto-generation in `reports/`
- 🧪 Easy to extend with more tests
- 📁 Clean structure, Git-friendly

---

## 🧪 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run test
```bash
pytest tests/
```

If a test fails, it will automatically:
- Save a screenshot in `screenshots/`
- Create a `.md` bug report in `reports/`

---

## 🛠 Project Structure
```
bug_reporter/
├── reports/            # Generated Markdown bug reports
├── screenshots/        # Screenshots of failed tests
├── tests/              # Pytest test files
│   └── test_login.py
├── conftest.py         # Pytest fixture: browser setup & teardown
├── requirements.txt    # All Python dependencies
├── .gitignore          # Ignore reports/screenshots/__pycache__
└── README.md           # This file
```

---

## 🧠 Tech Used

- Python 3.9+
- Selenium
- Pytest
- ChromeDriver

---

## 📌 Notes

- Uses `herokuapp.com` as a dummy test site
- Requires Chrome browser and compatible `chromedriver`
- Tested on macOS — cross-platform support expected

---

## 📫 Contact

This project was created for demo purposes by a QA enthusiast VikNo. 

TG: @jakethebirdy

Feel free to fork, extend, or reach out!

