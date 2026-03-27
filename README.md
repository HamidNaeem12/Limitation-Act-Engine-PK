# ⚖️ Legal Limitation Calculator

A web-based reference tool for Pakistani legal practitioners to calculate filing deadlines under the **Limitation Act, 1908**. Built with Python and Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app.streamlit.app)

---

## Overview

Calculating limitation deadlines accurately is critical in legal practice. This tool helps practitioners determine the final filing deadline for common case types by applying the statutory period from the First Schedule of the Limitation Act, 1908, along with the Section 12 exclusion for time spent obtaining certified copies.

**Supported case types:**

| Case Type | Statutory Period | Source |
|---|---|---|
| Civil Suit (General) | 3 years (1,095 days) | First Schedule, Article 120 |
| First Appeal (Civil) | 30 days | First Schedule, Article 156 |
| Civil Revision | 90 days | First Schedule, Article 163 |
| Criminal Appeal (High Court) | 60 days | Cr.P.C Section 417 |
| Death Sentence Appeal | 7 days | Cr.P.C Section 410 |

---

## Features

- Instant deadline calculation based on order/decree date
- Section 12 exclusion for certified copy procurement days
- Clear status indicators: days remaining, due today, or time-barred
- Statutory source reference displayed for each case type
- Input validation to prevent erroneous date entries

---

## Running Locally

### Prerequisites

- Python 3.9 or higher
- pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/limitation-calculator.git
cd limitation-calculator
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run limitation_calculator.py
```

4. Open your browser and navigate to `http://localhost:8501`

---

## Project Structure

```
limitation-calculator/
├── limitation_calculator.py   # Main application
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Contributing

Contributions are welcome. To propose a change:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add: description of change"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request with a clear description of the change

Please ensure any additions remain consistent with the Limitation Act, 1908, and include the relevant statutory reference for any new case types.

---

## Legal Disclaimer

This tool is intended for **reference purposes only** and does not constitute legal advice. Limitation periods may be affected by court holidays, condonation of delay orders, jurisdiction-specific rules, and other legal factors not captured by this tool.

Always verify deadlines independently and consult a qualified legal practitioner before taking or refraining from any legal action. The authors accept no liability for reliance on the output of this tool.

---

## License

This project is open source. See `LICENSE` for details.
