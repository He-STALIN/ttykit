<div align="center">

# TTYKit

> **Helping made beautiful out in terminal**

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![GitHub license](https://img.shields.io/github/license/He-STALIN/ttykit)](LICENSE)
[![Repository](https://img.shields.io/badge/Repository-GitHub-4b93ff?style=flat&logo=github&logoColor=white)](https://github.com/He-STALIN/ttykit)

</div>
---

## 📦 For Start

```bash
git clone https://github.com/He-STALIN/ttykit.git
```

- Change dir and exec
```bash
pip install .
```

- And use in your projects!

## License
- This lib uploading with MIT License [See License](LICENSE)

## Code Examples

### Status
```python
from ttykit import Status, TaskState

with Status("Something unit", spinner="line") as status:
    <some action>
    status.set_state(TaskState.SUCCESS)
```

### Progress
```python
from ttykit import Progress

with Progress(100, "Some desc", 40) as progress:
    <some action>
    progress.update(<value>)
    <some action again>
    progress.finish()
```
or
```python
with Progress(100, "Some desc", 40) as progress:
    while not progress.finished:
        <some actions>
        progress.advance(<step>)
        <maybe action again>
```

## Also
- also you can use prepared colors in this lib