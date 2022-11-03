from numpy.core.fromnumeric import size
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

st.title("Vehicle Insurance Prediction")



nav = st.sidebar.radio("Sections",["Home","Two-Wheeler","Four-Wheeler-Light","Four-Wheeler-Heavy"])
st.sidebar.markdown("Made by [Mainak](https://www.linkedin.com/in/mainak-chaudhuri-127898176/)")  
if nav == "Home":
    st.image("bike.jpg",width= 700)
    




elif nav == "Two-Wheeler":

    data = pd.read_csv("bikes.csv")
    data1 = data.copy()
    label_encoder = preprocessing.LabelEncoder()
    data['brand']= label_encoder.fit_transform(data['brand'])
    data['brand'].unique()
    lr = LinearRegression()
    Z = data[['power', 'age', 'kms_driven','stroke','brand']]
    lr.fit(Z, data['price'])
    st.image("bike.jpg",width= 800)
    st.header("Two Wheeler Insurance Premium")
    val1 = st.number_input("Enter your Bike's Horsepower",100,2000,step = 100)
    val2 = st.number_input("Enter your Bike's Age (years)",1,40,step = 1)
    val3 = st.number_input("Enter your Bike's Kilometers Travelled (in 1000 km)",1,50,step = 1)
    val4 = st.number_input("Enter your Bike's Stroke",1,5,step = 1)
    val5 = st.number_input("Enter your Bike's Brand",0,22,step = 1)

    val = np.array([val1,val2,val3,val4,val5]).reshape(1,-1)
    
    datax = [data1["brand"], data["brand"]]
    headers = ["data1", "data"]
    df3 = pd.concat(datax, axis=1, keys=headers)
    dfx = df3.sort_values('data')
    dfx = dfx.drop_duplicates()
    dfx.reset_index(drop=True, inplace=True)
    st.markdown("##### Choose a brand id from the brand list given below, by pressing on the + button. For eg. BMW corresponds to Id : 0")
    dfx.rename(columns={'data1': 'Bike Brand','data':'Brand ID'}, inplace=True)
    st.dataframe(dfx)


    pred = lr.predict(val)[0]
    pred = round(pred)
    if st.button("Predict"):
        st.success(f"Your predicted premium price is Rs. {pred}")


elif nav == "Four-Wheeler-Light":

    data = pd.read_csv("car_price_prediction.csv")
    data1 = data.copy()
    label_encoder = preprocessing.LabelEncoder()
    data['Manufacturer']= label_encoder.fit_transform(data['Manufacturer'])
    data['Manufacturer'].unique()
    lr = LinearRegression()
    Z = data[['Engine volume','Milage','Cylinders','Airbags','Manufacturer']]
    lr.fit(Z, data['Price'])
    st.image("car.jpeg",width= 800)
    st.header("Light Four Wheeler Insurance Premium")
    val1 = st.number_input("Enter your Vehicle's Engine Volume",100,2000,step = 100)
    val2 = st.number_input("Enter your Vehicle's Mileage",100,4000,step = 100)
    val3 = st.number_input("Enter your Vehicle's Cylinders",1,8,step = 1)
    val4 = st.number_input("Enter the number of Airbags",1,20,step=1)
    val5 = st.number_input("Enter your Vehicle's Manufacturer",1,63,step = 1)

    val = np.array([val1,val2,val3,val4,val5]).reshape(1,-1)
    
    datax = [data1["Manufacturer"], data["Manufacturer"]]
    headers = ["data1", "data"]
    df3 = pd.concat(datax, axis=1, keys=headers)
    dfx = df3.sort_values('data')
    dfx = dfx.drop_duplicates()
    dfx.reset_index(drop=True, inplace=True)
    st.markdown("##### Choose a brand id from the brand list given below, by pressing on the + button. For eg. BMW corresponds to Id : 0")
    dfx.rename(columns={'data1': 'Manufacturer','data':'Manufacturer ID'}, inplace=True)
    st.dataframe(dfx)


    pred = lr.predict(val)[0]
    pred = round(pred)/(-10)
    if st.button("Predict"):
        st.success(f"Your predicted premium price is Rs. {pred}")

elif nav == "Four-Wheeler-Heavy":

    data = pd.read_csv("bikes.csv")
    data1 = data.copy()
    label_encoder = preprocessing.LabelEncoder()
    data['brand']= label_encoder.fit_transform(data['brand'])
    data['brand'].unique()
    lr = LinearRegression()
    Z = data[['power', 'age', 'kms_driven','stroke','brand']]
    lr.fit(Z, data['price'])
    st.image("truck.jpeg",width= 800)
    st.header("Commercial Four Wheeler Insurance Premium")
    val1 = st.number_input("Enter your Bike's Horsepower",100,2000,step = 100)
    val2 = st.number_input("Enter your Bike's Age (years)",1,40,step = 1)
    val3 = st.number_input("Enter your Bike's Kilometers Travelled (in 1000 km)",1,50,step = 1)
    val4 = st.number_input("Enter your Bike's Stroke",1,5,step = 1)
    val5 = st.number_input("Enter your Bike's Brand",0,22,step = 1)

    val = np.array([val1,val2,val3,val4,val5]).reshape(1,-1)
    
    datax = [data1["brand"], data["brand"]]
    headers = ["data1", "data"]
    df3 = pd.concat(datax, axis=1, keys=headers)
    dfx = df3.sort_values('data')
    dfx = dfx.drop_duplicates()
    dfx.reset_index(drop=True, inplace=True)
    st.markdown("##### Choose a brand id from the brand list given below, by pressing on the + button. For eg. BMW corresponds to Id : 0")
    dfx.rename(columns={'data1': 'Bike Brand','data':'Brand ID'}, inplace=True)
    st.dataframe(dfx)


    pred = lr.predict(val)[0]
    pred = round(pred)
    if st.button("Predict"):
        st.success(f"Your predicted premium price is Rs. {pred}")


