# Resume Parser with GitHub Actions

This is a simple resume parser built with Python. The main purpose of this project is to serve as a learning exercise for implementing Continuous Integration/Continuous Deployment (CI/CD) pipelines.

## Features

- Parses resume files in various formats (e.g., PDF, DOCX) to extract relevant information.
- Extracts key details such as name, contact information, skills, work experience, education, etc.
- Provides a simple command-line interface (CLI) for interacting with the parser.

## Getting Started

### Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.8
- Pip (Python package manager)

### Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/ashwiniyer176/Resume-Parsing-Portfolio.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Resume-Parsing-Portfolio
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

To use the resume parser, follow these steps:

1. Place your resume file(s) in the `assets/` directory.
2. Run the parser using the following command:

    ```bash
    python main.py
    ```
3. The parser will extract the relevant information from the resume and display it on the console.

## CI/CD Pipeline

This project includes a CI/CD pipeline configured with the following stages:

1. **Build:** Runs unit tests and linters to ensure code quality.
2. **Deploy:** Automatically deploys the application to a staging environment.
3. **Test:** Runs integration tests against the staging environment.
4. **Deploy (Production):** If all tests pass, deploys the application to production.

The CI/CD pipeline is implemented using tools such as GitHub Actions, Travis CI, or Jenkins. Feel free to customize it based on your preferences and requirements.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ashwiniyer176/Resume-Parsing-Portfolio/blob/main/LICENSE) file for details.
