from pathlib import Path
import tempfile
import unittest
from aurelis_open_core.funding_runner import FundingRunner, FundingTarget

class FundingRunnerTests(unittest.TestCase):
    def test_rank_is_deterministic(self):
        with tempfile.TemporaryDirectory() as d:
            runner = FundingRunner(d)
            a = FundingTarget("A", "A", "https://a", "1", None, 90, (), "x")
            b = FundingTarget("B", "B", "https://b", "1", None, 95, (), "x")
            self.assertEqual([x.id for x in runner.rank([a, b])], ["B", "A"])

    def test_plan_and_queue_are_written(self):
        with tempfile.TemporaryDirectory() as d:
            runner = FundingRunner(d)
            t = FundingTarget("A", "A", "https://a", "1", None, 90, ("https://a",), "x")
            plan = runner.write_plan([t])
            queue = runner.write_operator_queue([t])
            self.assertTrue(Path(plan).exists())
            self.assertTrue(Path(queue).exists())

if __name__ == "__main__":
    unittest.main()
