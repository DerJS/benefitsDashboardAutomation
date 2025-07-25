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
    
