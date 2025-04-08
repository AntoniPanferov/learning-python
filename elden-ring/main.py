import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import pandas as pd

def load_file():
    global df, file_path
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not file_path:
        return
    try:
        df = pd.read_csv(file_path)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, df.to_string())
        messages.config(text=f"Loaded file: {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error loading file: {e}")

def save_file():
    global df
    if df is None:
        messagebox.showerror("Error", "No file loaded")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if not save_path:
        return
    try:
        df.to_csv(save_path, index=False)
        messages.config(text=f"File saved as: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving file: {e}")

def search_and_replace():
    global df
    if df is None:
        messagebox.showerror("Error", "No file loaded")
        return
    search_value = entry_search.get().strip()
    replace_value1 = entry_replace1.get().strip()
    replace_value2 = entry_replace2.get().strip()
    if not search_value or not replace_value1 or not replace_value2:
        messagebox.showerror("Error", "Please fill in all fields")
        return
    if "Row Name" not in df.columns or "residentSpEffectId" not in df.columns or "residentSpEffectId1" not in df.columns:
        messagebox.showerror("Error", "Required columns are missing in the file")
        return
    df.loc[df["Row Name"].astype(str) == search_value, ["residentSpEffectId", "residentSpEffectId1"]] = [replace_value1, replace_value2]

    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, df.to_string())
    messages.config(text="Replacement completed")

def build_gui():
    global root, text_area, entry_search, entry_replace1, entry_replace2, messages, df
    root = tk.Tk()
    root.title("Tarnished Editor")
    root.state("zoomed")

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)
    main_frame.columnconfigure(0, weight=3)
    main_frame.columnconfigure(1, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=0)

    frame_text = tk.Frame(main_frame)
    frame_text.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    lbl_content = tk.Label(frame_text, text="Content")
    lbl_content.pack(anchor="w")

    text_area = scrolledtext.ScrolledText(frame_text)
    text_area.pack(fill=tk.BOTH, expand=True)

    frame_inputs = tk.Frame(main_frame)
    frame_inputs.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

    lbl_search = tk.Label(frame_inputs, text="Search Entry:")
    lbl_search.pack(anchor="w", pady=(0, 2))
    entry_search = tk.Entry(frame_inputs)
    entry_search.pack(fill=tk.X, pady=(0, 10))

    lbl_replace1 = tk.Label(frame_inputs, text="New Value for residentSpEffectId:")
    lbl_replace1.pack(anchor="w", pady=(0, 2))
    entry_replace1 = tk.Entry(frame_inputs)
    entry_replace1.pack(fill=tk.X, pady=(0, 10))

    lbl_replace2 = tk.Label(frame_inputs, text="New Value for residentSpEffectId1:")
    lbl_replace2.pack(anchor="w", pady=(0, 2))
    entry_replace2 = tk.Entry(frame_inputs)
    entry_replace2.pack(fill=tk.X, pady=(0, 10))

    lbl_messages = tk.Label(frame_inputs, text="Messages:")
    lbl_messages.pack(anchor="w", pady=(10, 2))
    messages = tk.Label(frame_inputs, text="", height=5, anchor="nw", justify="left", relief="sunken")
    messages.pack(fill=tk.BOTH, expand=True)

    frame_buttons = tk.Frame(main_frame)
    frame_buttons.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)
    frame_buttons.columnconfigure((0, 1, 2), weight=1)

    btn_load = tk.Button(frame_buttons, text="Load", command=load_file)
    btn_load.grid(row=0, column=0, sticky="ew", padx=5)

    btn_save = tk.Button(frame_buttons, text="Save as", command=save_file)
    btn_save.grid(row=0, column=1, sticky="ew", padx=5)

    btn_search_replace = tk.Button(frame_buttons, text="Search and Replace", command=search_and_replace)
    btn_search_replace.grid(row=0, column=2, sticky="ew", padx=5)

    df = None
    root.mainloop()

build_gui()
