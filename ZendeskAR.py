log = str(input("Email: ")) 
pwd = str(input("Password: ")) #Password needs to be a Google App password if 2FA is enabled.

def autoSearch(login, password):

    import imaplib

    imapObj = imaplib.IMAP4_SSL('imap.gmail.com', 993) #IMAP Server info for Gmail
    imapObj.login(login, password)
    imapObj.select('"Auto Replied"') #Folder created in gmail that new tickets filter to.


    typ, data = imapObj.search(None, 'X-GM-RAW', 'is:unread')
    
    print(data)

    for x in data[0].split():
        typ, data = imapObj.fetch(x, '(RFC822)')
        print('Message %s\n%s\n' % ((x), data[0][1]))
        print("")
        import pyzmail
        msg = pyzmail.PyzMessage.factory(data[0][1])
        print("")
        ticket_rec = msg.get_addresses('reply-to')
        ticket_from = ticket_rec[0]
        ticket_id = ticket_from[1]
        print("reply-to: ", ticket_id)
        print("")
        ticket_sub = msg.get_subject()
        print(ticket_sub)

        autoReply(login, password, ticket_id, ticket_sub)

    imapObj.close()
    imapObj.logout()


def autoReply(login, password, ticket_id, ticket_sub):
    import smtplib

    toaddr = ticket_id

    fromaddr = login
    sig = "John Doe| IT Technician\n123-456-7890 | john.doe@companyxyz.com\n\n" #Format signature to your liking.
    
    #Creates your response -- {{ticket.requester.first_name}} is the first name of the person  that created the ticket in ZenDesk. ZenDesk as a way more that you can utilize as well.
    MESSAGE = "To: %s\r\nSubject: %s \r\nHi {{ticket.requester.first_name}},\n\nThank you for submitting a ticket through the companyxyz IT Portal. Your ticket has been received and we will begin working on it as soon as possible.\n\nThank you,\n\n%s" % (ticket_id, ticket_sub, sig)
    
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587) #SMTP Server info for Gmail

    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(login, password)

    smtpObj.sendmail(fromaddr, toaddr, MESSAGE)
    smtpObj.quit()

import time
import os
x = 1
y = 0
while (x == 1):
    autoSearch(log,pwd)
    y = y + 1
    time.sleep(60)
    os.system('clear')
    print(y) #Helps me keep track of how many times it has looped.
    print("")
