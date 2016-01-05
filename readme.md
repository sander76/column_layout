# MkDocs Three column layout

Uses the 12 column bootstrap layout to create responsive columns.
You can create a 2 or 3 column layout.

## Syntax
```
%1 **column1** %5 **column2** %6 **column3 (optional)**
```

Restrictions:

- Each column can have a width between 1 and 9
- Total column width should add up to 12

## Installation:

```
python setup.py install
```

In your ```mkdocs.yml``` file:

```markdown
markdown_extensions:
  - three_columns
```