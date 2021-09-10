import tkinter as tk
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

root = tk.Tk()
root.title("Phone Number Info Finder")
root.geometry("300x300")

head = tk.Label(root, text= "Phone Info Finder",padx = 30, pady = 10)
head.grid(row = 0, column = 0 )

inp = tk.Entry(root,width = 40)
inp.grid(column = 0, row = 1,padx = 30,pady = 10,columnspan = 1)

def printinfo():
    global inp
    phone = inp.get()
    phone = phonenumbers.parse(phone)
    tk.Label(root, text = timezone.time_zones_for_number(phone)).grid(row = 4, column = 0)
    tk.Label(root, text = (carrier.name_for_number(phone,"en"))).grid(row = 5, column = 0)
    tk.Label(root, text = geocoder.description_for_number(phone,'en')).grid(row = 6, column = 0)
    tk.Label(root, text = ("Valid" if phonenumbers.is_valid_number(phone) else "Invalid")).grid(row = 7, column =0)

btn = tk.Button(root, text = "FIND", bg = "black", fg='white',height=1,width=5, command = lambda:printinfo())
btn.grid(column = 0, row = 2,padx = 30,pady = 10,columnspan = 1)

root.mainloop()