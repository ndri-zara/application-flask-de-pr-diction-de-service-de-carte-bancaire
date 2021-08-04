from flask import Flask, render_template, url_for, request
import pandas as pd



app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('home.html')

@app.route('/second')
def second():
    df = pd.read_csv("C:\\Users\\zara\\bien.csv" , sep=',')
    
    return df.to_html()

@app.route('/quatrième')
def own_prediction():
    
    return render_template('own_prediction.html')


@app.route('/troisième')
def troisième():
    df = pd.read_csv("C:\\Users\\zara\\bien.csv" , sep=',')
    a= df.sample(n=10)
    return a.to_html()
    
    





    

if __name__ == '__main__':
    app.run(debug=True)