# Zendesk-Auto-Responder

The Zendesk Auto Responder was created because my company had disabled the auto response feature in Zendesk, therefore I turned to automation. Our Gmail is connected to Zendesk in this case. I am fairly new to coding, so I'm sure there is a better way to write this, however, it works as intended. Any suggestions on how to improve it are welcome.

***************************************************************************************************************************************** 
  
  How it works:
  
  1. A filter is used to filter all new tickets to a folder I created in Gmail called "Auto Replied".
  2. Using Python 3, the auto responder parses the "Auto Replied" folder for all unread messages.
  3. It then parses the contents of the email grabbing the contents of the reply-to (holds the unique ticket identifier) field and the           subject.
  4. Then it will respond to the ticket using a pre-coded response, the subject from the parsed email, and the reply-to field.
  5. The code then loops every minute.

Since the code is logging into your email and responding it bypasses any permissions that would otherwise keep you from using Zendesks APIs.

*****************************************************************************************************************************************
CAUTION!
*****************************************************************************************************************************************
Never save your credentials in plain text!
