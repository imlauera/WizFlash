![alt text](screenshots/wz1.png)
![alt text](screenshots/wz2.png)
![alt text](screenshots/wz3.png)

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
```python
python3 run.py
```

*If you had any kind of issue running this, please let me know, I'm very active here and I'll read all the issues.*
