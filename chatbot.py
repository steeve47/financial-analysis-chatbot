"""Predefined-query financial chatbot prototype.

The values are taken from the FY2023-FY2025 financial trend analysis included
with this project. Dollar amounts are in USD millions.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List


DATA_FILE = Path(__file__).with_name("financial_data.csv")


def load_data() -> List[Dict[str, str]]:
    """Load the small analyzed dataset shipped with the prototype."""
    with DATA_FILE.open(newline="", encoding="utf-8") as data_file:
        return list(csv.DictReader(data_file))


DATA = load_data()


def _row(company: str, fiscal_year: str) -> Dict[str, str]:
    for record in DATA:
        if record["Company"] == company and record["Fiscal Year"] == fiscal_year:
            return record
    raise ValueError(f"No data found for {company} {fiscal_year}.")


def _money_millions(value: str) -> str:
    return f"${int(value):,} million"


def supported_queries() -> List[str]:
    """Return the five queries supported by the prototype."""
    return [
        "What was Microsoft's revenue in FY2025?",
        "How has Tesla's net income changed from FY2023 to FY2025?",
        "Which company had the highest revenue in FY2025?",
        "What was Apple's net margin in FY2025?",
        "Compare FY2025 revenue for Apple, Microsoft, and Tesla.",
    ]


def simple_chatbot(user_query: str) -> str:
    """Return a canned response for one of the supported financial queries."""
    query = " ".join(user_query.strip().lower().split())

    if query == "what was microsoft's revenue in fy2025?":
        revenue = _row("Microsoft", "FY2025")["Total Revenue ($M)"]
        return f"Microsoft's FY2025 revenue was {_money_millions(revenue)}."
    elif query == "how has tesla's net income changed from fy2023 to fy2025?":
        start = int(_row("Tesla", "FY2023")["Net Income ($M)"])
        end = int(_row("Tesla", "FY2025")["Net Income ($M)"])
        change = end - start
        return (
            f"Tesla's net income decreased by {_money_millions(str(abs(change)))} "
            f"from FY2023 ({_money_millions(str(start))}) to FY2025 "
            f"({_money_millions(str(end))})."
        )
    elif query == "which company had the highest revenue in fy2025?":
        fy2025 = [record for record in DATA if record["Fiscal Year"] == "FY2025"]
        highest = max(fy2025, key=lambda record: int(record["Total Revenue ($M)"]))
        return (
            f"{highest['Company']} had the highest FY2025 revenue at "
            f"{_money_millions(highest['Total Revenue ($M)'])}."
        )
    elif query == "what was apple's net margin in fy2025?":
        margin = _row("Apple", "FY2025")["Net Margin (%)"]
        return f"Apple's FY2025 net margin was {margin}%."
    elif query == "compare fy2025 revenue for apple, microsoft, and tesla.":
        values = [
            f"{company}: {_money_millions(_row(company, 'FY2025')['Total Revenue ($M)'])}"
            for company in ("Apple", "Microsoft", "Tesla")
        ]
        return "FY2025 revenue comparison — " + "; ".join(values) + "."
    else:
        return (
            "Sorry, I can only answer the predefined queries. "
            "Ask 'help' to see the supported questions."
        )


def run_cli() -> None:
    """Run an interactive command-line session."""
    print("Financial Analysis Chatbot")
    print("Type 'help' to list supported queries or 'quit' to exit.")
    while True:
        user_query = input("\nYou: ").strip()
        if user_query.lower() in {"quit", "exit"}:
            print("Bot: Goodbye.")
            return
        if user_query.lower() == "help":
            print("Bot: You can ask:")
            for query in supported_queries():
                print(f"- {query}")
            continue
        print(f"Bot: {simple_chatbot(user_query)}")


if __name__ == "__main__":
    run_cli()
