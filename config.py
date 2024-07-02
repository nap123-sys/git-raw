import tkinter as tk

print("hello")
print("please kill me")
# i am a horrible person for making this 
def button_clicked():
    print("Button clicked!")

root = tk.Tk()

button = tk.Button(root, text="Click me", command=button_clicked)
button.pack()

root.mainloop()