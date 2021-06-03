# Проекты, реализованные в ходе обучения в Яндекс.Практикуме по специализации “Аналитик данных”

| Название проекта                                                                               | Используемые инструменты                                                                                                                                       | Задачи проекта                                                                                                                                                                            | Описание проекта                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Исследование надёжности заёмщиков — анализ банковских данных                                | Pandas, PyMystem3, Python, лемматизация, предобработка данных                                                                                                  | На основе статистики о платёжеспособности клиентов исследовать влияет ли семейное положение и количество детей клиента на факт возврата кредита в срок                                    | На основе данных кредитного отдела банка исследовал влияние семейного положения иколичества детей на факт погашения кредита в срок. Была получена информация оданных. Определены и обработаны пропуски. Заменены типы данных на соответствующиехранящимся данным. Удалены дубликаты. Выделены леммы в значениях столбца икатегоризированны данные.                                                                                                                                                                                         |
| 2. Продажа квартир в Санкт-Петербурге — анализ рынка недвижимости                              | Matplotlib, Pandas, Python, визуализация данных, исследовательский анализ данных, предобработка данных                                                         | Используя данные сервиса Яндекс.Недвижимость, определить рыночную стоимость объектов недвижимости и типичные параметры квартир                                                            | На основе данных сервиса Яндекс.Недвижимость определена рыночная стоимостьобъектов недвижимости разного типа, типичные параметры квартир, в зависимости отудаленности от центра. Проведена предобработка данных. Добавлены новые данные.Построены гистограммы, боксплоты, диаграммы рассеивания.                                                                                                                                                                                                                                           |
| 3. Определение выгодного тарифа для телеком компании                                           | Matplotlib, NumPy, Pandas, Python, SciPy, описательная статистика, проверка статистических гипотез                                                             | На основе данных клиентов оператора сотовой связи проанализировать поведение клиентов и поиск оптимального тарифа                                                                         | Проведен предварительный анализ использования тарифов на выборке клиентов,проанализировано поведение клиентов при использовании услуг оператора ирекомендованы оптимальные наборы услуг для пользователей. Проведена предобработкаданных, их анализ. Проверены гипотезы о различии выручки абонентов разных тарифов иразличии выручки абонентов из Москвы и других регионов.                                                                                                                                                               |
| 4. Изучение закономерностей, определяющих успешность игр                                       | Matplotlib, NumPy, Pandas, Python, исследовательский анализ данных, описательная статистика, предобработка данных, проверка статистических гипотез             | Используя исторические данные о продажах компьютерных игр, оценки пользователей и экспертов, жанры и платформы, выявить закономерности, определяющие успешность игры                      | Выявлены параметры, определяющие успешность игры в разных регионах мира. Наосновании этого подготовлен отчет для магазина компьютерных игр для планированиярекламных кампаний. Проведена предобработка данных, анализ. Выбран актуальныйпериод для анализа. Составлены портреты пользователей каждого региона. Провереныгипотезы: средние пользовательские рейтинги платформ Xbox One и PC одинаковые;средние пользовательские рейтинги жанров Action и Sports разные. При анализе использовал критерий Стьюдента для независимых выборок. |
| 5. Исследование данных авиакомпании — проверить гипотезу о повышенииспроса во время фестивалей | Matplotlib, Pandas, Python, SQL, SciPy, проверка статистических гипотез                                                                                        | Произвести выгрузки и подготовку данных авиакомпаний с помощью SQL, проверить гипотезу о различии среднего спроса на билеты во время различных событий                                    | Проведена выгрузка и подготовка предоставленных данных авиакомпании средствами SQL. Проверена гипотеза о различии среднего спроса на билеты во время проведенияразличных фестивалей и в обычное время .                                                                                                                                                                                                                                                                                                                                    |
| 6. Оптимизация маркетинговых затрат в Яндекс.Афише                                             | Matplotlib, Pandas, Python, когортный анализ, продуктовые метрики, юнит-экономика                                                                              | На основе данных о посещениях сайта Яндекс.Афиши изучить, как люди пользуются продуктом, когда они начинают покупать, сколько денег приносит каждый клиент, когда он окупается            | Проведен анализ данных от Яндекс.Афиши целью оптимизации маркетинговых затрат.Рассчитаны метрики LTV, CAC, Retention rate, DAU, WAU, MAU, ROMI                                                                                                                                                                                                                                                                                                                                                                                             |
| 7. Проверка гипотез по увеличению выручки в интернет-магазине —оценить результаты A/B теста    | A/B-тестирование, Matplotlib, Pandas, Python, SciPy, проверка статистических гипотез                                                                           | Используя данные интернет-магазина приоритезировать гипотезы, произвести оценку результатов A/B-тестирования различными методами                                                          | Проведена приоритизация гипотез по фреймворкам ICE и RICE. Затем провел анализрезультатов A/B-теста, построил графики кумулятивной выручки, среднего чека,конверсии по группам, а затем посчитал статистическую значимость различий конверсийи средних чеков по сырым и очищенным данным. На основании анализа мной былопринято решение о нецелесообразности дальнейшего проведения теста.                                                                                                                                                 |
| 8. Исследования рынка общепита в Москве для принятия решения оботкрытии нового заведения       | Pandas, Plotly, Python, Seaborn, визуализация данных                                                                                                           | Исследование рынка общественного питания на основе открытых данных, подготовка презентации для инвесторов                                                                                 | Мною был исследован вопрос - будет ли успешным и популярным на долгое время кафе, вкотором гостей обслуживают роботы-официанты. По результатам анализа подготовленапрезентация для инвесторов с рекомендациями. В построении графиков я использовалибиблиотеки seaborn и plotly. Также мне потребовалось получить район расположениякафе-конкурентов. Эту задачу я решил, подключившись к API Яндекс.Геокодербиблиотекой requests                                                                                                          |
| 9. Анализ пользовательского поведения в мобильном приложении                                   | A/B-тестирование, Matplotlib, Pandas, Plotly, Python, Seaborn, визуализация данных, проверка статистических гипотез, продуктовые метрики, событийная аналитика | На основе данных использования мобильного приложения для продажи продуктов питания проанализировать воронку продаж, а также оценить результаты A/A/B-тестирования                         | В данном проекте мной были изучены принципы событийной аналитики. Я построилворонку продаж, исследовал путь пользователей до покупки. Проанализировалрезультаты A/B-теста введения новых шрифтов. Сравнил 2 контрольных группы междусобой, убедился в правильном разделении трафика, а затем сравнил с тестовой группойВыявлено, что новый шрифт значительно не повлияет на поведение пользователей.                                                                                                                                       |
| 10. Создание дашборда по пользовательским событиям для агрегаторановостей                      | PostgreSQL, Python, SQLAlchemy, Tableau, dash, построение дашбордов, продуктовые метрики                                                                       | Используя данные Яндекс.Дзена построить дашборд с метриками взаимодействия пользователей с карточками статей                                                                              | Работу над этим проектом я провел на удаленной машине в сервисе Yandex.Cloud. Мнойбыл установлен PostgreSQL, развернута база данных. Затем я написал скрипт пайплайна,который позволил собирать данные за определенный временной период, и настроил егоавтономную работу через crontab. Для визуализации собранных данных я написал скриптдашборда с несколькими фильтрами и также запустил его на удаленной машине. Порезультатам была подготовлена презентация с полученными графиками                                                   |
