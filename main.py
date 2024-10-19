import pywhatkit as pwk
import tkinter
from tkinter import ttk
from tkinter import messagebox
from docxtpl import DocxTemplate
import datetime
import random
from docx2pdf import convert
import pandas as pd

window = tkinter.Tk()
window.title("CAFE - Billing System")
window.geometry('1024x768')
window.configure(bg='#f0f8ff')

# Configure grid weights to make the window resizable
window.columnconfigure(0, weight=1)
window.rowconfigure([1, 2], weight=1)

# Function to update time dynamically
def update_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute

date = f"{day}{month}{year}"
time = f"{hour}:{minute}"

# Top frame for Welcome Message and Date/Time
top_frame = tkinter.Frame(window, bg='#4682B4', padx=10, pady=10)
top_frame.grid(row=0, column=0, sticky="ew")

welcome_label = tkinter.Label(top_frame, text="Welcome to Billing System", bg='#4682B4', fg='white', font=("Arial", 16, "bold"))
welcome_label.pack(side="left", padx=10, pady=5)

time_label = tkinter.Label(top_frame, text="", bg='#4682B4', fg='white', font=("Arial", 14))
time_label.pack(side="right", padx=10, pady=5)

# Start the time update
update_time()

# Customer Information Frame
customer_frame = tkinter.LabelFrame(window, text="Customer Information", padx=10, pady=10, bg='#f0f8ff', font=("Arial", 12, "bold"))
customer_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

# Configure grid columns for customer information
customer_frame.columnconfigure([0, 1, 2], weight=1)

first_name_label = tkinter.Label(customer_frame, text="Name", bg='#f0f8ff', font=("Arial", 10, "bold"))
first_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
first_name_entry = tkinter.Entry(customer_frame)
first_name_entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

phone_number_label = tkinter.Label(customer_frame, text="Phone No.", bg='#f0f8ff', font=("Arial", 10, "bold"))
phone_number_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")
phone_number_entry = tkinter.Entry(customer_frame)
phone_number_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

billlabel = tkinter.Label(customer_frame, text="Billing Number", bg='#f0f8ff', font=("Arial", 10, "bold"))
billlabel.grid(row=0, column=2, padx=10, pady=5, sticky="w")
billentry = tkinter.Entry(customer_frame)
billentry.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

# Menu Frame
menu_frame = tkinter.LabelFrame(window, text="Menu", padx=10, pady=10, bg='#f0f8ff', font=("Arial", 12, "bold"))
menu_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

# Configure grid in menu frame
menu_frame.columnconfigure([0, 1, 2], weight=1)

# Load item data from an Excel sheet
df = pd.read_excel('billing_items.xlsx')
df.set_index('Item Name', inplace=True)
item_dict = df.to_dict(orient='index')
for item, data in item_dict.items():
    item_dict[item] = data['Price']

billnumber = random.randint(1000, 9999)

def clear_item():
    qty_spinbox_main.delete(0, tkinter.END)
    qty_spinbox_main.insert(0, "1")
    desc_label_box_main.set('')

invoice_list = []

def update_total():
    total_amount = sum(item[3] for item in invoice_list)
    total_label.config(text=f"Total: {total_amount} INR")

def add_item():
    global item_dict
    billentry.delete(0, "end")
    billentry.insert(0, billnumber)
    if first_name_entry.get() == "" or phone_number_entry.get() == "":
        messagebox.showerror("Error", "Customer Details are Required")
        return
    qty = int(qty_spinbox_main.get())
    desc = desc_label_box_main.get()
    if desc in item_dict:
        price = item_dict[desc]
    else:
        messagebox.showerror("Error", "Please add some item from the dropdown menu")
        return
    line_total = qty * price
    invoice_item = [desc, qty, price, line_total]
    tree.insert('', 0, values=invoice_item)
    clear_item()
    invoice_list.append(invoice_item)
    update_total()

def new_invoice():
    first_name_entry.delete(0, tkinter.END)
    phone_number_entry.delete(0, tkinter.END)
    clear_item()
    tree.delete(*tree.get_children())
    invoice_list.clear()
    update_total()

def generate_invoice():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M")
    
    name = first_name_entry.get()
    phone = phone_number_entry.get()
    subtotal = sum(item[3] for item in invoice_list)
#     salestax = 0.1
    total = subtotal # * (1 + salestax)
    
#     doc = DocxTemplate("invoice1.docx")
#     doc.render({
#         "name": name,
#         "phone": phone,
#         "invoice_list": invoice_list,
#         "subtotal": subtotal,
#         "salestax": f"{salestax * 100}%",
#         "total": total
#     })
#     doc_name = f"{name}{date}{time}.docx"
#     doc.save(doc_name)
#     convert(doc_name)
    
#    messagebox.showinfo("Success", f"Invoice generated and saved as {doc_name}")
    
    # Save to Excel
    df = pd.read_excel('billing_details.xlsx')
    serialNo = len(df) + 1
    new_row = {
        "Serial_number": serialNo, "Bill_number": billnumber, "Name": name, "Phone_number": phone,
        "Items": invoice_list, "Amount": total, "Date": date, "Time": time
    }
    df = df.append(new_row, ignore_index=True)
    df.to_excel('billing_details.xlsx', index=False)
    
#     # Send invoice via WhatsApp
#     send_invoice_via_whatsapp(phone, name, total)

def send_invoice_via_whatsapp():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute+2
    name = first_name_entry.get()
    phone = phone_number_entry.get()
    subtotal = sum(item[3] for item in invoice_list)
#     salestax = 0.1
    total = subtotal # * (1 + salestax)
    
    phonenumber = "+91"+str(phone)
    # Format the message
    message = f"Hello {name},\nitems are : \n{invoice_list}\nYour total bill is {total} INR.\nThank you for your purchase!"
    
    # Send message
    pwk.sendwhatmsg(phonenumber, message, hour , minute + 1)
def send_invoice_via_email():
    name = first_name_entry.get()
    phone = phone_number_entry.get()
    subtotal = sum(item[3] for item in invoice_list)
    total = subtotal  # If you plan to add sales tax, update this line
    recipient_email = "ayusharm4999@gmail.com"  # Replace with recipient's email

    # Email content
    email_subject = f"Invoice from CAFE - {name}"
    email_body = f"Hello {name},\n\nHere is your invoice:\n\nItems Purchased:\n"
    
    # Adding items to the email body
    for item in invoice_list:
        email_body += f"- {item[0]} (Qty: {item[1]}, Price: {item[2]} INR, Total: {item[3]} INR)\n"
    
    email_body += f"\nTotal Bill: {total} INR\n\nThank you for visiting CAFE!"

    # Create email message
    msg = MIMEMultipart()
    msg['From'] = "ayusharma4999@gmail.com"  # Replace with your email
    msg['To'] = recipient_email
    msg['Subject'] = email_subject

    # Attach the email body
    msg.attach(MIMEText(email_body, 'plain'))

    # Email credentials and sending logic
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("ayusharma4999@gmail.com", "Password")  # Replace with your email and password
        text = msg.as_string()
        server.sendmail("ayusharma4999@gmail.com", recipient_email, text)
        server.quit()
        messagebox.showinfo("Success", "Invoice sent successfully via email!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

def delete_item():
    selected_item = tree.selection()
    if selected_item:
        item_values = tree.item(selected_item, 'values')
        tree.delete(selected_item)
        for item in invoice_list:
            if item[0] == item_values[0] and item[1] == int(item_values[1]):
                invoice_list.remove(item)
                break
        update_total()

# Dropdown and spinbox for menu items in Menu Frame
desc_label_main = tkinter.Label(menu_frame, text="Main Course", bg='#f0f8ff', font=("Arial", 10, "bold"))
desc_label_main.grid(row=0, column=0, padx=10, pady=5, sticky="w")
desc_label_box_main = ttk.Combobox(menu_frame, values=list(item_dict.keys()))
desc_label_box_main.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

qty_label_main = tkinter.Label(menu_frame, text="Qty", bg='#f0f8ff', font=("Arial", 10, "bold"))
qty_label_main.grid(row=0, column=1, padx=10, pady=5, sticky="w")
qty_spinbox_main = tkinter.Spinbox(menu_frame, from_=1, to=10, increment=1)
qty_spinbox_main.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Add Item Button
add_item_button = tkinter.Button(menu_frame, text="Add Item", command=add_item, bg='#4682B4', fg='white')
add_item_button.grid(row=1, column=2, padx=10, pady=5, sticky="ew")

# Billing Frame
billing_frame = tkinter.LabelFrame(window, text="Billing Summary", padx=10, pady=10, bg='#f0f8ff', font=("Arial", 12, "bold"))
billing_frame.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

# Configure grid for billing frame
billing_frame.columnconfigure([0, 1], weight=1)

# TreeView to display selected items
columns = ("Description", "Qty", "Price", "Total")
tree = ttk.Treeview(billing_frame, columns=columns, show="headings")
tree.heading("Description", text="Description")
tree.heading("Qty", text="Qty")
tree.heading("Price", text="Price")
tree.heading("Total", text="Total")
tree.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

# Scrollbar for the TreeView
scrollbar = ttk.Scrollbar(billing_frame, orient="vertical", command=tree.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
tree.configure(yscrollcommand=scrollbar.set)

# Total label
total_label = tkinter.Label(billing_frame, text="Total: 0 INR", bg='#f0f8ff', font=("Arial", 12, "bold"))
total_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

# Button Frame
button_frame = tkinter.Frame(window, bg='#f0f8ff')
button_frame.grid(row=4, column=0, padx=20, pady=10, sticky="ewns")

# Invoice buttons
delete_button = tkinter.Button(button_frame, text="Delete Item", command=delete_item, bg='#ff6347', fg='white')
delete_button.grid(row=0, column=0, padx=10, pady=5)

new_invoice_button = tkinter.Button(button_frame, text="New Invoice", command=new_invoice, bg='#4682B4', fg='white')
new_invoice_button.grid(row=0, column=1, padx=10, pady=5)

generate_button = tkinter.Button(button_frame, text="Generate Invoice", command=generate_invoice, bg='#32cd32', fg='white')
generate_button.grid(row=0, column=2, padx=10, pady=5)

whatsapp_button = tkinter.Button(button_frame, text="WhatsApp", command=send_invoice_via_whatsapp, bg='#32cd32', fg='white')
whatsapp_button.grid(row=0, column=3, padx=10, pady=5)

email_button = tkinter.Button(button_frame, text="Email", command=send_invoice_via_email, bg='#32cd32', fg='white')
email_button.grid(row=0, column=4, padx=10, pady=5)

window.mainloop()
