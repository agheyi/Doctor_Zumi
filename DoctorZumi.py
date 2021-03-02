#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from zumi.zumi import Zumi
import time
import socket
from zumi.util.screen import Screen

zumi = Zumi()
screen = Screen()
screen.happy()

while True:
    full_msg = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'XXX.XXX.XX.XX' # ADD HOST IP HERE

    s.connect((host, 5560))

    full_msg = str(full_msg)
    while True:
        msg = s.recv(40)
        full_msg += msg.decode("utf-8")
        if full_msg == "Wearing":
            screen.draw_text("Thank you for     wearing you       mask")
            zumi.play_note(26, 150)
            zumi.play_note(26, 250)
            zumi.play_note(27, 500)
            zumi.play_note(28, 150)
            zumi.play_note(29, 250)
            zumi.play_note(30, 500)
            zumi.play_note(37, 250)
        elif full_msg == "Not wearing":
            screen.draw_text("Please take and  wear a mask     from here")
            zumi.play_note(30, 500)
            zumi.play_note(29, 500)
            zumi.play_note(28, 1000)
        elif full_msg == "bleh":
            screen.clear_display()
        break
    s.close()


# In[ ]:





# In[ ]:




