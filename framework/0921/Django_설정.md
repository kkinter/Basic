

**가상환경 생성**

``` 
python -m venv <이름>
python -m venv mypjt
```



**가상환경 실행**

```
source <이름>/Scripts/activate
source mypjt/Scripts/activate
```

**라이브러리 확인**

```
pip list
```

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-09-21-13-52-53-image.png)

**라이브러리 설치**

```
pip install <이름>==<버전>
pip install django==3.2.12
```

**프로젝트 생성**

```
django-admin startproject <이름>
django-admin startproject server
```

**웹서버 실행**

```
python manage.py runserver
```

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-09-21-14-01-00-image.png)

**웹서버 종료**

```
ctrl + c
```

> ### LTS 란?
> 
> Long-Term-Support releases의 줄임말으로,
> 
> 일반적인 버전보다 지원을 오래 해주는 버전

![Django release roadmap](https://static.djangoproject.com/img/release-roadmap.4cf783b31fbe.png)

**앱 생성하기**

```
python manage.py startapp <앱 이름>
python manage.py startapp testapp
```

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-09-21-14-18-21-image.png)

| mypjt(가상환경 폴더)/ | Include              |                    |             |
| --------------- | -------------------- | ------------------ | ----------- |
|                 | Lib                  |                    |             |
|                 | Scripts              |                    |             |
|                 | **server(프로젝트 폴더)**/ | manage.py          |             |
|                 |                      | db.sqlite3         |             |
|                 |                      | **testapp(앱 폴더)/** | migrations/ |
|                 |                      |                    | __init__.py |
|                 |                      |                    | admin.py    |
|                 |                      |                    | apps.py     |
|                 |                      |                    | modles.py   |
|                 |                      |                    | tests.py    |
|                 |                      |                    | views.py    |


