# SMS Sending System

This is a simple SMS sending system built in Python using the Tkinter GUI library. The system allows users to load a CSV file, select recipients based on categories, and send SMS messages.

## Features

- Load CSV file with user data.
- Select recipients based on categories.
- Send SMS messages to selected recipients.
- View the delivery status of sent messages.



Usage

    Run the application:

```python
    python main.py
```

    Alternatively, you can generate a standalone executable (exe) file using PyInstaller. Open a terminal and run:
    
```python
    
    pyinstaller --onefile --noconsole main.py
```python

    Load a CSV file using the "Load File" button.

    Select a column and category for SMS recipients.

    Enter your SMS message.

    Click the "Send Message" button to send SMS messages.

    View the delivery status in the console or check details using the "Details" button.

Configuration

    The API key for sending SMS messages is stored in the config.ini file. You can update it through the settings.

Contributing

Feel free to open issues and submit pull requests to help improve the project.
