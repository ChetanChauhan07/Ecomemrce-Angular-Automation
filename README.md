# 🛒 E-commerce Angular Automation

Automated test framework for an Angular-based e-commerce web application using **Selenium**, **PyTest**, and **pytest-html**.

---

## ⚙️ Features

- Multi-browser support (Chrome & Firefox via command-line flag)
- Page Object Model (POM) for maintainable test design
- Detailed HTML reports with inline screenshots on failures
- Configurable via CLI: run in headless mode, choose browser, etc.
- Easily extendable for new test scenarios

---

## 🧩 Project Structure

```text
.
├── pages/               # Page object model classes
├── tests/               # Actual test scripts
├── conftest.py          # Fixtures & hooks (includes screenshot logic)
├── requirements.txt     # Python dependencies
└── Reports/             # Generated HTML reports and screenshots
🚀 Setup & Installation
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/ChetanChauhan07/Ecomemrce-Angular-Automation.git
cd Ecomemrce-Angular-Automation
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Ensure you have:

Python 3.7+ installed

ChromeDriver & GeckoDriver (Firefox) in your PATH

🧪 Running Tests
bash
Copy
Edit
pytest \
  --browser_name=chrome \
  --html=Reports/report.html \
  --self-contained-html \
  -q
Flags & Options:

--browser_name=[chrome|firefox] — choose browser

--html=... — path to generated HTML report

--self-contained-html — embeds screenshots into the report

-q — quiet mode (minimal console output)

📷 Screenshots on Failure
Tests that fail during execution automatically save a screenshot to the Reports/ folder and display a thumbnail in the HTML report. Clicking it opens the full image—great for diagnosing UI issues!

🧱 Extending the Framework
Add a new Page Object
Create a class under pages/ defining locators & actions.

Write a new test in tests/ using your page object(s).

Run the test as above—you'll get pass/fail statuses, logs, screenshots, and report generated.

🛠️ Troubleshooting
No screenshots in report?
Ensure you used:

bash
Copy
Edit
--html=Reports/report.html --self-contained-html
Browser not launching?
Check that the respective driver (chromedriver/geckodriver) is in your PATH and matches your browser version.

Files not committing?
Screenshots and reports are auto-generated at runtime—no need to add or commit them to Git.

🧠 Best Practices
Keep all test logic within Page Objects—tests should drive the scenarios, not the browser directly.

Use pytest.mark.parametrize() to test multiple data variations.

Integrate with CI/CD pipelines to publish Reports/report.html after builds.

📬 Contributions & Issues
Bug reports or enhancement requests? Open an Issue!

Feature ideas or fixes? Send a Pull Request—happy to help!

📄 License
This project is licensed under the MIT License.
See the LICENSE file for details.

yaml
Copy
Edit

---

### ✅ Next Steps

1. Save this as `README.md` in your project root.
2. Customize project name, badges, or screenshots as desired.
3. Add `requirements.txt` with:
selenium
pytest
pytest-html
