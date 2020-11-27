from flask import Flask, render_template, request, redirect, url_for, jsonify
import scraper
import pandas as pd
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/video', methods=['GET','POST'])
def video():
    if request.method == 'POST':
        result=request.form['video']
        scraper.scrape(result)
        #print (video)
        fileName = 'scrape.csv'
        commentList = pd.DataFrame.from_csv(fileName)
        return render_template('video.html', data=commentList.to_html())


if __name__=="__main__":
    app.run(debug = True)