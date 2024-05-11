https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
инструкция для selenium
http://chromedriver.chromium.org/getting-started
https://www.guru99.com/selenium-tutorial.html — Туториал на английском, ориентирован на Java.
https://www.guru99.com/live-selenium-project.html — Можно попробовать писать автотесты для демо-сайта банка. Тоже Java.
http://barancev.github.io/good-locators/ — что такое хорошие селекторы
http://barancev.github.io/what-is-path-env-var/ — что за PATH переменная?

https://www.selenium.dev/documentation/webdriver/waits/
https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready
https://blog.codeship.com/get-selenium-to-wait-for-page-load/
http://barancev.github.io/slow-loading-pages/
http://barancev.github.io/page-loading-complete/

https://realpython.com/python-testing/ написание юнит-тестов в Python
https://habr.com/ru/post/358950/ Пирамида тестов на практике

Selenium WebDriver это — универсальный интерфейс, который позволяет манипулировать разными браузерами напрямую из кода на языке программирования.
важной для нас возможностью Selenium WebDriver — умению взаимодействовать с элементами веб-страницы.
Поиск с помощью CSS-селекторов, когда путь к элементу описывается через синтаксис CSS. Селектор — это описание пути к элементу на странице.
Поиск с помощью указания значений тегов или атрибутов элементов: ID, class, и т.д.
Поиск с помощью языка запросов XPath.
части элементов HTML-страницы, по которым можно найти элемент: id, tag, атрибут, name, class


mkdir environments
создание папки виртуального окружения

cd environments
открываем папку

py -m venv selenium_env
создание виртуального окружения

selenium_env\Scripts\activate.bat
активация виртуалки должна выводить имя в круглых скобках
запуск интерпретатора py или python

~/environments$ python ну или просто
py

поиск по id
"#bullet" поиск по имени в id
[id="bullet"]  по атрибуту
[name = "bullet-cat"] по нейм
.jumbotron-heading по классу или [class="jumbotron-heading"]
Псевдо-класс :nth-child(2) — позволяет найти второй по порядку элемент среди дочерних элементов

xpath
Символ / аналогичен символу > в CSS-селекторе, а символ // — пробелу.
el1/el2 — выбирает элементы el2, являющиеся прямыми потомками el1;
el1//el2 — выбирает элементы el2, являющиеся потомками el1 любой степени вложенности.

//img[@id='bullet'] фильтрация по имени
//div[@class="row"]/div[2] фильтрация по порядковому номеру
//p[text()="Lenin cat"] по полному совпадению текста
//div[contains(@class, "navbar")] по частичному совпадению текста
//img[@name='bullet-cat' and @data-type='animal'] булевы операции с несколькими условиями

//div/*[@class="jumbotron-heading"] * для выбора всех элементов когда не знаешь тег


"#" для id, "." для классов, [value="Cat memes"] для атрибутов
.card-body > p[data-type="description"] когда есть описание значения

Поиск элементов с помощью Selenium
find_element(By.ID, value) — поиск по уникальному атрибуту id элемента #
'#'id_value { style properties };  [id=id_value]
find_element(By.CSS_SELECTOR, value) — поиск элемента с помощью правил на основе CSS
requireds = browser.find_elements(By.CSS_SELECTOR, 'input[required]') поиск по аттрибуту
[attr~=value] одно из которых в точности равно value
[attr|=value] может быть или в точности равно "value" или может начинаться с "value" со сразу же следующим "-"
[attr$=value] заканчивается на "value"
[attr*=value] Обозначает элемент с именем атрибута attr чьё значение содержит по крайней мере одно вхождение строки "value" как подстроки


find_element(By.XPATH, value) — поиск с помощью языка запросов XPath //
find_element(By.NAME, value) — поиск по атрибуту name элемента
find_element(By.TAG_NAME, value) — поиск элемента по названию тега элемента
find_element(By.CLASS_NAME, value) — поиск по значению атрибута class; ..
find_element(By.LINK_TEXT, value) — поиск ссылки на странице по полному совпадению;
find_element(By.PARTIAL_LINK_TEXT, value) — поиск ссылки на странице, если текст селектора совпадает с любой частью текста

для поиска нескольких элементов find_elemens

Работа со списками класс select выбирает значение из выпадающего списка без необходимости лишнего нажатия
select_by_value(value): специальный класс Select из библиотеки WebDriver
select.select_by_visible_text("text") и select.select_by_index(index). Первый способ ищет элемент по видимому тексту, например, select.select_by_visible_text("Python") найдёт "Python" для нашего примера.
select.select_by_index(1) Второй способ ищет элемент по его индексу или порядковому номеру

execute_script позволяет выполнить скрипт прямо в консоли браузера
browser.execute_script("window.scrollBy(0, 100);") для прокрутки вниз на 100 пикселей
current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла
new_window = browser.window_handles[1]  # возвращает имя новой вкладки
browser.switch_to.window(window_name) # для переключения на новую вкладку

для реализации задержки используем time.sleep(), browser.implicitly_wait(5)


git-add - Добавить содержимое файла в индекс. добавления файла в список отслеживаемых

file:///C:/Program%20Files/Git/mingw64/share/doc/git-doc/git-add.html

