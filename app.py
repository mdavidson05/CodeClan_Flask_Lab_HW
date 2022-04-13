#This has to be written exactly like this every time
from flask import Flask

app = Flask(__name__) #has to be called __name__ nothing else will work

from controllers import controller #This line has to be done after the app is created, otherwise controller can't see app. Controller is a class file

if __name__ == '__main__':
    app.run(debug=True)
