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

**앱 등록**

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-09-22-13-54-36-image.png)

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-09-22-13-54-46-image.png)

url > view > templates

1. 가상환경 생성 실행

2.  django LTS 버전 설치

3. django 프로젝트 생성

4. 앱 생성 ( 커맨드를 manage.py 가 있는 경로에서)

5. 앱 등록 (settings.py)

6. 서버 실행 테스트  runserver

7. 앱 >  URL >  VIEW  > TEMLATES

URL

path('index/', views.index),

def index(request):

    return render(request, "index.html")



**오류**

[Python could not be resolved Pylance from source 모듈 인식 안될때 해결방법](https://incomeplus.tistory.com/187)



**경로를 맞게 설정했으나, 이미지 Not Found 오류가 있음**

> static 설정이 필요함

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-09-22-15-01-24-image.png)



****static에 변수 선언   ****

`{% get_staitc_prefix %}dir/{{var}}.jpg`

```python
<img src="{% static 'img/sam.jpg' %}" alt="2">
<img src="{% get_static_prefix %}img/{{din_img}}.jpg" alt="4">
```

쟝고 문법

[[django] 파이썬 Django(장고) 템플릿 문법](https://goodthings4me.tistory.com/92)


