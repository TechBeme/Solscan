<div align="center">

# 🔗 Solscan Transaction Viewer

**A Flask web application for viewing and exporting Solana blockchain transactions**

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)](https://flask.palletsprojects.com/)
[![Solana](https://img.shields.io/badge/Solana-Blockchain-9945FF?logo=solana)](https://solana.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[Features](#-features) • [Quick Start](#-quick-start) • [Usage](#-usage) • [API](#-api) • [Tech Stack](#%EF%B8%8F-tech-stack) • [License](#-license)

**Languages:** [🇧🇷 Português](README.pt-BR.md) • [🇪🇸 Español](README.es.md)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [API](#-api)
- [Tech Stack](#%EF%B8%8F-tech-stack)
- [Configuration](#%EF%B8%8F-configuration)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

**Solscan Transaction Viewer** is a lightweight Flask web application that fetches and displays transaction history for any Solana wallet address using the Solscan API. It provides an interactive, searchable table view with sorting capabilities and CSV export functionality.

Perfect for:
- 📊 Analyzing wallet transaction history
- 🔍 Searching and filtering transactions
- 📥 Exporting transaction data to CSV
- 📈 Tracking blockchain activity

---

## 👨‍💻 About the Developer

<div align="center">

**Developed by Rafael Vieira (TechBeme)**

[![GitHub](https://img.shields.io/badge/GitHub-TechBeme-181717?logo=github)](https://github.com/TechBeme)
[![Fiverr](https://img.shields.io/badge/Fiverr-Tech__Be-1DBF73?logo=fiverr)](https://www.fiverr.com/tech_be)
[![Upwork](https://img.shields.io/badge/Upwork-Profile-14a800?logo=upwork)](https://www.upwork.com/freelancers/~01f0abcf70bbd95376)
[![Email](https://img.shields.io/badge/Email-contact@techbe.me-EA4335?logo=gmail)](mailto:contact@techbe.me)

**Full-Stack Developer & Automation Specialist**

Specialized in **web scraping**, **automation systems**, **modern web applications**, and **API integrations**.

### 💼 Core Expertise

- 🔍 Web Scraping & Data Extraction
- ⚡ Process Automation & Workflows
- 💻 Full-Stack Development (Flask, React, Python, TypeScript)
- 🔌 API Development & Integrations
- 🗄️ Database Design & Optimization
- 🎨 Modern UI/UX Development

### 🌍 Languages

🇺🇸 **English** • 🇧🇷 **Português** • 🇪🇸 **Español**

### 📬 Contact

**Email**: [contact@techbe.me](mailto:contact@techbe.me)

</div>

---

## ✨ Features

### Data Visualization
- **Interactive DataTable**: Search, sort, and filter transactions with ease
- **Transaction Details**: View signature, block number, timestamp, instructions, signers, and fees
- **Real-time Data**: Fetches up-to-date transaction data from Solscan API
- **Responsive Design**: Works on desktop and mobile devices

### Export Capabilities
- **CSV Export**: Download transaction data in tab-delimited CSV format
- **Formatted Data**: Properly formatted SOL fees (9 decimal places)
- **Complete History**: Export all transactions at once

### Technical Features
- **High Limit Queries**: Fetches up to 99,999,999 transactions per address
- **Instruction Parsing**: Groups and displays parsed instruction types
- **Fee Conversion**: Automatic conversion from lamports to SOL
- **In-Memory Storage**: Fast CSV generation and downloads

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/TechBeme/Solscan.git
cd Solscan

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# Development mode
python flask-solscan.py

# Production mode with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 flask-solscan:app
```

The application will start on `http://localhost:5000` (development) or `http://localhost:8000` (production).

---

## 📖 Usage

### Viewing Transactions

1. Open your browser and navigate to:
   ```
   http://localhost:5000/<WALLET_ADDRESS>
   ```
   Replace `<WALLET_ADDRESS>` with any valid Solana wallet address.

2. The page will display an interactive table with all transactions for that address.

### Using the DataTable

- **Search**: Use the search box to filter transactions by any field
- **Sort**: Click column headers to sort ascending/descending
- **Pagination**: Navigate through pages of transactions
- **Items per page**: Adjust how many transactions to display at once

### Exporting Data

Click the **"Download CSV"** button at the bottom of the page to download all transaction data in CSV format with tab delimiters.

---

## 🔌 API

### Endpoints

#### `GET /<address>`

Fetches and displays transactions for the specified Solana wallet address.

**Parameters:**
- `address` (path parameter): Solana wallet address

**Response:**
- HTML page with interactive DataTable

**Example:**
```
http://localhost:5000/DYw8jCTfwHNRJhhmFcbXvVDTqWMEVFBX6ZKUmG5CNSKK
```

#### `GET /download/<address>`

Downloads transaction data as a CSV file.

**Parameters:**
- `address` (path parameter): Solana wallet address (must be previously queried)

**Response:**
- CSV file with tab-delimited transaction data

**Example:**
```
http://localhost:5000/download/DYw8jCTfwHNRJhhmFcbXvVDTqWMEVFBX6ZKUmG5CNSKK
```

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|----------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) | 3.8+ | Core programming language |
| ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white) | 3.0+ | Web framework |
| **Requests** | 2.31+ | HTTP client for API calls |
| **Pandas** | 2.0+ | Data processing and CSV generation |
| **Gunicorn** | 21.0+ | Production WSGI server |
| **jQuery** | 3.6.0 | JavaScript library |
| **DataTables** | 1.11.5 | Interactive table plugin |
| **Solscan API** | v2 | Blockchain transaction data |

---

## ⚙️ Configuration

### Environment Variables

No environment variables required for basic usage. The application uses Solscan's public API.

### Custom Port

To run on a different port:

```bash
# Development
flask --app flask-solscan run --port 8080

# Production
gunicorn -w 4 -b 0.0.0.0:8080 flask-solscan:app
```

### Worker Configuration

For production deployments, adjust Gunicorn workers based on your server:

```bash
# Formula: (2 x CPU_CORES) + 1
gunicorn -w 9 -b 0.0.0.0:8000 flask-solscan:app  # For 4-core CPU
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Reporting Issues

Please report bugs and request features through [GitHub Issues](https://github.com/TechBeme/Solscan/issues).

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 Rafael Vieira (TechBeme)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## ⚠️ Disclaimer

This project is **independent** and **not affiliated with Solscan or Solana**. It's a third-party tool that uses publicly available data from the Solscan API for educational and analytical purposes.

- Uses publicly available API endpoints
- Respects rate limits and API terms
- No warranty or guarantee of data accuracy
- Users are responsible for compliance with applicable laws

---

## 🙏 Acknowledgments

- [Solscan](https://solscan.io/) for providing the API
- [Solana](https://solana.com/) blockchain ecosystem
- [Flask](https://flask.palletsprojects.com/) web framework
- [DataTables](https://datatables.net/) for interactive tables
- All open-source contributors

---

<div align="center">

**Developed by [Rafael Vieira (TechBeme)](https://github.com/TechBeme)**

[![GitHub](https://img.shields.io/badge/GitHub-TechBeme-181717?logo=github)](https://github.com/TechBeme)
[![Fiverr](https://img.shields.io/badge/Fiverr-Tech__Be-1DBF73?logo=fiverr)](https://www.fiverr.com/tech_be)
[![Upwork](https://img.shields.io/badge/Upwork-Profile-14a800?logo=upwork)](https://www.upwork.com/freelancers/~01f0abcf70bbd95376)
[![Email](https://img.shields.io/badge/Email-contact@techbe.me-EA4335?logo=gmail)](mailto:contact@techbe.me)

⭐ Star this repo if you find it useful!

</div>