__author__ = 'marcsantago'
#!/usr/bin/env python3
import tkinter

top = tkinter.Tk()
top.title("Python Phone Script Creator")
top.minsize(500, 300)

#phone number section
phone_frame = tkinter.Frame(top)
phone_frame.pack()
phone_label = tkinter.Label(phone_frame, text="Enter Your Phone Number No Dashes Or Spaces:")
phone_label.pack(padx=5, pady=0, side='left')
phone_entry = tkinter.Entry(phone_frame)
phone_entry.pack(padx=5, pady=0, side='left')


#cell phone provider
phone_provider_frame = tkinter.Frame(top)
phone_provider_frame.pack()
phone_provider_label = tkinter.Label(phone_provider_frame, text="Select Your Cellular Provider")
phone_provider_label.pack()
tmb = tkinter.Radiobutton(phone_provider_frame, text="T-Mobile", value=0)
tmb.pack()
ver = tkinter.Radiobutton(phone_provider_frame, text="Verizon", value=1)
ver.pack()
sprint = tkinter.Radiobutton(phone_provider_frame, text="Sprint", value=2)
sprint.pack()

#gmail
gmail_frame = tkinter.Frame(top)
gmail_frame.pack()
gmail_label = tkinter.Label(gmail_frame, text="Enter Your Gmail")
gmail_label.pack(padx=5, pady=0, side='left')
gmail_entry = tkinter.Entry(gmail_frame)
gmail_entry.pack(padx=5, pady=0, side='left')


top.mainloop()