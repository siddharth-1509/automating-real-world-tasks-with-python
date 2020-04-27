#!/usr/bin/env python3

import os
import datetime
import reports
#import emails

def get_data():
    s=''
    for root, dirs, files in os.walk("supplier-data/descriptions/"):
        path = root.split(os.sep)
        for file in files:
            temp='supplier-data/descriptions/'+file
            print(file)
            f=open(temp,'r')
            a=f.readlines()
            f.close()
            s=s+ 'name: '+str(a[0].strip())+'<br/>'+'weight: '+str(a[1].strip())+'<br/><br/>'
    print(s)
    return s

def main():
    paragraph = get_data()
    today = datetime.date.today().strftime("%B %d, %Y")
    title = "Processed Update on {}".format(today)
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)
    count=paragraph.count('<br/>')
    paragraph=paragraph.replace('<br/>','\n',count)
    email = emails.generate_email("automation@example.com", "student-01-03b4255ed51c@example.com",
     "Upload Completed - Online Fruit Store", 
     "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",attachemnt)
    emails.send_email(email)


if __name__ == "__main__":
    main()

