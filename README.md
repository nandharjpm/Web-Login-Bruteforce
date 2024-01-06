# Web Application Penetration Testing Tool: Web Login Brutefocer

This script is crafted for assessing security robustness in web applications.
which is concentrates on the demo.testfire.net/doLogin site to elevating security practices

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nandharjpm/Web-Login-Bruteforce.git
   ```
2. Install dependencies:
   ```bash
   pip install requests
   ```
3. File Permission:
   ```bash
   chmod +x bruteforce.py
   ```
### Usage
   ```bash
   ./bruteforce.py -u http://demo.testfire.net/doLogin -U uname.txt -P paswd.txt
   ```

Prepare a list of usernames in a file named "uname.txt" and passwords in a file named "paswd.txt".
Customize the headers and cookies in the script (if needed) for your specific testing scenario.

Run the script:

python3 bruteforce.py

Configuration:

Modify the script to suit your testing needs. You can customize headers, cookies, and other parameters directly in the script.

### Results and Output:

The script will display attempts and indicate whether they were successful or failed. Monitor the output for valuable insights.

### Disclaimer

This tool is intended for educational purposes only. Ensure you have proper authorization before using it on any website or application.
Unauthorized penetration testing may be illegal and can result in serious consequences. Use responsibly and in accordance with ethical hacking guidelines.

### Acknowledgments

Thanks to the [Requests](https://pypi.org/project/requests/) library for simplifying HTTP requests.

Contact Information:
For questions, feedback, or issues, feel free to contact the project maintainer:
Nandhakumar S
nandharjpm@gmail.com
GitHub Profile: github.com/nandharjpm
