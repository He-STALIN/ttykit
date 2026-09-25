<div align="center">

# TTYKit

> **Helping made beautiful out in terminal**

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://python.org)
[![GitHub license](https://img.shields.io/github/license/He-STALIN/ttykit)](https://github.com/He-STALIN/ttykit/blob/main/LICENSE)
[![Repository](https://img.shields.io/badge/Repository-GitHub-4b93ff?style=flat&logo=github&logoColor=white)](https://github.com/He-STALIN/ttykit)
[![Downloads](https://img.shields.io/pypi/dm/ttykit)](https://pypi.org/project/ttykit/)

</div>

## This file is 2-lang
- [EN Version](#en)
- [RU Версия](#ru)


## EN
### For Start
- #### Automatic
    - exec `pip install ttykit`

- #### Manually
    - #### Dev version
        - clone repository
            ```bash
            git clone https://github.com/He-STALIN/ttykit.git
            ```

        - change to dir and exec
            ```bash
            pip install .
            ```

    - #### From Release
        - download any release from [Releases](https://github.com/He-STALIN/ttykit/releases)

        - exec in terminal
            ```bash
            pip install <path>
            ```
            where `<path>` you need write path to the downloaded release file

### support the project
- If you would like the project to continue developing, you can make a [donation](https://yoomoney.ru/to/4100118618732284/100).
- Account: `4100 1186 1873 2284` (YouMoney)
- or
- Find bugs in the library and report them in the [`issues` section on GitHub](https://github.com/He-STALIN/ttykit/issues).

### Code Examples
- #### Status
    ```python
    from ttykit import Status, TaskState

    with Status("Something unit", spinner="line") as status:
        ... # your payload
        status.set_state(TaskState.SUCCESS)
    ```

- #### Progress
    ```python
    from ttykit import Progress

    with Progress(100, "Some desc", 40) as progress:
        ... # your code
        progress.update(value)
        ... # your code again
        progress.finish()
    ```

- **for more code examples see** [CODE USE](https://github.com/He-STALIN/ttykit/blob/main/docs/en/CODE_USE.md)


### License
- This lib uploading with MIT License. [See License](https://github.com/He-STALIN/ttykit/blob/main/LICENSE)

### Versions
- You interesting see versions? You can see [CHANGELOG](https://github.com/He-STALIN/ttykit/blob/main/docs/en/CHANGELOG.md)


## RU
### Для начала использования
- #### Авто-установка
    - выполните `pip install ttykit` в терминале

- #### Вручную
    - #### Разрабатываемую версию
        - скопируйте репозиторий
            ```bash
            git clone https://github.com/He-STALIN/ttykit.git
            ```

        - перейдите в папку и выполни
            ```bash
            pip install .
            ```
    - #### Релизную версию
        - Скачайте любой релиз из вкладки ["Releases"](https://github.com/He-STALIN/ttykit/releases)

        - выполните в терминале
            ```bash
            pip install <path>
            ```
            Где `<path>` вам нужно вставить путь к скачанному файлу релиза


### Поддержите проект
- Если вы желаете, чтобы проект разрабатывался дальше, вы можете сделать [пожертвование](https://yoomoney.ru/to/4100118618732284/100).
- Счет: `4100 1186 1873 2284` (ЮМани)
- или
- Ищите ошибки в библиотеке и сообщайте о них в [`issues` на GitHub](https://github.com/He-STALIN/ttykit/issues).


### Примеры кода
- #### Status класс
    ```python
    from ttykit import Status, TaskState

    with Status("Какая-то задача", spinner="line") as status:
        ... # ваша нагрузка
        status.set_state(TaskState.SUCCESS)
    ```

- #### Progress класс
    ```python
    from ttykit import Progress

    with Progress(100, "Некоторое описание", 40) as progress:
        ... # ваш код
        progress.update(value)
        ... # и снова ваш код
        progress.finish()
    ```

- **Для большего количества примеров и описания смотрите** [CODE USE](https://github.com/He-STALIN/ttykit/blob/main/docs/ru/CODE_USE.md)


### Лицензия
- Это библиотека распространяется под лицензией MIT. [Смотреть лицензию](https://github.com/He-STALIN/ttykit/blob/main/LICENSE)

### Версии
- вам интересно узнать про версии? Вы можете посмотреть [CHANGELOG](https://github.com/He-STALIN/ttykit/blob/main/docs/ru/CHANGELOG.md)


---
<div align="center">

*ttykit by He_STALIN. All rights reserved*

</div>