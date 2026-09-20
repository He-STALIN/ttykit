<div align="center">

# TTYKit

> **Helping made beautiful out in terminal**

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![GitHub license](https://img.shields.io/github/license/He-STALIN/ttykit)](LICENSE)
[![Repository](https://img.shields.io/badge/Repository-GitHub-4b93ff?style=flat&logo=github&logoColor=white)](https://github.com/He-STALIN/ttykit)
[![Downloads](https://img.shields.io/pypi/dm/ttykit)](https://pypi.org/project/ttykit/)

</div>

##### Вы из России? Смотрите [русскую версию](/docs/ru/README.ru.md)

---

## For Start
### Manually:
- Clone repository
    ```bash
    git clone https://github.com/He-STALIN/ttykit.git
    ```

- Change dir and exec
    ```bash
    pip install .
    ```
### Auto
- exec `pip install ttykit`

- And use in your projects!

## Support the project
- If you would like the project to continue developing, you can make a [donation](https://yoomoney.ru/to/4100118618732284/100).
- Account: `4100 1186 1873 2284` (YouMoney)
- or
- Find bugs in the library and report them in the `issues` section on GitHub.

## Code Examples

- ### Status
    ```python
    from ttykit import Status, TaskState

    with Status("Something unit", spinner="line") as status:
        <some action>
        status.set_state(TaskState.SUCCESS)
    ```

- ### Progress
    ```python
    from ttykit import Progress

    with Progress(100, "Some desc", 40) as progress:
        <some action>
        progress.update(<value>)
        <some action again>
        progress.finish()
    ```

- **for more code examples see** [CODE USE](docs/en/CODE_USE.md)

## Also
- also you can use prepared colors in this lib

## License
- This lib uploading with MIT License. [See License](LICENSE)

## Versions
- You interesting see versions? You can see [CHANGELOG](docs/en/CHANGELOG.md)

---
<div align="center">

*ttykit by He_STALIN. All right reserved*

</div>