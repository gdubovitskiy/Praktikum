# Создание дашборда по пользовательским событиям для агрегаторановостей

## Задача

Используя данные Яндекс.Дзена построить дашборд с метриками взаимодействия пользователей с карточками статей.

## Данные

Таблица `dash_visits`:
* *record_id* — id пользователя
* *item_topic* — тема карточки
* *source_topic* — тема источника
* *age_segment* — возраст (разделен по категориям)
* *dt* — время события
* *visits* — количество просмотров

## Используемые инструменты
*PostgreSQL, Python, SQLAlchemy, Tableau, dash*