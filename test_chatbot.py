import unittest

from chatbot import simple_chatbot, supported_queries


class ChatbotTests(unittest.TestCase):
    def test_supported_query_returns_microsoft_revenue(self):
        response = simple_chatbot("What was Microsoft's revenue in FY2025?")
        self.assertIn("$281,724 million", response)

    def test_query_matching_ignores_case_and_extra_spaces(self):
        response = simple_chatbot("  WHAT WAS APPLE'S NET MARGIN IN FY2025? ")
        self.assertIn("26.9%", response)

    def test_tesla_net_income_change(self):
        response = simple_chatbot(
            "How has Tesla's net income changed from FY2023 to FY2025?"
        )
        self.assertIn("decreased by $11,205 million", response)

    def test_highest_revenue(self):
        response = simple_chatbot("Which company had the highest revenue in FY2025?")
        self.assertIn("Apple", response)
        self.assertIn("$416,161 million", response)

    def test_comparison(self):
        response = simple_chatbot(
            "Compare FY2025 revenue for Apple, Microsoft, and Tesla."
        )
        self.assertIn("Apple: $416,161 million", response)
        self.assertIn("Microsoft: $281,724 million", response)
        self.assertIn("Tesla: $94,827 million", response)

    def test_unknown_query_is_explicit(self):
        response = simple_chatbot("What is the stock price?")
        self.assertIn("only answer the predefined queries", response)

    def test_five_queries_are_documented(self):
        self.assertEqual(len(supported_queries()), 5)


if __name__ == "__main__":
    unittest.main()
