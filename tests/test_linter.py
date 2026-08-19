from dax_toolkit.linter import lint_measure


def test_flags_underscore_measure_names():
    issues = lint_measure("Revenue_YTD", "TOTALYTD(SUM(Sales[Amount]), 'Date'[Date])")
    assert any(i.rule == "naming" for i in issues)


def test_accepts_well_formed_name():
    issues = lint_measure("Revenue YTD", "TOTALYTD(SUM(Sales[Amount]), 'Date'[Date])")
    assert not any(i.rule == "naming" for i in issues)


def test_flags_unexplained_magic_number():
    issues = lint_measure("Late Orders", "CALCULATE(COUNTROWS(Orders), Orders[DaysLate] > 15)")
    assert any(i.rule == "magic-number" for i in issues)


def test_allows_percentage_literal_100():
    issues = lint_measure("Attainment Pct", "DIVIDE([Actual],[Goal]) * 100")
    assert not any(i.rule == "magic-number" for i in issues)


def test_flags_multiple_calculate_without_var():
    expr = "CALCULATE(SUM(Sales[Amount])) - CALCULATE(SUM(Sales[Amount]), SAMEPERIODLASTYEAR('Date'[Date]))"
    issues = lint_measure("Revenue Delta", expr)
    assert any(i.rule == "readability" for i in issues)
