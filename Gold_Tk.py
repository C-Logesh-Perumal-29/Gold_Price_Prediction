# Importing Library :
from tkinter import *
import tkinter as tk

# Create Object :
root = Tk()

# Title :
root.title("Gold Price Prediction")


# Setting icon :
icon = PhotoImage(file = 'icon.png') 
root.iconphoto(False, icon)

# Screen Size : 
root.geometry('300x500')

# Apply Background Image :
background_Image = PhotoImage(file = "Background.png")

# Show the Background Image Using Label :
label_for_bg = Label(root, image = background_Image)
label_for_bg.place(x = -2, y = -2)


# Importing Libraries for Trained Model :
import joblib 
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Load and Split the Data :
Dataset = pd.read_csv("D:\\Gold Price Prediction\\Gold rate.csv")

X = Dataset.iloc[37:,:1].values
Y = Dataset.iloc[37:,:1].values

# Pre-Processing the data :
Poly = PolynomialFeatures(degree=3)
X_Poly = Poly.fit_transform(X)

Poly.fit(X_Poly, Y)
LR_2 = LinearRegression()
LR_2.fit(X_Poly, Y)

# ---------------------------------------------------------------------------------------------------------------------------

Year = tk.IntVar()

def submit():
    Year_Value = Year.get()
    #print("Year : " , Year_Value)
    
    model = joblib.load("D:\\Gold Price Prediction\\Gold_Price_Model.pkl")
    Pred_Custom = model.predict(Poly.fit_transform([[Year_Value]]))
    #print("Gold Price : ",int(Pred_Custom))

    E_G = (Pred_Custom/10) * 8

    L_Price1 = Label(root, font=('Berlin Sans FB Demi',12,'normal'), text = f'10g Gold Price : {int(Pred_Custom)}')
    L_Price1.place(x=10, y=400)
    
    L_Price2 = Label(root, font=('Berlin Sans FB Demi',12,'normal'), text = f'8g Gold Price : {int(E_G)}')
    L_Price2.place(x=10, y=450)
  
# User Input :
e1 = Entry(root, textvariable = Year, font=('Cooper Black',13,'normal')).place(x = 48, y = 200)

# Button :
Sub_Btn = tk.Button(root, fg='black', bg='#FFD700', text = 'Submit', font=('Cooper Black',15,'normal'), command = submit)
Sub_Btn.pack(pady=240)



# Execute Tkinter :
root.mainloop()