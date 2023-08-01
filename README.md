# Flask Search Function with DOM-Based XSS Vulnerability
## Description:

Welcome to the Flask Search Function repository, a simple web application showcasing a search functionality powered by Python Flask. This repository includes the source code for a search function that enables users to search for specific data stored in the `data.json` file and display the results on the web interface.

### Features:

1. **Search Functionality:** The repository provides a basic search function that allows users to enter search queries and find relevant data from the `data.json` file.

2. **Python Flask Web Framework:** The web application is built using the popular Python web framework, Flask. Flask provides a straightforward way to create web applications, making it easy to set up routes, handle requests, and serve dynamic content.

3. **Dynamic Templating:** The search results are dynamically rendered using the Jinja2 templating engine in the `index.html` template file, which allows for easy integration of Python variables into HTML.

### Security Note:

Please be aware that the provided search function is susceptible to a DOM-Based Cross-Site Scripting (XSS) vulnerability. DOM-Based XSS is a type of vulnerability that occurs when client-side scripts manipulate the Document Object Model (DOM) in an unsafe manner, leading to potential XSS attacks.

### Usage:

1. Ensure you have Python and Flask installed on your system.
2. Clone the repository to your local machine.
```bash
git clone https://github.com/2024sabuhiabbasov/DOM-based-XSS
```   
3. Navigate to the repository's directory.
```bash
cd DOM-based-XSS
```
4. Run the Flask application using the following command:
```bash
python app.py
```
5. Access the application through your web browser at `http://localhost:5000`.

### Important note:
This repository is for educational and demonstration purposes only. The presence of the DOM-Based XSS vulnerability in the search function is intentional and is included to raise awareness about potential security risks. It is essential to address and fix such vulnerabilities before deploying web applications to production environments.

### Disclaimer
The author of this repository is not responsible for any misuse or unauthorized use of this code. Users are advised to use this code responsibly and in compliance with legal and ethical guidelines.

I hope you find this repository informative and educational. Happy coding and stay secure!
