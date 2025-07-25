Paylocity Benefits Dashboard -Automation Challenge 
Jordan Sanchez - Software Quality Engineer 

This repository contains both UI and API automated tests for the Paylocity Benefits Dashboard. 

- UI Automation using Playwright and Pytest (Python),
- API Automation using Postman and Newman (Node.js),

Below, you'll find the Repository Structure, following the Page Object Model (POM) design pattern.

benefitsDashboardAutomation/
├── testsAPI/                    # Postman API tests
├── testsUI/                     # UI Automation tests
│   ├── pages/                   # Page Object Model (POM)
│   ├── tests/                   # Test cases
│       ├── data/                # Used for creating employees
|       └── Helpers/             # Helper methods
├── pytest.ini
├── requirements.txt
└── README.md

Prerequisites:
- Python 3.9 +
- Node.js + npm (for running Newman)
- Postman (optional, for managing API tests)
- Visual Studio Code (recommended)
- Git (to clone the repository)

Setup: 
1. Clone the repository:
    git clone https://github.com/DerJS/benefitsDashboardAutomation.git
    cd benefitsDashboardAutomation

2. Create and activate a virtual environment:
    python -m venv venv
    venv\Scripts\activate  on MacOS:source venv/bin/activate

3. Install Python dependencies and Playwright: 
    pip install -r requirements.txt
    playwright install

4. For running both UI and API automation, your path should look like: 
    (venv) PS "yourRoute"\benefitsDashboardAutomation>

5. Run UI tests (I recommend running test_standard_workflow.py since it covers all previos TC created, the flags headed and slowmo are added to enhance user experice):
    pytest testsUI/tests/test_standard_workflow.py --headed --slowmo 200

6. Run API test:
    install Newman globally: npm install -g newman
    run: newman run testsAPI/automationChallengePostman_collection.json





    
