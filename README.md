# powerbi-dax-toolkit

A small **DAX convention linter** plus a curated, documented library of
DAX snippets for the KPIs that show up in nearly every commercial/
financial Power BI model: YTD, YoY variation, Pareto 80/20 client
concentration, and row-level security (RLS) filters.

Companion to [`sql-kpi-toolkit`](../sql-kpi-toolkit) for when the same
calculation belongs in the semantic model instead of (or in addition to)
the source query.

## The linter

Not a full DAX parser — a handful of pragmatic checks that keep a model
maintainable as more people add measures to it:

- measure names are `Title Case With Spaces`, not `snake_case`
- no unexplained numeric literals buried in an expression (`> 100` with
  no comment) — surface them as a parameter or a named variable instead
- multiple `CALCULATE` calls in one measure should use `VAR` to name
  intermediate results

```python
from dax_toolkit import lint_measure

issues = lint_measure("Revenue_YTD", "TOTALYTD(SUM(Sales[Amount]), 'Date'[Date])")
for issue in issues:
    print(issue.rule, "-", issue.message)
```

## Snippets

| File | Pattern |
|---|---|
| `snippets/ytd_and_yoy.dax` | Year-to-date + year-over-year variation |
| `snippets/pareto_concentration.dax` | Ranked cumulative revenue share per client |
| `snippets/rls_filters.dax` | Row-level security via a bridge/access table |

## Development

```bash
pip install pytest ruff
pytest
ruff check .
```

## License

MIT — see [LICENSE](LICENSE).
