```python
core
|-- __init__.py
|-- management/
|   |-- __init__.py
|   |   `-- commands
|   |       |-- __init__.py
|   |       `-- wait_for_db.py
import time
  
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
  
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to wait for DB."""
    
    def handle(self, *args, **options):
        """Entrypoint for command"""
        self.stdout.write('Waitng for database ...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unvailable, waiting 1 second ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available !'))

```

```bash
$ docker-compose run --rm app sh -c "python manage.py test"
[+] Running 1/0
 - Container api-prac-db-1  Running                      0.0s 
System check identified no issues (0 silenced).
..Waitng for database ...
Database unvailable, waiting 1 second ...
Database unvailable, waiting 1 second ...
Database unvailable, waiting 1 second ...
Database unvailable, waiting 1 second ...
Database unvailable, waiting 1 second ...
Database available !
.Waitng for database ...
Database available !
.
----------------------------------------------------------------------
Ran 4 tests in 0.034s

OK
```

```bash
$ docker-compose run --rm app sh -c "python manage.py wait_for_db"
[+] Running 1/0
 - Container api-prac-db-1  Running                      0.0s 
Waitng for database ...
Database available !
```