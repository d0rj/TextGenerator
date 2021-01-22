# Argument Generator

## Description

Простое консольное приложение для генерации текста из шаблонов, умеющее изменять форму слова. Частный случай применения - генерация аргументов против X, за Y и т.д.; для чего, собственно, и делалось.

## Usage

Установить зависимости:

```shell
pip install pymorphy2
```

*Для справки*:

```shell
python main.py -h
```

Пример использования:

```shell
python main.py -X=слово --file './path/to/template.txt'
```

## Templates

Для примера используется знаменитый [аргумент](https://www.youtube.com/watch?v=WsFP8If0TbI&ab_channel=%5B99%D0%BC%D1%8B%D1%81%D0%BB%D0%B5%D0%B9%5DZvonov) мистера П.Звонова, работающий против любого X.

## Warning

**Works only with russian and ukranian arguments**.
