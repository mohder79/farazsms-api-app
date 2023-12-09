__version__ = "1.0.0"
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import re
import webbrowser
import requests
import json  
from tkinter import PhotoImage  
import requests
import json
import configparser
import os
import configparser


# Global variables
global name_and_last_name , number , status_description , message_id ,Load_File, api_key,sms
name_and_last_name = ''
number =''
status_description =''
message_id=''
Load_File = ''
api_key = ''
sms = ''
# Variable to track the current language
current_language = "Persian"
df = None  # DataFrame for CSV data
column_names = []  # List to store column names
category_selector = ""  # Currently selected category from selected column
user_text = ""  # masage Text entered by the user
selections_dict = {} # Dictionary to store selections user


class FarazSms:
    '''
    API documentation: https://docs.ippanel.com/
    '''

    def __init__(self, api_key):
        # Initialize the FarazSms class with the provided API key
        self.api_key = api_key
        self.base_url = 'https://api2.ippanel.com/api/v1/sms'
        self.headers = {
            "Content-Type": "application/json",
            "apikey": self.api_key,
        }

    def _make_request(self, method, endpoint, data=None):
        # Make a generic HTTP request to the specified endpoint with the given method
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=self.headers, data=data)

        # Check if the request was successful (status code 200)
        if response.status_code != 200:
            return {"error": f"Request failed with status code {response.status_code}"}

        # Return the JSON response if successful
        return response.json()

    def send_message(self, number: list, msg: str):
        # Send a single SMS message to the specified recipient numbers
        endpoint = 'send/webservice/single'
        payload = json.dumps({
            "sender": "+985000125475",  # Specify the sender number
            "recipient": number,
            "message": msg,  # Message content
            "description": {
                "summary": 'summary',  # Summary description
                "count_recipient": f"{len(number)}"  # Count of recipients
            },
        })
        return self._make_request("POST", endpoint, data=payload)

    def credit(self):
        # Retrieve the current account credit information
        endpoint = 'accounting/credit/show'
        try :
            credit =  int(self._make_request("GET", endpoint)['data']['credit'])
        except  : 
        #     if  current_language == "English" : 
        #         credit ='Error in internet or API.'
        # else : 
        #         credit = 'خطا در اینترنت یا api'
            credit = 'error'
        return  credit 

    def Delivery_check(self , bulk_id):
        '''
        Check the delivery status of a message with the given bulk ID
        
        The status key in response shows the last status of a recipient:
            2 => delivered
            4 => discarded
            1 => pending
            3 => failed
            0 => send
        '''
        endpoint = f'message/show-recipient/message-id/{bulk_id}'
        return self._make_request("GET", endpoint)


# Function to switch language
def switch_language():
    global current_language
    if current_language == "English":
        set_persian_language()
        current_language = "Persian"
    else:
        set_english_language()
        current_language = "English"

# Function to set English language
def set_english_language():
    # Modify labels, buttons, or any text elements to English language
    file_label.config(text="Load File")
    browse_button.config(text="Load File")
    category_label.config(text="category")
    column_label.config(text="column")
    # result_label.config(text="Results")
    result_select_csv_file_label.config(text="")
    # message_text.delete("1.0", tk.END)
    # message_text.insert(tk.END, "Enter your message here...")
    save_button.config(text="Send Message")
    designer_label.config(text="Designed by mohder")
    version_label.config(text="Version 1.0.0")
    settings_button.config(text= "Settings" )
    credit_label.config(text=f"{str((sms.credit()))}credit : ")
    
    
    # Global variables for messages
    global File_loaded, file_empty_error, file_loaded_success, file_not_found_error, file_loaded_message
    global internet_api_error, send_status, pending_status, delivered_status, failed_status, discarded_status
    global status_details_format, file_not_loaded_error, select_column_error, select_category_error , Load_File
    global enter_message_error, select_user_error, message_sent_success, send_message_error , file_read_error 

    # English messages for file loading
    Load_File = 'Load'
    File_loaded = "File loaded"
    file_empty_error = "File is empty."
    file_loaded_success = "File loaded successfully."
    file_not_found_error = "File not found."
    file_loaded_message = "File loaded."
    file_read_error = "Error reading file"

    # English messages for SMS sending status
    internet_api_error = 'Error in internet or API.'
    send_status = "Sending"
    pending_status = "Pending"
    delivered_status = "Delivered"
    failed_status = "Failed"
    discarded_status = "Discarded"
    # English format for displaying status details
    status_details_format = f'{name_and_last_name} -- {number} -- Status: {status_description}\n'

    # English messages for user actions
    file_not_loaded_error = "File not loaded."
    select_column_error = "Select a column."
    select_category_error = "Select a category."
    enter_message_error = "Enter the message to send."
    select_user_error = "No user selected."
    message_sent_success = f"Message sent. Tracking code: {message_id}"
    send_message_error = "Error in sending message."


# Function to set Persian language
def set_persian_language():
    # Modify labels, buttons, or any text elements to Persian language
    file_label.config(text="بارگذاری فایل")
    browse_button.config(text="بارگذاری فایل")
    category_label.config(text="دسته بندی")
    column_label.config(text="ستون")
    # result_label.config(text="نتایج")
    result_select_csv_file_label.config(text="")
    # message_text.delete("1.0", tk.END)
    # message_text.insert(tk.END, "پیام خود را وارد کنید...")
    save_button.config(text="ارسال پیام")
    designer_label.config(text="طراحی شده توسط mohder")
    version_label.config(text="نسخه 1.0.0")
    settings_button.config(text= "تنظیمات" )
    credit_label.config(text=f"{str((sms.credit()))}: موجودی")
    
    
    # Global variables for messages
    global File_loaded, file_empty_error, file_loaded_success, file_not_found_error, file_loaded_message
    global internet_api_error, send_status, pending_status, delivered_status, failed_status, discarded_status
    global status_details_format, file_not_loaded_error, select_column_error, select_category_error ,Load_File
    global enter_message_error, select_user_error, message_sent_success, send_message_error , file_read_error_name
    
    # Messages for file loading
    Load_File = 'بارگذاری'
    File_loaded = "فایل بارگذاری شد"
    file_empty_error = "فایل خالی است"
    file_loaded_success = "فایل با موفقیت بارگذاری شد"
    file_not_found_error = "فایل یافت نشد"
    file_loaded_message = "فایل بارگذاری شد."
    file_read_error_name = "خطا در خواندن فایل"
    # Messages for SMS sending status
    internet_api_error = 'خطا در اینترنت یا api'
    send_status = "ارسال"
    pending_status = "در انتظار"
    delivered_status = "تحویل داده شد"
    failed_status = "شکست خورد"
    discarded_status = "کنار گذاشته شد"

    # Format for displaying status details
    status_details_format = f'{name_and_last_name} -- {number} -- وضعیت: {status_description}\n'

    # Messages for user actions
    file_not_loaded_error = "فایل بارگذاری نشده است"
    select_column_error = "یک ستون انتخاب کنید"
    select_category_error = "یک دسته بندی انتخاب کنید"
    enter_message_error = "پیام ارسالی را وارد کنید"
    select_user_error = "کاربری را انتخاب نکردید"
    message_sent_success = f"پیام ارسال شد کد پیگیری: {message_id}"
    send_message_error = "خطا در ارسال پیام"


def select_csv_file():
    '''
    Opens a file dialog to allow the user to select a CSV file.
    If a file is selected, it updates the file_entry widget with the selected file path and calls
    load_initial_data to load data from the selected file.
    '''
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv;*")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)
        load_initial_data(file_path)
        result_label.config(text=File_loaded)


def load_initial_data(csv_file_path):
    """
    Reads a CSV file specified by the csv_file_path.
    Extracts column names from the DataFrame (data_frame)
    and updates the values for the column_selector Combobox.
    """
    global df, column_names

    # Read CSV file
    try:
        df = pd.read_csv(csv_file_path)
        if df.empty:
            result_label.config(text=file_empty_error)
        else:
            result_label.config(text=file_loaded_success)
    except FileNotFoundError:
        result_label.config(text=file_not_found_error)
    except pd.errors.EmptyDataError:
        result_label.config(text=file_empty_error)
    except pd.errors.ParserError:
        result_label.config(text=file_read_error)

    # Extract column names
    column_names = [column for column in df.columns]

    # Update column selector dropdown values
    column_selector['values'] = column_names


def Filter_df_by_column_and_category(selected_column, category_selector):
    """
    This function filters the DataFrame based on the selected column and selected category
    and returns the resulting DataFrame.

    Parameters:
    - selected_column (str): The column in the DataFrame to filter.
    - category_selector (str): The category to filter by within the selected column.

    Returns:
    - pandas.DataFrame: The filtered DataFrame.

    Example:
    Filter_df_by_column_and_category('buy_column', 'Phone') returns a DataFrame containing rows
    where the 'buy_column' is equal to 'Phone'.
    """
    result = df[df[selected_column] == category_selector]
    return result



def Selected_Column(event=None):
    """
    This function is triggered when a column is selected from the column_selector.
    It displays all items in the selected column in Category_selector.
    """
    get_input_data()
    
    # Check if a column is selected
    if not selected_column:
        return  # Exit the function if no column is selected

    # Find all Category names in the selected column of the DataFrame (df)
    Category_names = list(set(df[selected_column]))

    # Update the values in the Category_selector dropdown with the Category names
    Category_selector['values'] = Category_names


def Selected_Category(event=None):
    """
    This function is triggered when a category is selected from the Category_selector.
    It displays all items in the selected column have your selected Category in result_listbox
    """

    get_input_data()
    
    # Check if a category is selected
    if not selected_category:
        return  # Exit the function if no category is selected

    try:
        # use Filter_df_by_column_and_category function to get filtered data by column and category
        result_values = Filter_df_by_column_and_category(selected_column, selected_category)  
        
        # Clear the contents of the result_listbox
        result_listbox.delete(0, tk.END)

        # insert filtered data and format the values for display in the result_listbox
        for i, row in result_values.iterrows():
            # Create a formatted string with name, last name, and mobile number
            value = f"{row['اطلاعات هویتی (نام)']} -- {row['اطلاعات هویتی (نام خانوادگی)']} -- +98{row['شماره موبایل']}"
            
            # Insert the formatted string into the result_listbox
            result_listbox.insert(tk.END, value)  
    except Exception as e:
        # Handle exceptions (it just ignores them)
        pass  


def get_input_data():
    '''
     This function retrieves the selected column and category from their respective dropdowns.
    '''
    
    # Declare selected_column and selected_category as global variables
    global selected_column
    global selected_category
    global entered_message_text
    global selected_user
    
    # Get the selected item from the column_selector dropdown
    selected_column = column_var.get() 
    
    # Get the selected item from the category_selector dropdown
    selected_category = Category_var.get()
    
    # Get the text entered in the message_text 
    entered_message_text = message_text.get("1.0", tk.END).strip()
    
    # Get the selected index from the result_listbox
    selected_user = result_listbox.curselection()
    

def Sending_Status(id , bool):
    """
    Opens a new window with additional Sending Status details.
    """
    print(bool)
    def Update_Status(id , bool):
        
        # Get delivery details using the SMS API or use sample data
        try : 
            response_data = sms.Delivery_check(id)['data']['deliveries']
            print(response_data)
        except :
            details_text.insert(tk.END, internet_api_error)
            return
            

        # Clear the existing details_text content
        details_text.delete(1.0, tk.END)

        # Map numeric status codes to text descriptions
        status_mapping = {
            0: send_status,
            1: pending_status,
            2: delivered_status,
            3: failed_status,
            4: discarded_status,
        }
        # Insert delivery details into the Text widget with status descriptions
        for i in range(len(response_data)):
            number =  response_data[i]['recipient']
            status_code = response_data[i]["status"]
            status_description = status_mapping.get(status_code, status_details_format)
            
            
            try:
                # Find the index of the specified phone number
                index = selected_user['numbers'].index(' '+ number)
                name_and_last_name = f'{str(selected_user["names"][index])} {str(selected_user["last_names"][index])}'
            except ValueError:
                name_and_last_name = 'nan nan'
                        
            
            details_text.insert(tk.END, status_details_format)
        # Schedule the update_details function to be called again after 30 seconds
        print('wwww')
        if bool : 
            print('vvvv')
            details_window.after(100000, Update_Status(id , False))
        
        
    details_window = tk.Toplevel(root)
    details_window.title("جزئیات ارسال")

    # Create a Text widget to display details
    details_text = tk.Text(details_window, wrap=tk.WORD, width=90, height=60)
    details_text.pack()

    # Call the update_details function to initiate the periodic updates
    Update_Status(id , bool)  # Pass the desired ID or use a variable based on your logic



def Send_sms():
    """
    send an SMS with the selected numbers and text. and give the message_id
    """
    global selected_user
    
    # Call get_input_data() to retrieve selected_column and selected_category
    get_input_data()
    

    print(category_selector)

    try :
        # Check if the dataframe 'df' exists; if not, display an error message
        if not df :
            save_label.config(text=file_not_loaded_error)
            return  
    except Exception as e:
        # Handle exceptions (ignores them for now)
        pass  
    
    # Check if a column is selected
    if not selected_column:
        save_label.config(text=select_column_error)
        return
    
    # Check if a category is selected
    if not selected_category:
        save_label.config(text=select_category_error)
        return
    
    # Check if a message is entered
    if not entered_message_text:
        save_label.config(text=enter_message_error)
        return

    # Check if not select any user 
    if not selected_user:
        save_label.config(text=select_user_error)
        return

  # use selected_user indexs to made list of selcted number name and last name
    selected_values = [result_listbox.get(index) for index in selected_user]

    # dict for selsecd user data to seprad name,last name and number to send sms
    selected_user = {'names' : [],'last_names' : [],'numbers' : []}
    
    for users in selected_values:
        user = str(users).split('--')
        selected_user['names'].append(user[0])
        selected_user['last_names'].append(user[1])
        selected_user['numbers'].append(user[2])
        
    # Simulate sending a message and receiving a response (replace this with actual SMS sending code)
    # response_data = {'status': 'OK', 'code': 200, 'error_message': '', 'data': {'message_id': 606240441}}
    
    # sending a message and receiving a response
    response_data = sms.send_message(selected_user['names'] , entered_message_text)
    
    # Check the response status and code
    if response_data.get('status') == 'OK' and response_data.get('code') == 200:
        data = response_data.get('data', {})
        message_id = data.get('message_id')
        print(message_id)
        
        # Display success message with the message_id
        if message_id is not None:
            save_label.config(text=message_sent_success)
            Sending_Status(message_id , False)
        else:
            save_label.config(text=send_message_error)
    else:
        save_label.config(text=send_message_error)



def open_settings():
    """
    Opens a new window for API application settings.
    """
    # Declare save_settings_label as a global variable
    global save_settings_label
    
    # Create a new window for settings
    settings_window = tk.Toplevel(root)
    settings_window.title("تنظیمات")

    # Label and entry for API key
    api_key_label = tk.Label(settings_window, text="API Key:")
    api_key_label.grid(row=0, column=0, padx=10, pady=10)

    # Entry widget for entering the API key 
    api_key_entry = tk.Entry(settings_window)
    api_key_entry.grid(row=0, column=1, padx=10, pady=10)

    # Save button for settings
    save_settings_button = tk.Button(settings_window, text="Save", command=lambda: save_settings(api_key_entry.get()))
    save_settings_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Label for displaying API status
    save_settings_label = tk.Label(settings_window, text="")
    save_settings_label.grid(row=2, column=0, columnspan=2, pady=10)


def save_settings(api_key):
    """
    Save the API key in your settings.
    """
    # Open the configuration file for writing
    with open('config.ini', 'w') as configfile:
        # Create a ConfigParser object
        config = configparser.ConfigParser()

        # Add a section 'Settings' and set the 'api_key' option to the provided API key
        config['Settings'] = {'api_key': f'{api_key}'}

        # Write the configuration to the file
        config.write(configfile)

    # Update the label to indicate that settings have been saved
    save_settings_label.config(text="تنظیمات ذخیره شد")
    api_status.config(text="", justify="left")


def on_startup():
    """
    Function to be called at application startup.
    """
    # Check if the config file already exists
    config_file_path = 'config.ini'
    if not os.path.exists(config_file_path):
        # If it doesn't exist, create and write the default configuration
        with open(config_file_path, 'w') as configfile:
            config = configparser.ConfigParser()
            config['Settings'] = {'api_key': 'None'}
            config.write(configfile)

    # Read the configuration
    config = configparser.ConfigParser()
    config.read(config_file_path)

    # Get the 'api_key' value from the configuration
    api_key = config.get('Settings', 'api_key')

    if api_key == 'None':
        # If 'api_key' is 'None', update the status and open settings
        api_status.config(text="API را در تنظیمات وارد کنید", justify="left")
        open_settings()



# Run the on_startup function when the application starts
# { program ui 
root = tk.Tk()
root.title("سامانه ارسال SMS")  # App name
root.geometry("750x800")

# Load the settings icon and resize it to 32x32 pixels
settings_icon = PhotoImage(file="settings_icon.png")
resized_settings_icon = settings_icon.subsample(15, 15)  # Adjust the subsample values as needed

# Button for settings with the resized icon
settings_button = tk.Button(root, command=open_settings, image=resized_settings_icon, compound=tk.LEFT)
settings_button.grid(row=0, column=0, padx=10, pady=10)

# Display the account credit
credit_label = tk.Label(root)
credit_label.grid(row=0, column=2, columnspan=1, padx=10, pady=10)

# Label for Load CSV File
file_label = tk.Label(root)
file_label.grid(row=1, column=0, padx=10, pady=10)

file_entry = tk.Entry(root, width=60)
file_entry.grid(row=1, column=1, padx=10, pady=10)

# Button to browse and load CSV file
browse_button = tk.Button(root, command=select_csv_file )
browse_button.grid(row=1, column=2, padx=10, pady=10)

# Label for displaying results browse file label
result_select_csv_file_label = tk.Label(root, text="")
result_select_csv_file_label.grid(row=1, column=3, columnspan=3, padx=10, pady=10)

# Label and dropdown for category selection
column_label = tk.Label(root)
column_label.grid(row=2, column=0, padx=10, pady=10)

column_var = tk.StringVar()
column_selector = ttk.Combobox(root, textvariable=column_var, width=60)
column_selector.grid(row=2, column=1, padx=10, pady=10)

Category_var = tk.StringVar()
Category_selector = ttk.Combobox(root, textvariable=Category_var, width=60)
Category_selector.grid(row=3, column=1, padx=10, pady=10)

# Label and dropdown for category selection
category_label = tk.Label(root)
category_label.grid(row=3, column=0, padx=10, pady=10)

# Label for displaying results
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=1, columnspan=3, padx=10, pady=10)

# Listbox for displaying results with multiple selection capability
result_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=10, width=50)
result_listbox.grid(row=6, column=1, padx=10, pady=10)

# Text widget for entering message text
message_text = tk.Text(root, height=10, width=50)
message_text.grid(row=7, column=1, padx=10, pady=10)

# Button to save selected items and trigger message sending
save_button = tk.Button(root, command=Send_sms)
save_button.grid(row=8, column=1, padx=10, pady=10)

# Label for displaying save status or messages
save_label = tk.Label(root, text="")
save_label.grid(row=9, column=1, padx=10, pady=10)

# Label for designer attribution
designer_label = tk.Label(root)
designer_label.grid(row=10, column=2, padx=10, pady=10)

# Label for version
version_label = tk.Label(root, text="version 1.0.0")
version_label.grid(row=10, column=0, padx=10, pady=10)

# Label for clickable link
link_label = tk.Label(root, text="dr-jalilmokhtar.ir", fg="blue")
link_label.grid(row=10, column=1, padx=10, pady=10)

# Add the click event to the link
def open_link(event):
    webbrowser.open("http://dr-jalilmokhtar.ir/")

link_label.bind("<Button-1>", open_link)

# Label for displaying API status
api_status = tk.Label(root, text="")
api_status.grid(row=0, column=1, columnspan=3, padx=10, pady=10)


# Button for language switch
language_button = tk.Button(root, text="Switch Language", command=switch_language)
language_button.grid(row=0, column=1, padx=10, pady=10)

# ... (remaining code)

# Configure the appearance of the GUI with the default language (English)



# Bind the selected events to the respective functions
column_selector.bind("<<ComboboxSelected>>", Selected_Column)
Category_selector.bind("<<ComboboxSelected>>", Selected_Category)


# Configure the appearance of the GUI

# Main background color of the program (Light Gray)
root.configure(bg="#C0C0C0")

# File label settings
file_label.configure(bg="#C0C0C0", fg="#1E1E1E", font=("Arial", 12, "bold"))

# Category label settings
category_label.configure(bg="#C0C0C0", fg="#1E1E1E", font=("Arial", 12, "bold"))

# column label settings
column_label.configure(bg="#C0C0C0", fg="#1E1E1E", font=("Arial", 12, "bold"))

# Result label settings
result_label.configure(bg="#C0C0C0", fg="#1E1E1E", font=("Arial", 12, "bold"))

# Result browse file label settings
result_select_csv_file_label.configure(bg="#C0C0C0", fg="#1E1E1E", font=("Arial", 12, "bold"))

# Text widget settings
message_text.configure(bg="#FFFFFF", fg="#1E1E1E", font=("Arial", 10))

# Result listbox settings
result_listbox.configure(bg="#FFFFFF", fg="#1E1E1E", font=("Arial", 10))

# Save button settings
save_button.configure(bg="#4CAF50", fg="#FFFFFF", font=("Arial", 12, "bold"))

# Designer label settings
designer_label.configure(bg="#C0C0C0", fg="#1E1E1E", font=("Arial", 10, "italic"))

# Browse button settings
browse_button.configure(bg="#008CBA", fg="#FFFFFF", font=("Arial", 12, "bold"))

# API status label settings
api_status.configure(bg="#C0C0C0", fg="red", font=("Arial", 12, "bold"))

# Selected background color in the result listbox
result_listbox.configure(selectbackground="#4CAF50")

on_startup()

config_file_path = 'config.ini'
# Read the configuration
config = configparser.ConfigParser()
config.read(config_file_path)

# Get the 'api_key' value from the configuration
api_key = config.get('Settings', 'api_key')

sms = FarazSms(api_key)

print(api_key)

set_english_language()

root.mainloop()



















