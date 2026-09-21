# Financial Analysis Chatbot

A small, dependency-free Python chatbot prototype that answers five predefined
questions about Microsoft, Apple, and Tesla financial trends from FY2023
through FY2025.

The project includes both an interactive command-line interface and a
standalone browser demo. It is intentionally rule-based and educational; it
does not use an external AI service or live market data.

## Features

- Answers five predefined financial questions.
- Normalizes capitalization and extra whitespace in user input.
- Provides explicit responses for unsupported questions.
- Includes an interactive command-line interface.
- Includes a browser-only demo that runs without a server or build step.
- Includes automated tests and GitHub Actions CI.

## Quick start

### Command line

Requires Python 3.10 or newer.

```bash
python chatbot.py
```

Then type `help` to display the supported questions or `quit` to exit.

### Browser demo

Open [`chatbot_demo.html`](chatbot_demo.html) directly in a browser. Select a
suggested question or type one of the supported questions and choose **Ask**.
No installation or web server is required.

## Supported questions

1. What was Microsoft's revenue in FY2025?
2. How has Tesla's net income changed from FY2023 to FY2025?
3. Which company had the highest revenue in FY2025?
4. What was Apple's net margin in FY2025?
5. Compare FY2025 revenue for Apple, Microsoft, and Tesla.

## Project layout

| File | Description |
| --- | --- |
| [`chatbot.py`](chatbot.py) | Chatbot logic and interactive CLI |
| [`chatbot_demo.html`](chatbot_demo.html) | Standalone browser demonstration |
| [`financial_data.csv`](financial_data.csv) | Analyzed figures in USD millions |
| [`test_chatbot.py`](test_chatbot.py) | Automated unit tests |
| [`Financial_Trend_Analysis.html`](Financial_Trend_Analysis.html) | Exported financial trend analysis |

## Testing

Run the test suite from the project directory:

```bash
python -m unittest discover -v
```

## Data and limitations

- The dataset covers only Apple, Microsoft, and Tesla for FY2023–FY2025.
- Monetary values are expressed in USD millions.
- Responses are generated from the included CSV and are not retrieved live
  from the SEC, company filings, or market-data providers.
- Fiscal year-end dates differ between companies, so cross-company comparisons
  are directional rather than same-period quarterly comparisons.
- This educational prototype is not investment advice.

## Contributing

Improvements are welcome. Please keep the prototype dependency-free unless a
new dependency is necessary, add or update tests for behavior changes, and run
the test command before opening a pull request.

## License

This project is available under the [MIT License](LICENSE).
