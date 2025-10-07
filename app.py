from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    msg=''
    output=""

    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['sex'])
        cp= int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        oldpeak = int(request.form['oldpeak'])
        slope = int(request.form['slope'])
        ca = int(request.form['ca'])
        thal = int(request.form['thal'])
        test_data=[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        print ("test data",test_data)
        import pandas as pd
        from sklearn.model_selection import train_test_split
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score

        data = pd.read_CSV("heart.CSV")
        data.head()

        data.info()

        x=data.drop('target',axis=1)
        y=data['target']

  


