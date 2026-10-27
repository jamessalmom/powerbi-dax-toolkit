# powerbi-dax-toolkit

A small linter for DAX measure conventions, plus a few documented DAX snippets for KPIs that appear in most commercial and financial Power BI models: YTD, year-over-year variation, Pareto client concentration and row-level security.

It pairs with [sql-kpi-toolkit](https://github.com/jamessalmom/sql-kpi-toolkit), for when the same calculation belongs in the semantic model instead of (or as well as) the source query.

## The linter

It does not parse DAX. It runs a handful of checks that help a model stay readable once several people are adding measures to it:

- measure names in `Title Case With Spaces`, not `snake_case`;
- no unexplained numeric literals inside an expression (a bare `> 100`); move them to a variable or a parameter;
- measures with several `CALCULATE` calls should name intermediate results with `VAR`.

```python
from dax_toolkit import lint_measure

issues = lint_measure("Revenue_YTD", "TOTALYTD(SUM(Sales[Amount]), 'Date'[Date])")
for issue in issues:
    print(issue.rule, "-", issue.message)
# naming - measure name 'Revenue_YTD' should start with a capital letter and use spaces, not underscores
```

## Snippets

| File | Pattern |
|---|---|
| `dax_toolkit/snippets/ytd_and_yoy.dax` | Year-to-date and year-over-year variation |
| `dax_toolkit/snippets/pareto_concentration.dax` | Cumulative revenue share per client, ranked |
| `dax_toolkit/snippets/rls_filters.dax` | Row-level security through an access/bridge table |

## Development

```bash
pip install pytest ruff
pytest
ruff check .
```

## License

MIT, see [LICENSE](LICENSE).
