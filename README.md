# Gotcha 🧯

![Last Commit](https://img.shields.io/github/last-commit/xaviermontane/gotcha)
![License](https://img.shields.io/github/license/xaviermontane/gotcha)

Help everyday users identify likely burner/sockpuppet accounts on Twitter, Reddit, Discord, etc.—friends, bots, or harassment campaigns.

__Gotcha is:__

- A deep OSINT-based behavioural analysis tool
- Built for non-technical users, but with power-user capabilities
- Designed to detect burner/sockpuppet or malicious alt accounts

## 🎯 What Problem Does Gotcha Solve?

In today's digital landscape, fake accounts are everywhere. Whether it's coordinated harassment campaigns, bot networks spreading misinformation, or individuals creating multiple personas to manipulate conversations, identifying these accounts manually is time-consuming and requires specialized knowledge.

Gotcha bridges this gap by providing sophisticated account analysis capabilities in an accessible interface that anyone can use.

## 🔍 Key Features

- Core Analysis Capabilities
- __Behavioral Pattern Detection:__ Identifies unusual posting patterns, timing anomalies, and engagement metrics
- __Cross-Platform Correlation:__ Links suspicious accounts across multiple social media platforms
- __Network Analysis:__ Maps connections between potentially related accounts
- __Content Analysis:__ Examines writing style, language patterns, and content similarity
- __Timeline Forensics:__ Analyzes account creation dates, activity gaps, and posting schedules

## Getting Started

### Prerequisites

- Python 3.9 or later
- `pyenv` (optional, for managing Python versions)

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/xaviermontane/gotcha.git
   cd gotcha
   ```

2. Set up the Python environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Run the CLI:

   ```bash
   python core.py --help
   ```

---

## Usage

### Example Command

```bash
python cli.py scan @user1
```

This will scan the provided social media handles and output a summary.

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Submit a pull request.

---

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.
