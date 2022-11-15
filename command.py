import math
import os
import sys

import click

from main import app


@app.cli.command("test")
@click.option(
    "--with_dir",
    default=None,
    help="Run test from specific folder. Example: tests/controllers/probe",
)
def test(with_dir):
    import unittest

    import coverage

    COV = coverage.coverage(config_file=".coveragerc")
    COV.start()

    if with_dir:
        tests = unittest.TestLoader().discover(with_dir)
    else:
        tests = unittest.TestLoader().discover("tests")

    test_results = unittest.TextTestRunner(verbosity=2).run(tests)

    if int(os.environ.get("FLASK_COVERAGE")) == 1:
        COV.stop()
        COV.save()
        print("Coverage summary: ")
        cov_percentage = COV.report()
        COV.html_report()
        print(cov_percentage)

        if (
            len(test_results.failures) == len(test_results.errors) == 0
            and math.floor(cov_percentage) >= 80
        ):
            return sys.exit(0)
        else:
            return sys.exit(1)
    else:
        print(
            "*Note: Set FLASK_COVERAGE=1 in .env to generate coverage report and HTML"
        )
