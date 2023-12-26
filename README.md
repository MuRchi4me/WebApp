# Разработка Web-Приложений (РWП) 2024

Отчеты по лабораторным работам и ДЗ отправлять на репозиторий и дублировать на github.io

#### Образ виртуальной машины Linux [Ubuntu 22.04][(https://github.com/IgorSergeevichISIT/WebApp/blob/main/linux.md)] для выполнения заданий курса 

## Лекции
### Бекенд
* [Лекция 1. История Web, MVC, Django](lectures/Lecture_1_Web.pdf) 

* [Лекция 2. Базы данных, ER, миграции, ORM](lectures/Lecture_2_Databases_ORM.pdf) 

* [Лекция 3. Методология Agile, состав команды. Диаграммы UML. Работа в git](lectures/Lecture_3_Agile_UML_Git.pdf)

* [Лекция 4. OSI, HTTP. Стандарты интернета](lectures/Lecture_4_HTTP.pdf)

* [Лекция 5. Веб-сервис. REST. Swagger. Микросервисы](lectures/Lecture_5_Web_Service.pdf)

* [Лекция 8. Авторизация, сессии, permissions. Redis, swagger](lectures/Lecture_8_Authorization.pdf)

* [Лекция 9. Цифровая подпись. JWT. SSO](lectures/Lecture_9_jwt.pdf)

* [Лекция 14. Брокер, очереди, gRPC. WebSocket, Polling](lectures/Lecture_14_Async.pdf)

* Лекция 15. Резерв

### Фронтенд
* [Лекция 6. Введение в React, жизненный цикл компонентов, CORS](lectures/Lecture_6_React_Introduction.pdf)

* [Лекция 7. React Hooks](lectures/Lecture_7_Hooks.pdf)

* [Лекция 10. Redux](lectures/Lecture_10_Redux.pdf)

* [Лекция 11. POST, Axios. Диаграммы бизнес требований](lectures/Lecture_11_Axios.pdf)

* [Лекция 12. Адаптивная верстка. PWA. Нативные приложения](lectures/Lecture_12_PWA.pdf)

* [Лекция 13. Мобильные приложения iOS vs Android](lectures/Lecture_13_Mobile.pdf)

## Лабораторные работы
В рамках практических работ по курсу необходимо каждому разработать заявочную систему на услуги по своей предметной области. Система состоит из веб-сервиса, фронтенд приложения, нативного приложения и второго асинхронного сервиса.

У каждого своя предметная область на весь курс: бронирование отелей, билетов в театр/кинотеатр, онлайн-магазин по вариантам, тему выбирать из списка ниже. По каждой теме есть ключевой процесс, в котором `пользователь` оформляет `заявки`, в которой может быть несколько `услуг`. Также есть `модератор`, который может редактировать список `услуг` и одобрять `заявки`. От предметной области зависят: названия ролей пользователей, названия сущностей `услуг` и `заявок`, список полей для них, возможные статусы и изменяемые в них поля. В `нативном приложении` нужно реализовать интерфейс `гостя` - только просмотр `услуг`.

Основной вариант лабораторных по бэкенду - это Django и `Go`. Но можно выполнять также на `Java`, `C#` и `Node.js`, при выполнении условия лабораторных работ. Для фронтенда только `React`+`Redux`+`axios`+`React-Bootstrap`

Каждая лабораторная - это `sprint`, этап разработки по `agile`, под каждую отдельная именованная по теме ветка в `git`. Всего 4 репозитория: под каждый бекенд, фронтенд и нативное приложение. Каждая работа демонстрируется и защищается отдельно. При защите необходимо продемонстрировать работу приложения по своей теме, UML диаграмму из `StarUML`, репозиторий github с кодом и ответить на вопросы. По первому модулю необходимо также сделать ТЗ, а по второму отчет по курсу - РПЗ.

* [Примеры UML и ER диаграмм](/tutorials/homework)
* [Примеры документации](/docs/)
* [Курс по основам Git](https://devops.wiki.iu5edu.ru/docs/lectures/gitcicd/git/lectures/gitcicd/git)

## Лабораторные 2023

#### Лабораторная 1 

- **Цель работы**: выбор варианта-темы на весь курс, знакомство с разработкой бэкенда и разработка дизайна для 2 страниц
- **Порядок показа**: показать две страницы приложения, объяснить заголовки во вкладке `Network`, объяснить шаблоны, контроллеры этих страниц и коллекцию данных
- **Контрольные вопросы**: MVC, Django/Go, шаблонизация, HTTP, Web, HTML
- **Задание**: Базовая шаблонизация в Django (для Go просто HTML) для `услуг`, создание дизайна приложения

Создание базового интерфейса, состоящего из двух страниц. Первая для просмотра списка `услуг` (отели, товары, рейсы и тд) в виде карточек с наименованием, ценой и картинкой. При клике по карточке происходит переход на вторую страницу с подробной информацией об `услуге` (даты, описание и тд) 

В приложении должны быть использованы стили, для каждого элемента списка подгружается свое изображение. Разработать стиль приложения, который будет применяться далее в последующих лабораторных по фронтенду. `CSS` вынести в отдельный файл. Все данные для обеих страниц нужно брать прямо из коллекции, без использования БД.

Добавить поле input для фильтрации на сервере списка `услуг` по одному из полей (наименование, цена), отображаемых на странице (по умолчанию отображать все). Поле поиска должно сохраняться после запроса. Всего в приложении должно быть 2 GET запроса и одна модель-коллекция. Без `JavaScript`

* [Инструкция по работе c Python](/tutorials/python/python.md)
* [Методические указания Django](/tutorials/lab1-py/lab1_tutorial.md)
* [Методические указания Golang](/tutorials/lab1-go/README.md)

#### Лабораторная 2

- **Цель работы**: разработка структуры базы данных и ее подключение к бэкенду 
- **Порядок показа**: показать панель администратора/adminer, добавить запись, посмотреть данные через select в БД, показать шаблоны страниц. Объяснить модели, контроллеры для созданных таблиц
- **Контрольные вопросы**: ORM, SQL, модель и миграции
- **ER диаграмма**: сделать в StarUML; таблицы, связи, столбцы, типы столбцов и их длина, первичные, внешние ключи
- **Задание**: Создание базы данных `PostgreSQL` по теме работы, подключение к созданному шаблонизатору

Необходимо разработать структуру БД по выбранной теме и ее реализовать с учетом требований ниже. Использовать таблицу `услуг` в страницах разработанного приложения. Наполнить таблицы БД данными через `админку Django` или `Adminer`. Получение `услуг`, поиск и фильтрацию удаленных записей сделать через `ORM`.

Для карточек таблицы `услуг` добавить кнопку логического удаления услуги (через статус) с помощью выполнения SQL запроса без ORM.

**Требования к БД**: 

Обязательно наличие 4 таблицы: `услуг` (статус удален/действует, изображение), `заявок` (статус, дата создания datetime, дата формирования datetime, дата завершения datetime, `создатель` и `модератор`), `м-м заявки-услуги` (составной первичный ключ), `пользователей`

Обязательно наличие 5 или более статусов `заявок`: черновик, удалён, сформирован, завершён, отклонён. Названия таблиц и их полей должны соответствовать предметной области. 

* [Методические указания PostgreSQL](/tutorials/lab2-db/README.md)
* [Методические указания Django](/tutorials/lab2-py/lab2_tutorial.md)
* [Методические указания Golang](/tutorials/lab2-go/README.md)
* [Курс по основам БД](https://aiintro.docs.iu5edu.ru/docs/db/)

#### Лабораторная 3

- **Цель работы**: создание веб-сервиса в бэкенде нашей системы для использования его в `SPA`
- **Порядок показа**: Через `insomnia`/`postman` выполнить GET списка `заявок` (отфильтровать по дате формирования и статусу), выполнить GET списка `услуг` (с фильтром), удалить введенную `заявку` (если есть), добавить новую `услугу` с картинкой, добавить `услугу` в заявку, добавить вторую услугу, список `услуг` с заявкой-черновиком, посмотреть `заявку` (из 2 услуг), подтвердить введенную `заявку` (показать ошибку), сформировать `заявку`. Показать измененные данные через select, объяснить модели, сериализаторы.
- **Контрольные вопросы**: веб-сервис, REST, RPC, HTTP, OSI ISO
- **Диаграмма классов** с детализацией бэкенда (домены методов по `url` с интерфейсами, перечислить все методы, модели, таблицы БД) + insomnia/postman
- **Задание**: Создание веб-сервиса со всей итоговой бизнес логикой, но без авторизации, подключение его к БД и тестирование в `insomnia`/`postman`

Создание **веб-сервиса** для получения/редактирования данных из вашей БД. Требуется разработать все методы для реализации итоговой бизнес логики вашего приложения. Для изображений `услуг` использовать `Minio` (рекомендуется) или хранение файлов картинок в бинарном виде в БД.

**Требования к веб-сервису**

Методы и `url` в `API` должны соответствовать `REST`. Для списка `услуг` (как в 1 лабораторной) и `заявок` (по статусу и диапазону даты формирования) нужно предусмотреть фильтрацию на бэкенде. Взаимодействие с БД через `ORM`. Не делать `POST` `заявки`. Для логических действий в приложении (оплата, подтверждение, завершение) предусмотреть отдельные методы для обновления конкретных полей. Заявка создается пустой, указывается автоматически `создатель`, дата создания и статус, остальные поля указываются через `PUT` или смену статуса. При одобрении/отклонении заявки проставляется `модератор` и дата завершения. 

Статусы нельзя менять с любого на любой: `создатель` удаляет и формирует черновик заявки, а `модератор` отклоняет и завершает сформированную заявку. При получении `заявки` возвращется список ее услуг с картинками. В списке `услуг` возвращается id заявки-черновика этого пользователя для страницы `конструктора` заявки. В данной лабораторной пользователь `создатель` зафиксирован во всех методах - укажите его константой через функцию `singleton`.

- Услуги - GET список, GET одна запись, POST добавление, PUT изменение, DELETE удаление, POST добавление в заявку
- Заявки - GET список (кроме удаленных и черновика), GET одна запись (поля `заявки` + ее `услуги`), PUT изменение (если есть доп поля заявки), PUT сформировать создателем, PUT завершить/отклонить модератором, DELETE удаление
- м-м - DELETE удаление из заявки, PUT изменение количества/значения в м-м (если есть доп поля м-м) 

**Рекомендуется реализация методов для изображений**:
- добавление изображений отдельным методов по id услуги. Старое изображение заменяется/удаляется
- удаление изображения встроено в метод удаления услуги
- получение изображения для S3 напрямую по ссылке. При хранении картинки в БД - отдельный метод GET по id услуги.

* [Методические указания DRF](/tutorials/lab3-py/lab3_tutorial.md)
* [Методические указания Golang](/tutorials/lab3-go/README.md)
* [Пример подключения S3-хранилища](https://github.com/iu5git/Networking/tree/main/S3)
* [Пример использования Minio в Python](https://github.com/iu5git/Networking/tree/main/Minio_Python)

#### Лабораторная 4

- **Цель работы**: Разработка базового SPA на React
- **Порядок показа**: показать две страницы фронтенда в браузере из `localhost` с бэкендом, а в `GitHub Pages` с mock на телефоне, применить фильтрацию услуг. Внести изменения в БД, показать их во фронтенде. Объяснить код компонентов для фильтрации, передаваемые props, хуки, вызовы fetch.
- **Контрольные вопросы**: react, props, компонент, элемент, состояние, хуки, жизненный цикл компонента
- **Deployment диаграмма** все узлы и компоненты системы: фронтенда, web-сервера со статикой, веб-сервиса, базы данных и других хранилищ и тд. Узлы соединить протоколами, компоненты фронтенда и бэкенда поместить в узлах, указать API между ними.
- **Задание**: Разработать две страницы фронтенд приложения на `React`, `TS` и подключить его к веб-сервису. Подготовить ТЗ на итоговую систему. 

Разработать базовый интерфейс приложения на `React` для `гостя`, аналогичный двум страницам из лабораторной работы №1 для просмотра `услуг`. При этом на странице списка `услуг` должны быть все необходимые фильтры (по диапазону дат, названию, цене) с фильтрацией на бэкенде. Использовать компоненты `React-Bootstrap`. Для карточек предусмотреть изображение по-умолчанию, если поле в `услуге` пустое. Необходимо развернуть фронтенд на `GitHub Pages`.

В приложении должны быть навигационная панель `navbar` для списка базовых страниц, а также самописная навигационная цепочка `breadcrumbs`, где отображается путь от базовой страницы к текущей. В этой лабораторной никакого `Redux`, а `Context` вообще в курсе использовать нельзя.

Содержимое карточек получать из веб-сервиса лабораторной №3. Ajax-запросы написать самостоятельно через `fetch`. Ограничение с `CORS` решить через проксирование `React`. В методах `fetch` предусмотреть получение данных из коллекции с `mock`-объектами при отсутствии доступа к вашему бэкенду.

* [Методические указания](/tutorials/lab4/lab4_tutorial.md)

**ТЗ** на итоговую систему (сплошная нумерация):
1. **цель**
2. **назначение** - краткое описание для чего, кто работает в системе
3. **задачи**
4. **методы веб-сервиса** таблицей с группировкой по доменам: метод, url, описание, входные, выходные данные
5. **Функциональные требования** - список окон и какие действия для каких групп пользователей доступны. Указать, какие методы бэкенда при этом вызываются. 8 страниц: 

* гость: регистрация, аутентификация, список услуг, одна услуга

* создатель заявки: конструктор заявки, список заявок

* модератор: список услуг таблицей, редактирование/создание услуги

6. **требования к аппаратному** обеспечению для сервера и клиента
7. **требования к программному** обеспечению с версиями для серверных компонентов и для клиента

#### Лабораторная 5

- **Цель работы**: Завершение бэкенда для `SPA`
- **Порядок показа**: выполнить авторизацию через `swagger` в режиме инкогнито, использовать содержимое `куки`/`localStorage`+`authorization` из браузера для заголовков остальных запросов через `swagger` и `insomnia`/`postman`. Выполнить GET списка заявок: 403 для гостя, для модератора все заявки, для создателя только его. Выполнить PUT завершения заявки: для создателя 403 статус, для модератора успех и обновление полей. Показать содержимое `Redis`
- **Контрольные вопросы**: куки, сессия, redis, jwt, авторизация, аутентификация
- **Sequence диаграмма**: весь набор `HTTP` запросов по бизнес-процессу без БД и нативного приложения: аутентификация, список услуг без черновика, добавление услуги в заявку, еще раз список услуг с черновиком, просмотр черновой заявки, формирование заявки, обращение к асинхронному сервису и обратно, список заявок с данными от асинхронного. Добавить домены в качестве `Lifeline`, при добавлении сообщений выбирать методы доменов из диаграммы классов, передавать ключевые входные и выходные данные через `arguments` в скобках у `Message`
- **Задание**: Добавление авторизации и `swagger` в веб-сервис

Реализовать методы бэкенда для `аутентификации` и `регистрации`. Авторизация через хранение сессий и куки. Автозаполнение пользователя в таблице `заявок` при создании новой. Добавить описание методов для `swagger`.

Добавить проверку `Permissions` для методов `модератора`. Без авторизации в `Swagger` должно быть доступно только чтение-получение данных через API, с авторизацией - методы `пользователя`, а для `модератора` доступны все методы.

* [Настройка через WSL](https://github.com/iu5git/Networking/tree/main/kafka_wsl)
* [Методические указания Redis](/tutorials/redis/README.md)
* [Методические указания DRF Сессии](/tutorials/lab5-py/README.md)
* [Методические указания Golang JWT](/tutorials/lab5-go/README.md)

#### Лабораторная 6

- **Цель работы**: Завершение интерфейса `пользователя` в `React`
- **Порядок показа**: показать авторизацию, добавление и формирование `заявки`. Пояснить в коде использование `redux` и `axios`. Показать авторизацию в браузере, использовать содержимое `localStorage`/`cookie` чтобы показать заявки пользователя в `insomnia`/`postman`.
- **Контрольные вопросы**: схема redux, reducer, store, контекст, axios
- **Диаграмма классов** с детализацией бэкенда и фронтенда: добавить методы авторизации, фронтенд разделить на страницы, добавить у страниц зависимость от API.
- **Activity диаграмма/BPMN** для итогового бизнес-процесса для ДЗ: описание бизнес-процесса, разделение на дорожки по ролям двух пользователей и выделенного сервиса, действия соответствуют операциям пользователей в вашей системе.
- **Задание**: Добавить авторизацию и возможность оформления `заявок` во фронтенд через `Redux Toolkit`

Добавить страницы для регистрации и авторизации. Добавить окно для просмотра списка `заявок` пользователя в виде таблицы. Добавить в меню пункты для новых страниц. Для обращений к методам веб-сервиса использовать `axios`. При выполнении запросов отображать на странице анимацию.

Добавление менеджера состояний `Redux Toolkit` для хранения фильтров заявок и услуг, а также состояния интерфейса после авторизации. В приложении должно быть реализовано переключение между интерфейсом гостя и интерфейсом пользователя по кнопке `Вход`/`Выход`. После авторизации в меню должно отображаться Имя/Логин пользователя. При выходе должно сбрасываться содержимое конструктора новой заявки.

Добавление на странице услуг кнопки `Добавить` для внесения данной услуги в новую заявку. Добавление страницы `конструктора` заявки-черновика, где можно удалить уже добавленные в заявку услуги, поменять их количество или `подтвердить` заявку. Эта же страница используется для просмотра заявок в других статусах, но без возможности редактирования. Переход на страницу `конструктора` через специальную кнопку, которая меняет состояние, если заявка-черновик есть или ее нет. 

* [Методические указания Redux Toolkit + fetch](/tutorials/redux/redux_toolkit.md)
* [Методические указания Redux Toolkit + кодогенерация и Axios](/tutorials/lab6/lab6_tutorial.md)

#### Лабораторная 7

- **Цель работы**: Создание нативного приложения
- **Порядок показа**: Кроме `Tauri` показывать на телефоне, отредактировать услуги в БД и продемонстрировать изменение в нативном приложении  
- **Контрольные вопросы**: виды нативных приложений и отличие от web-приложений, react-native, pwa, tauri
- **Задание**: Создание приложения для `гостя` на iOS/Android/Tauri/Qt/React-native и подключением к веб-сервису

Создание простого нативного приложения для интерфейса гостя (без авторизации и редактирования), состоящий из 2 страниц с фильтрацией и картинками. Подключить приложение к разработанному API через IP адрес в локальной сети.

* [Методические указания Tauri](/tutorials/tauri/)
* [Методические указания React Native + Redux Toolkit](/tutorials/react-native/react_native.md)
* [Методические указания iOS (Swift)](https://github.com/iu5git/web-2022/blob/main/tutorials/ios_tutorial/ios_tutorial.md)
* [Методические указания Android (Java)](https://github.com/iu5git/web-2022/blob/main/tutorials/android_tutorial/android_tutorial.md)
* [Методические указания Android (Kotlin + Compose)](/tutorials/lab7-android-kotlin/README.md)

#### Лабораторная 8

- **Цель работы**: Знакомство с межсервисным взаимодействием и асинхронностью
- **Порядок показа**: вызвать через `insomnia` http-метод асинхронного сервиса, показать что в основном приложении появился результат, потом вызвать метод основного сервиса напрямую, чтобы изменить результат
- **Контрольные вопросы**: grpc, асинхронность, веб-сервис
- **Задание**: Создание асинхронного сервиса для отложенного действия (вычисление, моделирование, оплата и тд)

Требуется разработать второй простой асинхронный сервис на другом языке (кто делал на Django - Go и наоборот) с одним http-методом для выполнения отложенного действия в вашей системе (вычисление, моделирование, оплата и тд). Действие выполняется с задержкой 5-10 секунд, результат сервиса случайный, например успех/неуспех, достаточно в результате обновить одно поле в `заявке`. 

В исходном веб-сервисе также необходимо добавить http-метод для внесения результатов. Асинхронный сервис взаимодействует с основным через `http`, без прямого обращения в БД. Добавить псевдо авторизацию в методе основного сервиса - передавать как константу какой-нибудь ключ, например на 8 байт, и через if просто проверять на совпадение это поле.

* [Методические указания Django](/tutorials/lab8-py/README.md)
* [Методические указания Golang](/tutorials/lab8-go/README.md)

#### Домашнее Задание

- **Цель работы**: Закрепление полученный знаний
- **Порядок показа**: создать заявку в интерфейсе `пользователя`. Авторизоваться под `модератором`, одобрить `заявку` и отредактировать список `услуг`.
- **Отчет**: отчет необходимо отправить на почту [aikanev@bmstu.ru](). Оценивается раскрытие предметной области в описании и приложении, корректность оформления отчета.
- **Контрольные вопросы**: любые вопросы по реализации интерфейса `модератора`
- **Диаграммы**: диаграмма состояний для статусов `заявок` и диаграмма прецедентов. Актуализировать все диаграммы из лабораторных, все диаграммы должны соответствовать реализованной вами системе. Все диаграммы должны быть читаемые, шрифт на них должен не отличаться по размеру от шрифта текста отчета.
- **Задание**: Реализовать интерфейс `модератора` и подготовить итоговый отчет

Необходимо добавить в приложение React интерфейс `модератора`, доступный после его авторизации и имеющий следующие отличия:
- Новое окно редактирования `услуг`, список услуг отображается таблицей. Доступно добавление новых услуг (обязательные и необязательные поля), редактирование, удаление.
- В окне списка `заявок` доступны кнопки для смены статуса заявок. Также есть поля фильтрации по диапазону `даты формирования` и статусу заявок (через бэкенд) и пользователю (на фронтенде).
- Окно списка `заявок` переделать на `short polling` чтобы отображать актуальные статусы

**Отчет-РПЗ** по всем лабораторным и ДЗ:
1. **Введение** (актуальность, цель, назначение, нефункциональные требования, задачи)
2. **Бизнес-процесс**. Описание предметной области. Диаграмма прецедентов, диаграмма состояний и деятельности/BPMN (>300 слов)
3. **Архитектура**. Диаграммы развертывания, ER с назначением таблиц и диаграмма классов с детализацией бэкенда и фронтенда (>300 слов)
4. **Алгоритмы**. Диаграмма последовательности HTTP запросов (>300 слов)
5. **Описание интерфейса**. Перечень окон, их назначение и выполняемые пользователями действия (>300 слов)
6. **Заключение**. Перечень выполненных задач и достигнутые результаты. Ссылка на GitHub
7. **Список использованных источников**  
8. **Приложение. Техническое задание**

#### Дополнительные задания
1. Индексы в БД, большое количество `услуг` (> 100000) и пагинация (+4 балла). Порядок показа: показать пагинацию с фильтрацией по индексу в React-приложении. Включить и отключить индекс - показать отличие во времени запроса.
* [Индексы и план запроса](https://github.com/iu5git/Database/blob/main/tutorials/lab_index.md)
2. Адаптивность дизайна (+2 балла). Перейти в адаптивный режим браузера, поменять ширину. Объяснить настройки для размера карточек, количества колонок и тд.
* [Progressive Web App и адаптивный дизайн](/tutorials/pwa/PWA.md)
3. Кодогенерация из `swagger` (+2 балла). Показать применение сгенерированного кода фронтенда из `swagger`.

#### Темы индивидуальных заданий
1. Автоматическое тестирование вашего сервиса через Python - автотесты методов API
3. Полноценное нативное приложение - интерфейс модератора или клиента с авторизацией 
4. Заказ без авторизации через redis
5. Черновик-заявки через redux и 5 запросов-событий которые меняют это состояние: одобрение, удаление заявки, добавление в заявку, авторизация и деавторизация
7. Ролевая модель через несколько кастомных таблиц
8. Список услуг кешировать в redis
9. Сделать дашборд со статистикой заявок по месяцам и прирост новых услуг/заявок/клиентов
11. Атрибуты услуги через вертикальную таблицу атрибутов: список атрибутов в отдельной таблице, а значения через вторую м-м 
12. Запрос прав модератора при регистрации и окно подтверждения запросов в отдельной странице у модераторов.

#### Темы методических указаний для детализации
2. Для 2 лабораторной. Подробнее про миграции Django. Примеры работы с моделями с получением заявки и ее услуг. Составной PK в м-м
5. Для доп. задания. Работа с индексами и пагинацией (в бэкенде и фронтенде)
6. Для 1 лабораторной. Описать верстка карточками, использование картинок, создание дизайна и использование стилей из `figma`

### Темы 2024:

#### Малый бизнес
1. Система заявок для поваров в быстром питании на приготовление. `Услуги` - виды блюд с указанием поваров, `заявки` - заказ на приготовление блюд.
2. Рецепты автоматического приготовления пищи. `Услуги` - продукты, `заявки` - рецепты
3. Заявки от коллцентра мелкого бизнеса: менеджер-создатель заявки, исполнитель+курьер. `Услуги` - услуги данного бизнеса, `заявки` - заявки от клиентов на услуги.
4. Продажа очков. `Услуги` - свойства линз, `заявки` - заказы от покупателей на линзы
5. Книжное издательство. `Услуги` - работы издательства (печать, брошюрование и тд), `заявки` - заказы на издание книги
6. Размещение товаров на маркетплейсе. `Услуги` - категории товаров, `заявки` - заявки от продавцов на размещение товара
7. 2НДФЛ. `Услуги` - набор кодов для отчислений, `заявки` - справки 2 НДФЛ за месяц
8. Бухгалтерский баланс компании. `Услуги` - добавочный капитал, заемные средства и тд, `заявки` - отчетность компании по показателям

#### Компьютерные игры
1. Карточная игра Эволюция. `Услуги` - карты Эволюции, `заявки` - карточные ходы соперников в игре
2. Автоматический подбор игроков для игры. `Услуги` - карты, игровые локации, `заявки` - игры, список участников автоматически собирается из поданных ими запросов

#### Химическое производство
1. Оборудование для химических лабораторий. `Услуги` - лабораторное оборудование, `заявки` - заявки на приобретение
2. One-pot синтезы. `Услуги` - исходные вещества, `заявки` - проведение синтеза при заданных условиях
3. Производство косметики. `Услуги` - вещества для производства, `заявки` - виды косметики с указанием состава
4. Производство лекарств из готовых веществ. `Услуги` - действующие и др вещества, `заявки` - составляющие лекарств
5. Производство красок из красителей. `Услуги` - готовые красители и др вещества, `заявки` - виды красок (батик, гуаш) по цветам


#### Электронные услуги
1. Визовый центр РФ - заявки на визы. `Услуги` - виды виз, `заявки` - заявки на получение нужной визы.
2. Автоматический контроль паспортов на границе. `Услуги` - паспорта, которые заведены в системе, `заявки` - факты пересечения границы по паспорту
3. Банковские счета. `Услуги` - банковские договоры, `заявки` - открытие новых счетов в рамках банковского договора
4. Заявки на изготовление документов при смене фамилии. `Услуги` - виды документов для замены, `заявки` - заявка на замену с указанием новой фамилии и причины
5. Электронная таможня. `Услуги` - виды товаров, ценностей, валют для провоза, `заявки` - заявки для декларирование провозимых товаров.
6. Регистрация новых препаратов. `Услуги` - список болезней для лечений препаратом, `заявки` - заявки на регистрацию нового препарата
7. Регистрация новых видов животных. `Услуги` - места обитания животных, `заявки` - заявки на открытие нового вида с указанием рода
8. Уведомления электронных услуг. `Услуги` - получатели уведомления, `заявки` - отправка уведомления
9. Сервис для самозанятых. `Услуги` - виды предоставляемых услуг `заявки` - заявка на регистрацию замозанятого с указанием ФИО, деятельности и др данных
10. Сбор средств на реконструкцию исторических зданий. `Услуги` - виды работ по реконструкции `заявки` - заявки на реконструкцию и сбор средств
11. Электронное голосование. `Услуги` - варианты названий для объектов города, `заявки` - результаты голосования
12. Заявка на проведение тендера. `Услуги` - участники тендера, `заявки` - статусы тендера
13. Договоры банка. `Услуги` - набор услуг банка, `заявки` - заявка на подключение к обслуживанию
14. Чаты. `Услуги` - чаты, `заявки` - отправка сообщений (м-м сообщений-`заявок` для ответов вместо м-м к `услугам`)
15. Групповая отправка файла в мессенджере. `Услуги` - получатели, `заявки` - процесс отправки файла
16. Регистрация участников на спортивное соревнование. `Услуги` - участники, `заявки` - заявка для команды на участие
17. Банкомат. `Услуги` - различные виды купюр, `заявки` - операции внесения/снятия наличных
18. Удаленная поддержка. `Услуги` - виды происшествий, `заявки` - обращения от пользователей
19. Счетчики воды. `Услуги` - разные адреса, `заявки` - фиксация показаний от счетчиков


#### ИТ услуги
1. Консалтинг по ИТ безопасности. `Услуги` - виды консалтинга, `заявки` - заявки на проведение консалтинга
2. Обслуживание ИТ инфраструктуры. `Услуги` - виды проводимых работ, `заявки` - заявки по настройке сетевого оборудованию, виртуалки и тд
3. Мониторинг ИТ угроз. `Услуги` - виды угроз, `заявки` - факты возникновения угроз в подразделении компании
4. Сайт КТС. `Услуги` - виды разработки, `заявки` - заявки от заказчиков
5. Аренда виртуальных машин. `Услуги` - тарифы на аренду, `заявки` - заявки на аренду кластера машин
6. Заявки на подключение провайдера. `Услуги` - виды работ по подключению, `заявки` - заявка от клиента на подключение
7. Заявки на установку серверного ПО. `Услуги` - программное обеспечение, `заявки` - заявки от сотрудников
8. Создание датацентра. `Услуги` - комплектующие, аппаратное обеспечение, `заявки` - процесс создания датацентра
9. Голосовой помощник. `Услуги` - доступные действия помощника, `заявки` - интенты пользователя


#### Социальные услуги
1. Трудоустройство женщин в отпуске по уходу за ребенком. `Услуги` - вакансии для женщин с детьми, `заявки` - подача заявок на вакансии от женщин
2. Система трудоустройства для инвалидов. `Услуги` - вакансии для инвалидов, `заявки` - подача заявок на вакансию от инвалидов
3. Система социальной помощи инвалидам - доставка еды, сопровождение на мероприятие и тд. `Услуги` - оказываемые услуги, `заявки` - заявки на них от инвалидов
4. Заказы на молочную кухню (для детей). `Услуги` - виды продуктов, `заявки` - заявки от родителей
5. Справочник по медицине катастроф и первой помощи. `Услуги` - виды первой помощи, `заявки` - виды поражений при чрезвычайных ситуациях
6. Сервис для работодателей. `Услуги` - города, в которых будет открыта вакансия, `заявки` - заявки на создание вакансий



## Примерные вопросы к экзамену и РК
1. Опишите шаблон MVC, структуру и назначение компонентов.
2. Опишите схему, как реализован шаблон MVC в фреймворке Django.
3. Что такое Django? Его назначение и возможности.
4. Что такое шаблонизация Django? Приведите примеры.
5. Опишите протокол HTTP. Схему работы и основные понятия.
6. Опишите стек протоколов интернета TCP/IP.
7. Перечислите основные составляющие web и опишите их.
8. Что такое HTML, CSS? Приведите примеры.
9. Что такое URI? Опишите элементы URI для HTTP.
10. Виды баз данных. Приведите примеры и отличия.
11. Объясните назначение ORM, ее составляющие. Укажите преимущества и недостатки ORM.
12. Что такое модель и миграция?
13. Укажите группы SQL запросов, их примеры и назначение.
14. Что такое веб-сервис? Отличие от веб-сервера.
15. Что такое Web API? Назначение и применение.
16. Микросервисная архитектура. Отличия от монолитной архитектуры.
17. Перечислите требования REST, опишите их.
18. Что такое RPC? Варианты RPC и их отличия.
19. Что такое Swagger? Назначение и использование.
20. Что такое AJAX? Схема работы и назначение.
21. Назначение JSON и XML. Примеры и отличия.
22. Что такое git? Опишите схему работы с ветками GitHub.
1. Методология разработки Agile. Состав IT команды.
2. Перечислите основные диаграммы UML и их назначение.
3. Что такое Web реального времени? Что такое WebSocket?
4. Укажите отличия XmlHttpRequest и fetch. Приведите примеры.
5. Перечислите отличия Axios от fetch. Приведите примеры.
6. Что такое React? Что такое компонент, его состояния и свойства.
7. Структура React проекта. Назначение Babel и WebPack.
8. Жизненный цикл React компонента.
9. Назначение хуков useState и useEffect.
10. Назначение хуков useContext и useReducer.
11. Опишите схему работы менеджера состояний Redux.
12. Опишите работу Redux на диаграмме последовательности.
13. Какие параметры передаются при создании Store? Их назначение.
14. Что такое Cors? Укажите варианты решения.
15. Что такое Redis? Его назначение и варианты применения.
16. Опишите схему авторизации с помощью JWT.
17. Опишите схему авторизации с помощью сессий.
18. Что такое авторизация и аутентификация? Укажите варианты авторизации и их отличия.
19. Что такое SSO? Схема работы.
20. Протокол OAuth. Схема работы.
21. Отличия мобильных и веб-приложения. Языки и технологии для разработки мобильных приложений.
22. Что такое pwa? Отличия от других вариантов приложений.
23. Плюсы и минусы разработки на React Native.
24. Назначение фреймворков Electron и Tauri. Их отличия.
25. Опишите этапы подхода DevOps. Назначение GitHub Pages.

