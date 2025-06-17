# my_text_editor.py
#  testing before implementation
# 
import tkinter as tk
from tkinter import scrolledtext, Menu, filedialog, messagebox
#         defaultextension=".txt",
import os # For getting filename from path

class TextEditorApp: # Renamed for clarity when deploying
    def __init__(self, master):
        self.master = master
        master.title("Simple Text Editor")
        master.geometry("800x600")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, undo=True)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        self.menu_bar = Menu(master)
        master.config(menu=self.menu_bar)

        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open...", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_command(label="Save As...", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_editor)

        self.edit_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo, accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo, accelerator="Ctrl+Y")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=lambda: self.text_area.event_generate("<<Cut>>"), accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Copy", command=lambda: self.text_area.event_generate("<<Copy>>"), accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Paste", command=lambda: self.text_area.event_generate("<<Paste>>"), accelerator="Ctrl+V")
        self.edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")

        self.current_file_path = None
        self.update_title()

        # Bind keyboard shortcuts
        master.bind_all("<Control-n>", lambda event: self.new_file())
        master.bind_all("<Control-o>", lambda event: self.open_file())
        master.bind_all("<Control-s>", lambda event: self.save_file())
        master.bind_all("<Control-Shift-S>", lambda event: self.save_as_file()) # Note: Shift needs to be explicit
        master.bind_all("<Control-a>", lambda event: self.select_all())
        # Cut, Copy, Paste, Undo, Redo are often handled by the Text widget itself or OS,
        # but explicitly binding can be good.
        # For Ctrl+X, C, V, Z, Y, the Text widget often handles these well.
        # Make sure your focus is on the text_area for these to work by default.

    def update_title(self):
        if self.current_file_path:
            filename = os.path.basename(self.current_file_path)
            self.master.title(f"Simple Text Editor - {filename}")
        else:
            self.master.title("Simple Text Editor - New File")

    def new_file(self):
        if self.text_area.edit_modified(): # Check if text has changed
            if not messagebox.askyesno("Unsaved Changes", "You have unsaved changes. Do you want to discard them and create a new file?"):
                return
        self.text_area.delete(1.0, tk.END)
        self.current_file_path = None
        self.text_area.edit_modified(False) # Reset modified flag
        self.update_title()

    def open_file(self):
        if self.text_area.edit_modified():
            if not messagebox.askyesno("Unsaved Changes", "You have unsaved changes. Do you want to discard them and open a new file?"):
                return
        filepath = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        try:
            with open(filepath, "r", encoding='utf-8') as f: # Added encoding
                content = f.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.current_file_path = filepath
            self.text_area.edit_modified(False) # Reset modified flag
            self.update_title()
        except Exception as e:
            messagebox.showerror("Error Opening File", f"Could not open file: {e}")

    def save_file(self):
        if self.current_file_path:
            try:
                content = self.text_area.get(1.0, tk.END).rstrip('\n') # Remove trailing newline if any
                with open(self.current_file_path, "w", encoding='utf-8') as f: # Added encoding
                    f.write(content)
                self.text_area.edit_modified(False) # Reset modified flag
                self.update_title() # Update title, maybe remove '*' if you add it for unsaved
            except Exception as e:
                messagebox.showerror("Error Saving File", f"Could not save file: {e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            initialfile="Untitled.txt",
            filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        try:
            content = self.text_area.get(1.0, tk.END).rstrip('\n')
            with open(filepath, "w", encoding='utf-8') as f: # Added encoding
                f.write(content)
            self.current_file_path = filepath
            self.text_area.edit_modified(False) # Reset modified flag
            self.update_title()
        except Exception as e:
            messagebox.showerror("Error Saving File", f"Could not save file: {e}")

    def select_all(self):
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)
        self.text_area.mark_set(tk.INSERT, "1.0")
        self.text_area.see(tk.INSERT)
        return "break" # Prevents default behavior if any

    def exit_editor(self):
        if self.text_area.edit_modified():
            if messagebox.askyesno("Exit", "You have unsaved changes. Do you want to save before exiting?"):
                self.save_file()
                if not self.text_area.edit_modified(): # Check if save was successful or cancelled
                    self.master.quit()
            else:
                 self.master.quit() # Exit without saving
        else:
            self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.protocol("WM_DELETE_WINDOW", app.exit_editor) # Handle window close button
    root.mainloop()

    
   

# This code creates a simple text editor using Tkinter with basic file operations and editing features.
# It includes a menu bar for file and edit operations, supports keyboard shortcuts,
# and handles unsaved changes before exiting or opening new files.
# The text editor can open, save, and create new files, and it uses a scrolled text area for editing.
# The code is structured to be clear and maintainable, with error handling for file operations.
# Note: Ensure you have Tkinter installed and available in your Python environment to run this code.
# The code is designed to be run as a standalone script.
# It can be easily extended with more features like find/replace, font customization, etc.
