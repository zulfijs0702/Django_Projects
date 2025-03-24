from bottle import Bottle, run 
app = Bottle()
@app.route('/')
def home__page():
    return 'Welcome'
if __name__=='__main__':
    run(app, host='localhost', port=8081)