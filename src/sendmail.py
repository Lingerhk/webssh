# -*- coding: utf-8 -*-

# project: 
# author: s0nnet
# time: 2017-01-03
# desc: webssh

import re
import logging
import smtplib

from tornado.options import options
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Semail:
    options.parse_config_file("webssh.conf")
    def __init__(self):
        
        self.userName = options.username
        self.passWord = options.password
        self.smtpAddr = options.smtpaddr
        self.smtpPort = options.smtpport
        self.fromAddr = options.fromaddr
        self.toAddrs = options.toaddrs
    
    def send_email(self, subject, text, timeout=30):
        
        bRet = True
        text = re.sub("\n", "<br>", text)
        
        msg = MIMEMultipart()
        msg["From"] = self.fromAddr
        msg["To"]   = self.toAddrs
        msg['Subject']  = subject
        msg.attach(MIMEText(text, 'html', 'utf-8'))
        
        message = msg.as_string()
        try:
            s = smtplib.SMTP(host=self.smtpAddr, timeout=timeout)
            
            s.ehlo()
            if s.has_extn('STARTTLS'):
                s.starttls()
                s.ehlo()
                
            s.login(self.userName, self.passWord)
            s.sendmail(self.fromAddr, self.toAddrs.split(","), message)
            s.quit()
            logging.info("send email success!")
        except Exception, e:
            logging.error("send email error: %s" %(str(e)))
            bRet = False
        
        return bRet
    

if __name__ == "__main__":
    try:
        email = Semail()
        email.send_email("test", "<table border=1> <tr> <td> ===test=== </td> </tr> </table>") 
    except Exception, e:
        print e
    
    
