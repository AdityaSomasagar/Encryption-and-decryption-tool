# [file name]: gui_frontend.py
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
import CaesarCipher

class CaesarCipherApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Caesar Cipher GUI")
        self.geometry("800x600")
        self.create_widgets()
        self.file_path = None

    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self, padding=20)
        main_frame.pack(expand=True, fill='both')

        # Operation selection
        self.operation_var = tk.StringVar(value='encrypt')
        ttk.Label(main_frame, text="Select Operation:").pack(anchor='w')
        ttk.Radiobutton(main_frame, text="Encrypt", variable=self.operation_var, 
                       value='encrypt').pack(anchor='w')
        ttk.Radiobutton(main_frame, text="Decrypt", variable=self.operation_var,
                       value='decrypt').pack(anchor='w')

        # File Drag & Drop Area
        ttk.Label(main_frame, text="File Operations:").pack(anchor='w', pady=(10,0))
        self.file_frame = ttk.LabelFrame(main_frame, text="Drag & Drop File Here")
        self.file_frame.pack(fill='x', pady=5)
        self.file_label = ttk.Label(self.file_frame, text="No file selected")
        self.file_label.pack(pady=20)
        
        # Configure drag and drop
        self.file_frame.drop_target_register(DND_FILES)
        self.file_frame.dnd_bind('<<Drop>>', self.on_file_drop)
        
        # Browse File Button
        ttk.Button(main_frame, text="Browse File", command=self.browse_file).pack(pady=5)

        # Text input
        ttk.Label(main_frame, text="Text Operations:").pack(anchor='w', pady=(10,0))
        self.input_text = scrolledtext.ScrolledText(main_frame, height=8)
        self.input_text.pack(fill='x')

        # Shift key input
        ttk.Label(main_frame, text="Shift Key:").pack(anchor='w', pady=(10,0))
        self.key_input = ttk.Entry(main_frame, width=10)
        self.key_input.pack(anchor='w')

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Process", command=self.process).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_fields).pack(side='left', padx=5)

        # Result display
        ttk.Label(main_frame, text="Result:").pack(anchor='w', pady=(10,0))
        self.result_text = scrolledtext.ScrolledText(main_frame, height=8, state='disabled')
        self.result_text.pack(fill='x')

    def on_file_drop(self, event):
        self.file_path = event.data.strip('{}')
        self.file_label.config(text=f"Selected File: {self.file_path}")

    def browse_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.file_label.config(text=f"Selected File: {self.file_path}")

    def process(self):
        try:
            key = int(self.key_input.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid key. Please enter an integer.")
            return

        operation = self.operation_var.get()
        
        if self.file_path:
            self.process_file(key, operation)
        else:
            self.process_text(key, operation)

    def process_text(self, key, operation):
        text = self.input_text.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text or select a file!")
            return

        try:
            if operation == 'encrypt':
                result = CaesarCipher.CCEncrypt(text, key)
            else:
                result = CaesarCipher.CCDecrypt(text, key)
            
            self.show_result(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def process_file(self, key, operation):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if operation == 'encrypt':
                processed = CaesarCipher.CCEncrypt(content, key)
            else:
                processed = CaesarCipher.CCDecrypt(content, key)

            # Save processed file
            save_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
            )
            if save_path:
                with open(save_path, 'w', encoding='utf-8') as f:
                    f.write(processed)
                messagebox.showinfo("Success", f"File {operation}ed successfully!\nSaved to: {save_path}")
                
        except Exception as e:
            messagebox.showerror("Error", f"File processing failed: {str(e)}")

    def show_result(self, result):
        self.result_text.config(state='normal')
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)
        self.result_text.config(state='disabled')

    def clear_fields(self):
        self.input_text.delete("1.0", tk.END)
        self.key_input.delete(0, tk.END)
        self.result_text.config(state='normal')
        self.result_text.delete("1.0", tk.END)
        self.result_text.config(state='disabled')
        self.file_path = None
        self.file_label.config(text="No file selected")

if __name__ == "__main__":
    app = CaesarCipherApp()
    app.mainloop()