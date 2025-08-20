import tkinter as tk 
from tkinter import messagebox 
import main
root=tk.Tk() 
root.title("Your Assistant") 


def generate_code_improvement():
    original_code=original_code_text.get("1.0",tk.END)
    user_request=user_request_entry.get() 
    improved_code, explanation, suggestions = main.generate_improved_code(original_code, user_request)
    improved_code_text.delete("1.0",tk.END)
    improved_code_text.insert(tk.END,improved_code) 

    explanation_text.delete("1.0",tk.END)
    explanation_text.insert(tk.END,explanation) 

    suggestions_text.delete("1.0",tk.END) 
    suggestions_text.insert(tk.END,suggestions) 

tk.Label(root,text="original Code").pack() 
original_code_text=tk.Text(root,height=10,width=50) 
original_code_text.pack() 

tk.Label(root,text="User Request:").pack() 
user_request_entry=tk.Entry(root,width=50)
user_request_entry.pack() 

generate_button=tk.Button(root,text="Generate Improved Code",command=generate_code_improvement) 
generate_button.pack()  

tk.Label(root,text="Improved Code").pack() 
improved_code_text=tk.Text(root,height=10,width=50) 
improved_code_text.pack() 

tk.Label(root,text="Explanation:").pack() 
explanation_text=tk.Text(root,height=5,widh=50) 
explanation_text.pack()
tk.Label(root, text="Suggestions:").pack()
suggestions_text = tk.Text(root, height=5, width=50)
suggestions_text.pack()

# Run the Tkinter event loop
root.mainloop()
