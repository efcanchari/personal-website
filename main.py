#from website import  create_app
#from website_postgres import create_app
from website import  create_app

app = create_app()

if __name__ == '__main__':
    if app:
        #app.run(debug=True)
        app.run(host='0.0.0.0',port=5000,debug=True)
    else:
        print("App couldn't load")