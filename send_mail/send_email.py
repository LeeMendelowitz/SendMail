#!/usr/bin/env python
# encoding: utf-8
 
import smtplib
import pandas
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
def send(server, fromaddr, toaddr, subject,
                  text_msg = None, html_msg = None):    
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = fromaddr
    msg['To'] = toaddr
    
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    if text_msg:
        part1 = MIMEText(text_msg, 'plain')
        msg.attach(part1)

    if html_msg:
        part2 = MIMEText(html_msg, 'html')
        msg.attach(part2)
    
    # Send email
    server.sendmail(fromaddr, toaddr, msg.as_string())