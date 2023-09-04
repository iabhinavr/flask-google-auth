# Flask OAuth2 Authentication with Google OAuth2 OpenID Connect

This project demonstrates how to set up OAuth2 authentication with Google OAuth2 OpenID Connect in a Flask web application.

## Getting Started

If you are cloning this repository, follow these steps to set up your project environment:

## Prerequisites

Before you begin, make sure you have the following prerequisites:

- Python installed (version 3.6 or higher)
- Pip (Python package manager) installed
- Git (optional, for cloning the repository)

## Installation

Clone the repository (if you haven't already):

```bash
git clone https://github.com/yourusername/your-repo.git
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

Activate the virtual environment (skip this step if you didn't create a virtual environment):

On Linux/macOS:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install project dependencies from requirements.txt:

```bash
pip install -r requirements.txt
```

## Configuration

Create an .env file in the project root directory with the following environment variables:

```
Copy code
GOOGLE_CLIENT_ID="your-google-client-id.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET="your-client-secret"
GOOGLE_REDIRECT_URI="http://localhost:5000/google/callback"
```

Replace the values with your Google OAuth2 credentials.

### Usage
Run the Flask application:

```bash
flask --app src/app run --debug
```

Access the application in your web browser at http://localhost:5000.

## License

This project is licensed under the MIT License