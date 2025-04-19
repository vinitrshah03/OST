""" 
Github Link: https://github.com/vinitrshah03/OST/tree/c0d3/Mini%20Project/AI%20Resume%20Analyzer

This script processes the entire web application for the AI Resume Analyzer. It initializes the Flask application and runs it in debug mode.

Note: This project has been developed using the Factory Design Pattern. This allows for better organization and scalability of the codebase.

Author: Vinit Shah
Date: 18/04/25
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

