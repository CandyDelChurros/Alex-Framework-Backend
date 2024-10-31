from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 
def index(): 
    return ('Olá Mundo')
    
@app.route('/contact')
def contact():
    return render_template('contact.html') 

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html') 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
