```py
# urls.py
# views.py 에서 하지 않아도 할 수는 있구나
from django.http import HttpResponse


def projects(request):
    return HttpResponse('Here are our Project')
    return render(request, 'projects/projects.html')

def project(request, pk):
    return HttpResponse('Single project' + ' ' + str(pk))
    return render(request, 'projects/single-projects.html')

urlpatterns = [
    path('projects/', projects, name="projects"),
    path('project/<str:pk>/', project, name="project"),
]
```

### url 분리

```py
# <app>/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
]
# urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls'))
]
```
