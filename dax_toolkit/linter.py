"""Pragmatic DAX measure convention checks.

Not a full DAX parser — a set of regex-based heuristics covering the
conventions that matter most for keeping a growing Power BI model
readable and consistent across authors.
"""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class LintIssue:
    rule: str
    message: str


_MEASURE_NAME_RE = re.compile(r"^[A-Z][A-Za-z0-9 ]*$")
_MAGIC_NUMBER_RE = re.compile(r"(?<![\w.])(\d{2,})(?![\w])")
_ALLOWED_MAGIC_NUMBERS = {"100"}  # e.g. "* 100" for percentages is idiomatic


def lint_measure(name: str, expression: str) -> list[LintIssue]:
    issues: list[LintIssue] = []

    if not _MEASURE_NAME_RE.match(name):
        issues.append(
            LintIssue(
                rule="naming",
                message=f"measure name '{name}' should start with a capital letter and use spaces, not underscores",
            )
        )

    for match in _MAGIC_NUMBER_RE.finditer(expression):
        value = match.group(1)
        if value not in _ALLOWED_MAGIC_NUMBERS:
            issues.append(
                LintIssue(
                    rule="magic-number",
                    message=f"expression contains an unexplained literal '{value}'; consider a variable or a parameter table",
                )
            )

    if "VAR" not in expression.upper() and expression.count("CALCULATE") > 1:
        issues.append(
            LintIssue(
                rule="readability",
                message="multiple CALCULATE calls without VAR; consider naming intermediate results for readability",
            )
        )

    return issues
