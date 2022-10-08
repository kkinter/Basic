```bash
#create user

python manage.py createsuperuser
```

![](C:\Users\Wook\AppData\Roaming\marktext\images\2022-10-05-14-34-22-image.png)

```py
##<app name> / admin.py

from django.contrib import admin

# Register your models here.

from .models import Project

admin.site.register(Project)

```

### static

```py
#models.py
featured_image = models.ImageField()
```

### collect static

```bash
python manage.py collectstatic
```

### white noise?

### allowed host ?
