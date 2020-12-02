import tkinter as tk

root = tk.Tk()

schaltf1 = tk.Button(root, text="Umrechnen", command=tk.destroy, cursor='hand2')
schaltf1.pack(anchor='se')

root.mainloop()