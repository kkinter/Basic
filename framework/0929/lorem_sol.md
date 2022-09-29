

## 1. 가상환경 생성

```bash
python -m venv venv
```

## 2. 프로젝트 생성

```py
django-admin startproject config
```

## 3. 앱 생성

```py
python startapp lorem
```

## 4. 앱등록

```py
#settings.py

installapp [
    'lorem',
]
```

## 5. URL 등록

```py
#<app name>/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]
```

## 6. 함수 생성

```py
#<app name>/view.py
#<app name>/templates 폴더를 앱 폴더에 생성했기 때문
def index(request):
    return render(request, 'lorem/index.html')
```

## 7. form

```py
#templates/lorem/index.html
# 앱 분리를 하기 위해 lorem:(폴더의)result

<form action="{% url 'lorem:result' %}">
    <input type="" name="">
    <input type="" name="">
</form>


```

```py
#<app name>/urls/py

path('result/', views.results)
```

```py
# <app name>/views.py
import random
def result(request):
    word_list = ['돼]
    
    paragraph = request.GET.get('paragraph')
    word = int(request.GET.get('word'))

    lorem_para = []
    # 단어의 수 만큼 랜덤으로 단어를 추출하는 반복
    string = ""
    for _ in rnage(paragraph):
        for _ in range(word):
            string += random.choice(word_list) + " "
        lorem_para.append(string)
    context = {
    'lorem_para' : lorem_para,
    }

    return render(request, 'lorem/result.html', context)
```
