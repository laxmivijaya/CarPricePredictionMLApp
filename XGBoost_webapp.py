# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 09:51:53 2024

@author: laxmi
"""

import pandas as pd
import datetime as dt
import xgboost as xgb
import streamlit as st
import time

def main():
    html_temp="""
      <div style = "background-color:Lightblue;padding:16px">
      <h2 style="color:black; text-align:center;"> <B>Car Price Prediction Using ML</B> </h2>
      </div>
      """
      
    model = xgb.XGBRegressor()
    model.load_model("C:/Users/laxmi/Downloads/Cardata/xgb_model.json")
    
    
    st.markdown(html_temp, unsafe_allow_html=True)
    
    st.write('')
    st.write('')

    st.markdown("##### Are you planning to sell your car!?\n##### So let's try evaluating the price.")
    p1 = st.number_input("What is the current ex-showroom price of the car (In Lakhs)", 2.5,25.0,step=1.0)
    p2 = st.number_input("What is the milage on the car?",1000, 100000, step=500)
    
    s1 = st.selectbox("What is the fuel type of the car?", ('Petrol', 'Diesel', 'CNG'))
    
    if (s1 == 'Petrol'):
        p3=0
    elif (s1 == 'Diesel'):
        p3=1 
    elif (s1 == 'CNG'):
        p3=2 
        
   
    s2 = st.selectbox("What type of customer are you?", ('Dealer', 'Individual'))
    
    if (s2 == 'Dealer'):
        p4=0
    elif (s2 == 'Individual'):
        p4=1 

    s3 = st.selectbox("What type of transmission do you need?", ('Manual', 'Auto'))
    
    if (s3 == 'Manual'):
        p5=0
    elif (s3 == 'Auto'):
        p5=1 
        
    p6 = st.slider("Number of prior owners of the car?",0,3)
    
    date_time=dt.datetime.now()

    years = st.number_input("Year car was manufactured?",1990, date_time.year)
    p7 = date_time.year - years
    
    data_new = pd.DataFrame({
        'Present_Price': p1,
        'Kms_Driven': p2,
        'Fuel_Type': p3,
        'Seller_Type': p4,
        'Transmission': p5,
        'Owner':p6,
        'Age':p7
    }, index=[0])
    
    try:
       if st.button('Predict'):        
          pred = model.predict(data_new)
          if pred>0:
             with st.spinner('Wait for it...'):
                 time.sleep(1)
          

             st.toast('Hip!')
             time.sleep(.5)
             st.toast('Hip!')
             time.sleep(.5)
             st.toast('Hooray!', icon='🎉')
             st.balloons()
             st.success("You can sell your car for {:.2f} lakhs".format(pred[0]), icon="✅")
          else:
              st.Warning("You will not be able to sell this car")
    except:
        st.Warning("Something went wrong, please check your input")
           
if __name__ == '__main__':
   main()