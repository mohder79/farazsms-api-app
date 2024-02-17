
# About the Project

This Python module provides a simple wrapper for sending SMS messages using the FarazSms API. The FarazSms API allows you to send single SMS messages and check the delivery status of messages.


# Usage

Initialize FarazSms Object:

```python

from farazsms import FarazSms

api_key = "YOUR_API_KEY"
faraz_sms = FarazSms(api_key)
```

# Send SMS:

```python


recipient_numbers = ["123456789", "987654321"]
message_content = "Hello, this is a test message."

response = faraz_sms.send_message(recipient_numbers, message_content)
print(response)
```
# Check Account Credit:


```python


credit_info = faraz_sms.credit()
print(credit_info)
```
# Check Message Delivery Status:

```python


    bulk_id = "YOUR_BULK_ID"
    delivery_status = faraz_sms.Delivery_check(bulk_id)
    print(delivery_status)
```
# API Documentation

For detailed information about the FarazSms API, refer to the [official API documentation](https://docs.ippanel.com/). 

# Note

Make sure to replace "YOUR_API_KEY" and "YOUR_BULK_ID" with your actual FarazSms API key and bulk ID.








# درباره پروژه

این ماژول پایتون یک روش ساده برای ارسال پیام‌های اس ام اس با استفاده از ای پی ای فراز اس ام اس فراهم می‌کند. ای پی ای فراز اس ام اس به شما امکان ارسال پیام‌های تکی اس ام اس و بررسی وضعیت تحویل پیام‌ها را می‌دهد.
راهنمای استفاده
مقدمه

```python

from farazsms import FarazSms

api_key = "YOUR_API_KEY"
faraz_sms = FarazSms(api_key)
```
# ارسال پیام
```python

recipient_numbers = ["123456789", "987654321"]
message_content = "سلام، این یک پیام آزمایشی است."

response = faraz_sms.send_message(recipient_numbers, message_content)
print(response)
```
# بررسی اعتبار حساب
```python

credit_info = faraz_sms.credit()
print(credit_info)
```
# بررسی وضعیت تحویل پیام
```python


bulk_id = "YOUR_BULK_ID"
delivery_status = faraz_sms.Delivery_check(bulk_id)
print(delivery_status)
```
# مستندات 
API
برای اطلاعات دقیق در مورد API FarazSms به مستندات رسمی API مراجعه کنید.
توجه

حتماً "YOUR_API_KEY" و "YOUR_BULK_ID" را با کلید API و شناسه دسته جمعی FarazSms واقعی خود جایگزین کنید.








