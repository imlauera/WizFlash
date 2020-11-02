### Installation
pip install -r requirements.txt
### Usage: python3 run.py

### Create the database:
In the python3 console
```python
from run import app
from models import *
app.app_context().push()
db.create_all()
```
