## Описание

Примеры автотестов, реализованных на Python + Selenium с использованием Pytest

Для установки виртуального окружения необходимо выполнить:
```commandline
pip install -r requirements.txt
```
Для работы автотестов необходимо установить [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) (для браузера Chrome) и [geckodriver](https://github.com/mozilla/geckodriver/releases) (для браузера Firefox), соответствующие версиям используемых браузеров.

Автотесты по умолчанию запускаются для браузера Firefox, но с помощью аргумента `--browser_name` можно передать значение `chrome`.

При запуске автотестов в браузере Chrome на сайте ya.ru иногда требуется пройти капчу, поэтому тесты помечены, как `xfail`.

Поддерживается функция генерации `allure` отчетов.

[Инструкция](https://docs.qameta.io/allure/#_installing_a_commandline) по установке Allure.

[Инструкция](https://docs.qameta.io/allure/#_pytest) по интеграции с Pytest.

![image](https://github.com/Marina-Bokova/selenium_test_task/assets/115635748/4e35d6a6-f7f3-4f57-a286-458d01ae93b0)

![image](https://github.com/Marina-Bokova/selenium_test_task/assets/115635748/7fb89600-2b7f-47f3-b020-37173c4cee27)
