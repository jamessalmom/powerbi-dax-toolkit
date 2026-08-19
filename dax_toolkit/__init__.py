"""dax_toolkit

A small linter for DAX measure naming/formatting conventions, plus a
curated, documented library of DAX snippets for the KPIs that come up
again and again in commercial/financial Power BI models: YTD, YoY,
Pareto client concentration, and row-level security (RLS) filters.

The linter doesn't parse full DAX grammar — it applies a handful of
pragmatic conventions (naming, no hardcoded literals in measures meant to
be reusable, explicit variable usage for readability) that keep a model
maintainable as it grows past a handful of measures.
"""

from .linter import LintIssue, lint_measure

__all__ = ["LintIssue", "lint_measure"]
__version__ = "0.1.0"
