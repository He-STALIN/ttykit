<div align="center">

# TTYKit

> **Helping made beautiful out in terminal**

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![GitHub license](https://img.shields.io/github/license/He-STALIN/ttykit)](LICENSE)
[![Repository](https://img.shields.io/badge/Repository-GitHub-4b93ff?style=flat&logo=github&logoColor=white)](https://github.com/He-STALIN/ttykit)
[![Downloads](https://img.shields.io/pypi/dm/ttykit)](https://pypi.org/project/ttykit/)

</div>

---

## Для начала
### В ручную:
- Скопируй репозиторий
    ```bash
    git clone https://github.com/He-STALIN/ttykit.git
    ```

- Перейди в директорию и выполни
    ```bash
    pip install .
    ```
### Автоматически
- выполни `pip install ttykit`

- и используй в своих проектах!

## Поддержать проект
- если вы хотите, чтобы проект развивался дальше, то можете сделать [пожертвование](https://yoomoney.ru/to/4100118618732284/100)
- Счет: `4100 1186 1873 2284` (ЮМани)
- или же
- находите ошибки в работе библиотеки и сообщайте о них в `issues`


## Примеры кода

- ### `Status`
    ```python
    from ttykit import Status, TaskState

    with Status("Something unit", spinner="line") as status:
        <some action>
        status.set_state(TaskState.SUCCESS)
    ```

- ### `Progress`
    ```python
    from ttykit import Progress

    with Progress(100, "Some desc", 40) as progress:
        <some action>
        progress.update(<value>)
        <some action again>
        progress.finish()
    ```

- **для большего количества примеров смотри** [CODE USE](/docs/ru/CODE_USE.md)

## Лицензия
- Эта библиотека распространяется под лицензией MIT. [Смотреть лицензию](/LICENSE)

## Версии
- Интересно посмотреть на список версий? Вы можете посмотреть в [Логе обновлений](/docs/ru/CHANGELOG.md)

---
<div align="center">

*ttykit от He_STALIN. Все права защищены*

</div>