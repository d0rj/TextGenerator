# Argument Generator

⚠️ Work in progress! ⚠️

## Описание

Простое консольное приложение для генерации текста из шаблонов (шаблонизатор), умеющее изменять форму слова. Частный случай применения - генерация аргументов против X, за Y и т.д.; для чего, собственно, и делалось.

## Использование

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
python main.py -v X=слово --variable Y=ворота -v ALPHA=альфа --file './path/to/template.txt'
```

Этот вызов для шаблона *./path/to/template.txt* заменит все переменные нужными значениями (**X** на формы слова ***слово***, **Y** - на ***ворота***, а **ALPHA** - на ***альфа***), если все переменные шаблона содержатся в переданных аргументах. 

Иначе, если в шаблоне нашлась **неизвестная переменная**, по умолчанию программа завершится с ошибкой, указывая на первую не найденную переменную. Чтобы этого избежать, необходимо указать флаг *-i* или *--ignore-unknown*. В таком случае шаблонизатор будет просто игнорировать неизвестные переменные.

### Аргументы программы

* **-f** / **--file** - Входной файл с шаблоном;
* **-v** / **--variable** - Добавляет в список переменных значение. Может применяться несколько раз. Аргумент должен выглядеть как X=слово, где X - любое название вашей переменной;
* **-i** / **--ignore-unknown** - Этот флаг указывает: игнорировать ли неизвестные переменные в шаблоне (если True), или выбрасывать исключение в ином случае. По умолчанию False;
* **-o** / **--output** - Файл для вывода результата. Опционально. Если не указано, то вывод будет в стандартном потоке (консоли).

## Шаблоны

### Создание шаблонов

Общий формат таков: **[ X | form ]**. Программа заменит такую запись на подходящую, основываясь на **form**.

#### **Переменные**

Название переменной должно соответствовать правилам:

*  Переменные состоят из прописных букв латинского алфавита, символа подчёркивания '**_**' и тире '**-**'.

Допускается передача в аргументах "лишних" переменных.

#### **Обработка слова**

На месте **form** может быть одна из строк, представляющих формы слов, соответствующая таблице:

Используемая строка | Форма слова | Пояснение | Пример
------------------- | ----------- | --------- | ------
*пустая строка* |  | то же, что и **именительный** падеж |
**about** |  | **предложный** падеж, но с подходящим предлогом *о/об* | об интернете / о матче
**nomn** | именительный | Кто? Что? | хомяк ест
**gent** | родительный | Кого? Чего? | у нас нету хомяка
**datv** | дательный | Кому? Чему? | сказать хомяку спасибо
**accs** | винительный | Кого? Что? | хомяк читает книгу
**ablt** | творительный | Кем? Чем? | зерно съедено хомяком
**loct** | предложный | О ком? О чём? и т.п. | хомяка несут в корзинке
**voct** | звательный | Его формы используются при обращении к человеку. | Саш, пойдём в кино.
**gen2** | второй родительный (частичный) |  | ложка сахару (gent - производство сахара); стакан яду (gent - нет яда)
**acc2** | второй винительный |  | записался в солдаты
**loc2** | второй предложный (местный) |  | я у него в долгу (loct - напоминать о долге); висит в шкафу (loct - монолог о шкафе); весь в снегу (loct - писать о снеге)

[Оригинальная таблица](https://pymorphy2.readthedocs.io/en/stable/user/grammemes.html#russian-cases)

### Пример

При **X** = **кот** и **Y** = **молоко**:

* Выражение **[X|nomn]овасия**, **[X|]овасия** или **[X]овасия** будет заменено на **котовасия**;

* Выражение **[X|form]** может иметь между словами сколько угодно пробелов, к примеру **[  X |form      ]**. Разницы после обработки не будет;

* **[Y] для [X | gent]** будет заменено на **молоко для кота**.

Для тестов по умолчанию используется знаменитый [аргумент](https://www.youtube.com/watch?v=WsFP8If0TbI&ab_channel=%5B99%D0%BC%D1%8B%D1%81%D0%BB%D0%B5%D0%B9%5DZvonov) мистера П.Звонова, работающий против любого X и за любой Y.

## Warning

**Works only with russian and ukranian arguments**.
