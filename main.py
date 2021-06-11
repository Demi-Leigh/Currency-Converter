# Creating a currency converter using tkintker
# and requests

import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Function to convert the currency
def convert():
    try:
        url = "https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/" + currency_ent.get()
        rates = requests.get(url).json()
        conversion = int(amount_ent.get()) * rates["conversion_rates"]["USD"]
        lbl_result.config(text=conversion)
    except:
        messagebox.showerror("Error", "No internet connection")


# Function to clear currency and amount
def clear():
    currency_ent.delete(0, END)
    amount_ent.delete(0, END)
    lbl_result.config(text=" ")


# Creating the window as well as adding a bg colour and title

window = Tk()
window.title("CURRENCY CONVERTER ")
window.geometry("500x300")
window.config(bg="yellow")
window.resizable(0, 0)


# Labels and Entry boxes to input currencies and amounts
lbl_currency = tk.Label(window, text="CURRENCY: ",  bg="yellow")
lbl_currency.grid(row=0, column=1, padx=20, pady=20,)

currency_ent = tk.Entry(window)
currency_ent.grid(row=0, column=2, padx=20, pady=20)

lbl_amount = tk.Label(window, text="ENTER THE AMOUNT: ",  bg="yellow")
lbl_amount.grid(row=1, column=1, padx=20, pady=20)
lbl_result = tk.Label(window, bg="yellow")
lbl_result.grid(row=5, column=1, padx=20, pady=20)

amount_ent = tk.Entry(window)
amount_ent.grid(row=1, column=2, padx=20, pady=20)

clear_btn = tk.Button(window, text="CLEAR", command=clear, width=10, fg="red", relief="raised", borderwidth=4)
clear_btn.grid(row=4, column=1, pady=20)

convert_btn = tk.Button(window, text="CONVERT", command=convert, width=10, fg="green", relief="raised", borderwidth=4)
convert_btn.grid(row=4, column=2, padx=20, pady=20)


window.mainloop()

