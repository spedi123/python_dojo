#Pre-rec

```
pip3 install pipenv
```

# Checklist

1. create a folder / dir for your assignemnt
2. Navigate into that folder
3. Create your virtual env

```
pipenv install flask
```

4.'Warnging' check for the files "pipfile" and "pipfile.lock" - if you don't see these you need ti fix it.

5. Launch the virtual env

```
pipenv shell
```

6. create a server.py file

```py
from flask import Flask, render_template, request, redirect, session
# this is going to move in the future
@app.route('/')
def hello_world():
    return 'Hello World!'
# end of moving area

#this must be on the bottom of this file
if __name__=="__main__":
    app.run(debug=True)
```
