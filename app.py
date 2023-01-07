from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import pickle

from logging import FileHandler,WARNING
app= Flask(__name__, template_folder = 'templates')

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

file = open('merchantCategoryCode.obj','rb')
le_loaded = pickle.load(file)
file.close()

file1 = open('transactionType.obj','rb')
le_reloaded = pickle.load(file1)
file1.close()

file2 = open('lr.obj','rb')
model_reloaded = pickle.load(file2)
file2.close()

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['GET', 'POST'])
def predict():
    if request.method== 'POST':
        credit_limit= float(request.form['a'])
        avaliable_money= float(request.form['b'])
        transaction_money= float(request.form['c'])
        POS_entry_mode= request.form['d']
        POS_condition_code= request.form['e']
        merchant_category_code= request.form['f']
        transaction_type= request.form['g']
        current_balance= float(request.form['h'])
        card_present= request.form['i']
        expiration_date_key= request.form['j']
        CVV= request.form['k']
        multi_swipe_minutes= float(request.form['l'])
        first_vendor_purchase= request.form['m']
        same_country= request.form['n']

        df1= pd.DataFrame(np.array([credit_limit]), columns=['Credit limit'])
        df2= pd.DataFrame(np.array([avaliable_money]), columns=['avaliable_money'])
        df3= pd.DataFrame((np.array([transaction_money])), columns=['transaction_money'])
        df4= pd.DataFrame(np.array([POS_entry_mode]), columns=['POS_entry_mode'])
        df5= pd.DataFrame(np.array([POS_condition_code]), columns=['POS_condition_code'])
        df6= pd.DataFrame(np.array([current_balance]), columns=['current_balance'])
        df7= pd.DataFrame(np.array([multi_swipe_minutes]), columns=['multi_swipe_minutes'])
        df8= pd.DataFrame(np.array([int((card_present).replace('FALSE',"0").replace('TRUE',"1"))]), columns=['card_present'])
        df9= pd.DataFrame(np.array([int((expiration_date_key).replace('FALSE',"0").replace('TRUE',"1"))]), columns=['expiration_date_key'])
        df10= pd.DataFrame(np.array([int((CVV).replace('FALSE',"0").replace('TRUE',"1"))]), columns=['CVV'])
        df11= pd.DataFrame(np.array([int((first_vendor_purchase).replace('FALSE',"0").replace('TRUE',"1"))]), columns=['first_vendor_purchase'])
        df12= pd.DataFrame(np.array([int((same_country).replace('FALSE',"0").replace('TRUE',"1"))]), columns=['same_country'])
        df13= pd.DataFrame(le_loaded.transform(np.array([merchant_category_code])), columns=['merchant_category_code'])
        df14= pd.DataFrame(le_reloaded.transform(np.array([transaction_type])), columns=['transaction_type'])

        df=pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14], axis=1)
        my_prediction= model_reloaded.predict(df)

    return render_template('result.html',prediction=my_prediction)

if __name__=="__main__":
    app.debug = True
    app.run(port=3840, host='0.0.0.0')