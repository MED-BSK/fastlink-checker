# FastLink Checker 🚀

A lightweight, robust command-line utility built with Python to audit website availability, status codes, response latency, and redirection hops in real-time.

## Features
- **Status Code Validation**: Verifies HTTP/HTTPS responses (200, 301, 404, 500, etc.).
- **Latency Measurement**: Tracks response time in milliseconds.
- **Redirect Tracking**: Inspects whether the domain triggers HTTP-to-HTTPS or URL redirection chains.
- **Zero Config**: Ready to run directly via CLI.

## Installation

```bash
git clone [https://github.com/MED-BSK/fastlink-checker.git](https://github.com/MED-BSK/fastlink-checker.git)
cd fastlink-checker
pip install requests
