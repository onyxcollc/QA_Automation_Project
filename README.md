# 🧪 QA Automation Framework – Python + Pytest

Welcome to the QA Automation Framework! This project is designed to demonstrate professional-level automation testing skills using Python, Pytest, Selenium, and Requests. It covers both **UI testing** and **API testing**, and is fully integrated with CI/CD pipelines using **GitHub Actions**.

---

## 📁 Project Structure

```
qa_automation/
├── tests/
│   ├── ui/
│   │   ├── test_login.py
│   │   └── test_checkout.py
│   ├── api/
│   │   ├── test_users.py
│   │   └── test_posts.py
│   └── conftest.py
├── pages/                     # Page Object Model for UI
│   ├── base_page.py
│   ├── login_page.py
│   └── cart_page.py
├── data/
│   ├── test_data.json
│   └── api_payloads.json
├── utils/
│   ├── logger.py
│   ├── api_helpers.py
│   └── wait_utils.py
├── reports/
│   ├── allure-results/
│   └── html/
├── .github/
│   └── workflows/
│       └── test.yml
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## 🛠️ Tech Stack

| Purpose         | Tool/Library         |
|----------------|----------------------|
| Language        | Python 3.x           |
| Testing         | Pytest               |
| UI Automation   | Selenium             |
| API Automation  | Requests, JSONSchema |
| Reporting       | Allure, pytest-html  |
| CI/CD           | GitHub Actions       |
| Framework Style | POM + Fixtures       |

---

## 🧪 How to Run Tests

### ✅ 1. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### ✅ 2. Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ 3. Run all tests

```bash
pytest -v
```

### ✅ 4. Run specific test

```bash
pytest tests/ui/test_login.py
```

### ✅ 5. Generate Allure Report

```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```

---

## 🌐 UI Testing (Selenium)

- Login functionality
- Cart and checkout flows
- Negative test cases
- Page Object Model for clean design
- Screenshots captured on failure

---

## 🔌 API Testing (Requests)

- REST API tests for endpoints (GET, POST, PUT, DELETE)
- JSON schema validation
- Token authentication handling
- Modular helper functions and payloads

---

## ⚙️ CI/CD Integration

✅ GitHub Actions is used to automatically:
- Install dependencies
- Run tests
- Upload reports as artifacts

`.github/workflows/test.yml` defines the full CI pipeline.

---

## 📈 Reporting

| Format      | Tool           |
|-------------|----------------|
| HTML        | pytest-html    |
| Interactive | Allure Reports |

---

## 📚 Learning Goals

This project demonstrates:
- Practical use of Pytest for structured automation
- Implementation of Page Object Model for scalability
- Integration of API testing and validation
- CI pipeline to simulate real-world deployment workflows

---

## 🤝 Contributing

This is a personal learning project. If you find bugs, feel free to fork and contribute. For discussions, open an issue.

---

## 🧠 Author

**Nicholas Olumese**  
QA Automation Engineer in training – Dedicated to building robust, scalable test solutions using Python.

---

## 📌 To-Do / Next Features

- [ ] Docker integration
- [ ] TestRail integration
- [ ] Pytest-parallel (xdist)
- [ ] SQL/DB validation layer
