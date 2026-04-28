import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import pandas as pd
import joblib

# -----------------------------------
# To load the expiry risk prediction model
# -----------------------------------
model = joblib.load(r"C:\Users\DELL\Downloads\Internship Project\Module 2\expiry_risk_prediction_model.pkl")
labels = ["Low", "Medium", "High"]

# -----------------------------------
# For the prediction function
# -----------------------------------
def predict():
    try:
        stock = int(entry_stock.get())
        sales_velocity = float(entry_sales.get())

        expiry_date = pd.to_datetime(entry_expiry.get())
        user_today = pd.to_datetime(entry_today.get())

        # To get the calculations
        days_remaining = (expiry_date - user_today).days
        days_remaining = max(days_remaining, 0)

        stock_cover = stock / sales_velocity
        estimated_sales = sales_velocity * days_remaining
        unsold = max(stock - estimated_sales, 0)

        # To get the prediction
        features = [[stock, sales_velocity, days_remaining, stock_cover]]
        prediction = model.predict(features)
        risk_label = labels[prediction[0]]

        # Show suggested actions
        if risk_label == "High":
            action = "Remove"
            color = "#c0392b"   # red
        elif risk_label == "Medium":
            action = "Promotion"
            color = "#d68910"   # orange
        else:
            action = "Discount"
            color = "#1e8449"   # green

        # To get the output
        lbl_days.config(text=f"Days Remaining: {days_remaining}", fg="black")
        lbl_unsold.config(text=f"Unsold Quantity: {int(unsold)}", fg="black")
        lbl_risk.config(text=f"Risk Level: {risk_label}", fg=color)
        lbl_action.config(text=f"Suggested Action: {action}", fg=color)

    except:
        messagebox.showerror("Error", "Please enter valid inputs")

# -----------------------------------
# To set the user interface
# -----------------------------------
root = tk.Tk()
root.title("Expiry Risk Prediction")
root.geometry("550x650")


root.configure(bg="#B22222")

# For the Header
tk.Label(root,
         text="Expiry Risk Prediction System",
         font=("Arial", 20, "bold"),
         bg="#B22222",
         fg="white").pack(pady=15)

# -----------------------------------
# For the input and output card color
# -----------------------------------
card_color = "#f1c40f"

# -----------------------------------
# To set the input card
# -----------------------------------
input_card = tk.Frame(root, bg=card_color, bd=2, relief="ridge")
input_card.pack(padx=25, pady=10, fill="both")

tk.Label(input_card,
         text="Enter Product Details",
         font=("Arial", 14, "bold"),
         bg=card_color,
         fg="black").grid(row=0, columnspan=2, pady=10)

label_style = {"bg": card_color, "fg": "black", "font": ("Arial", 10, "bold")}

tk.Label(input_card, text="Product ID", **label_style).grid(row=1, column=0, sticky="w", padx=10)
entry_pid = tk.Entry(input_card)
entry_pid.grid(row=1, column=1, pady=5)

tk.Label(input_card, text="Batch Number", **label_style).grid(row=2, column=0, sticky="w", padx=10)
entry_batch = tk.Entry(input_card)
entry_batch.grid(row=2, column=1, pady=5)

tk.Label(input_card, text="Manufacturing Date", **label_style).grid(row=3, column=0, sticky="w", padx=10)
entry_mfg = DateEntry(input_card, date_pattern='yyyy-mm-dd')
entry_mfg.grid(row=3, column=1, pady=5)

tk.Label(input_card, text="Expiry Date", **label_style).grid(row=4, column=0, sticky="w", padx=10)
entry_expiry = DateEntry(input_card, date_pattern='yyyy-mm-dd')
entry_expiry.grid(row=4, column=1, pady=5)

tk.Label(input_card, text="Current Stock", **label_style).grid(row=5, column=0, sticky="w", padx=10)
entry_stock = tk.Entry(input_card)
entry_stock.grid(row=5, column=1, pady=5)

tk.Label(input_card, text="Sales Velocity (units/day)", **label_style).grid(row=6, column=0, sticky="w", padx=10)
entry_sales = tk.Entry(input_card)
entry_sales.grid(row=6, column=1, pady=5)

tk.Label(input_card, text="Current Date", **label_style).grid(row=7, column=0, sticky="w", padx=10)
entry_today = DateEntry(input_card, date_pattern='yyyy-mm-dd')
entry_today.grid(row=7, column=1, pady=5)

# For the button
tk.Button(root,
          text="Predict",
          command=predict,
          bg="#1d4ed8",
          fg="white",
          font=("Arial", 13, "bold"),
          width=18,
          height=2).pack(pady=20)

# -----------------------------------
# For setting up the output card
# -----------------------------------
output_card = tk.Frame(root, bg=card_color, bd=2, relief="ridge")
output_card.pack(padx=25, pady=10, fill="both")

tk.Label(output_card,
         text="Prediction Results",
         font=("Arial", 14, "bold"),
         bg=card_color,
         fg="black").pack(pady=10)

lbl_days = tk.Label(output_card, text="", bg=card_color, fg="black", font=("Arial", 12))
lbl_days.pack(pady=5)

lbl_unsold = tk.Label(output_card, text="", bg=card_color, fg="black", font=("Arial", 12))
lbl_unsold.pack(pady=5)

lbl_risk = tk.Label(output_card, text="", bg=card_color, font=("Arial", 13, "bold"))
lbl_risk.pack(pady=5)

lbl_action = tk.Label(output_card, text="", bg=card_color, font=("Arial", 13, "bold"))
lbl_action.pack(pady=5)

# For the footer
tk.Label(root,
         text="ERP Module - Herbal Industry",
         bg="#B22222",
         fg="#eeeeee",
         font=("Arial", 9)).pack(pady=10)

# To run the prediction model
root.mainloop()


