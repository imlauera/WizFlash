### Installation
pip install -r requirements.txt
### Create the database
On the main dir, open a python3 console and type:
```python
from run import app
from models import *
app.app_context().push()
db.create_all()
```

### Usage
python3 run.py

If you've any kind of issues running this, please let me know, I'm very active right here.
