---
type: web_development
date_created: Monday, November 7th 2022, 1:06:31 pm
date_modified: Tuesday, November 8th 2022, 5:30:19 pm
---
#python #fullstack

# About
Flask is a lightweight fullstack python framework.

# Snippets

## simple example

```python
from flask import Flask

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

