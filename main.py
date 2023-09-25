from flask import Flask, render_template


app = Flask(__name__)

@app.get('/')
def root():
    return render_template('index.html')

@app.get('/page-1/')
def page1():
    return render_template('odezjda.html')

@app.get('/page-2/')
def page2():
    return render_template('obuv.html')

@app.get('/page-3/')
def page3():
    return render_template('kurtka.html')

if __name__=='__main__':
    app.run(debug=True)