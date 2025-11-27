import tkinter as tk
import random
import string

def generate_pass():
    try:
        length = int(length_entry.get()) #take input from the user
        if (length < 8):
            print("Password must be of minimum 8 characters!")
            result_entry.delete(0, tk.END)
            result_entry.insert(0, 'Minimum length is 8 characters!')
        else:
            character = (string.ascii_letters  +  string.punctuation +string.digits + string.ascii_uppercase) #characters to choose from
            password = ''.join(random.choice(character) for _ in range(length)) #generate password using for loop
            result_entry.insert(0, password)
            return password
    except    ValueError("Length should be minimum of 8 characters"):
        print(generate_pass())

root = tk.Tk()
root.title("Password Generator by Aamirz")
root.geometry("400x150")
root.resizable(False, False)

label = tk.Label(root, text = "Enter Password Length")
label.pack(pady=5)

length_entry = tk.Entry(root, width=10)
length_entry.pack()

generate_button = tk.Button(root, text= "Generate Password", command=generate_pass)
generate_button.pack(pady=10)

result_entry = tk.Entry(root, width=40, justify='center')
result_entry.pack(pady=5)

root.mainloop()
