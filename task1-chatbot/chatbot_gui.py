import tkinter as tk
import customtkinter as ctk
from responses import get_response

root=tk.Tk()
root.title("My Chatbot")
root.geometry("900x600")

myFont=("arial", 16)
bg_color="#2c2c2c"

chat_frame=ctk.CTkScrollableFrame(root, bg_color=bg_color, fg_color=bg_color)
chat_frame.pack(fill=tk.BOTH, expand=True)

input_val=tk.StringVar()

def get_prompt(event):
    message=input_val.get()
    if(message):
        show_prompt(message)
        response=get_response(message)
        show_response(response)
    input_val.set("")
        

def show_prompt(prompt):
    message_label=tk.Label(chat_frame, text=prompt, font=myFont, justify="right", bg="#1e4d2b", fg="white", wraplength=chat_frame.winfo_width()*0.75)
    message_label.pack(anchor="se", padx=5, pady=5)

def show_response(response):
    message_label=tk.Label(chat_frame, text=response, font=myFont, justify="left", bg="#1e3d58", fg="white", wraplength=chat_frame.winfo_width()*0.75)
    message_label.pack(anchor="sw", padx=5, pady=5)

def update_size(event):
    all_messages=chat_frame.winfo_children()
    for message in all_messages:
        message.configure(wraplength=chat_frame.winfo_width()*0.75)

chat_frame.bind("<Configure>", update_size)

input_frame=tk.Frame(root, bg="white")
input_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)
input_frame.grid_columnconfigure(0, weight=1)

input_bar=tk.Entry(input_frame, font=myFont, textvariable=input_val, borderwidth=0, )
input_bar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

submit_button=tk.Button(input_frame, text="Send", font=("arial", 16, "bold"), bg="blue", fg="white", borderwidth=0, padx=5, pady=5)
submit_button.grid(row=0, column=1)

input_bar.bind("<Return>", get_prompt)
submit_button.bind("<Button>", get_prompt)

root.mainloop()