class Notification:
    def send(self):
        return f"The notification has been sent !!"
    
class Email_Notification(Notification):
    def __init__(self,message_format):
        self.message_format= message_format
    def send(self):
        return f"The {self.message_format} notification has been sent !!"
    
class SMS_Notification(Notification):
    def __init__(self,message_format):
        self.message_format= message_format
    def send(self):
        return f"The {self.message_format} notification has been sent !!"
    
notification= Email_Notification("Email")
print(notification.send())
notification1= SMS_Notification("SMS")
print(notification1.send())