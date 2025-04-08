import pandas as pd
import tkinter as tk
from tkinter import filedialog, ttk, messagebox, scrolledtext
import os


class EldenRingCSVManipulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Elden Ring CSV Manipulator")
        self.root.geometry("800x600")
        self.df = None
        self.file_path = None
        self.row_name_col = None
        self.effect_id_col = None
        self.effect_id1_col = None

        # Hauptframe
        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Button-Leiste am oberen Rand
        button_bar = ttk.Frame(main_frame)
        button_bar.pack(fill=tk.X, pady=(0, 10))

        # Buttons in der oberen Leiste
        load_button = ttk.Button(button_bar, text="Laden", command=self.load_csv, width=15)
        load_button.pack(side=tk.LEFT, padx=5)

        self.save_button = ttk.Button(button_bar, text="Speichern", command=self.save_csv, width=15, state=tk.DISABLED)
        self.save_button.pack(side=tk.LEFT, padx=5)

        search_replace_button = ttk.Button(button_bar, text="Suchen und Ersetzen",
                                           command=self.show_search_replace_dialog, width=20)
        search_replace_button.pack(side=tk.LEFT, padx=5)

        exit_button = ttk.Button(button_bar, text="Beenden", command=self.exit_application, width=15)
        exit_button.pack(side=tk.LEFT, padx=5)

        # Dateiauswahl-Bereich
        file_frame = ttk.LabelFrame(main_frame, text="Dateiauswahl", padding="10")
        file_frame.pack(fill=tk.X, pady=5)

        self.file_label = ttk.Label(file_frame, text="Keine Datei ausgewählt")
        self.file_label.pack(fill=tk.X, padx=5)

        # Suchbereich
        search_frame = ttk.LabelFrame(main_frame, text="Suche und Manipulation", padding="10")
        search_frame.pack(fill=tk.X, pady=5)

        ttk.Label(search_frame, text="Suche in 'Row Name':").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.search_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.search_var, width=40).grid(row=0, column=1, sticky=tk.W, padx=5,
                                                                             pady=5)

        ttk.Label(search_frame, text="Neuer Wert für residentSpEffectId:").grid(row=1, column=0, sticky=tk.W, padx=5,
                                                                                pady=5)
        self.effect_id_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.effect_id_var, width=40).grid(row=1, column=1, sticky=tk.W, padx=5,
                                                                                pady=5)

        ttk.Label(search_frame, text="Neuer Wert für residentSpEffectId1:").grid(row=2, column=0, sticky=tk.W, padx=5,
                                                                                 pady=5)
        self.effect_id1_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.effect_id1_var, width=40).grid(row=2, column=1, sticky=tk.W, pady=5)

        button_frame = ttk.Frame(search_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.apply_button = ttk.Button(button_frame, text="Änderungen anwenden", command=self.apply_changes,
                                       state=tk.DISABLED)
        self.apply_button.pack(side=tk.LEFT, padx=5)

        # Ergebnisbereich
        result_frame = ttk.LabelFrame(main_frame, text="Ergebnisse", padding="10")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        self.result_text = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, height=10)
        self.result_text.pack(fill=tk.BOTH, expand=True)

        # SpEffect IDs Bereich
        speffect_frame = ttk.LabelFrame(main_frame, text="ER SpEffect IDs", padding="10")
        speffect_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        speffect_text = scrolledtext.ScrolledText(speffect_frame, wrap=tk.WORD, height=10)
        speffect_text.pack(fill=tk.BOTH, expand=True)

        # SpEffect IDs einfügen
        speffect_ids = """Fire           -   R   3160
               L   3162
Flame Art      -   R   3260
               L   3262
Lightning      -   R   3165
               L   3167
Sacred         -   R   3185
               L   3187
Magic          -   R   3170
               L   3172
Cold           -   R   3140
               L   3144
Poison         -   R   3175
               L   3179
Blood          -   R   3190
               L   3194
Occult         -   R   3310
               L   3314

Spezielle Effekte:
Dragon         -   3260/3262
Rot            -   3310/3314
Soporific      -   3150/3154"""

        speffect_text.insert(tk.END, speffect_ids)
        speffect_text.config(state=tk.DISABLED)  # Schreibgeschützt machen

        # Statusleiste
        self.status_var = tk.StringVar()
        self.status_var.set("Bereit")
        status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Event-Handler für das Schließen des Fensters
        self.root.protocol("WM_DELETE_WINDOW", self.exit_application)

    def find_column_names(self):
        """Findet die korrekten Spaltennamen in der CSV-Datei"""
        if self.df is None:
            return False

        print("\nVerfügbare Spalten:", self.df.columns.tolist())
        print("\nErste 5 Zeilen der Datei:")
        print(self.df.head())

        # Suche nach Row Name Spalte mit verschiedenen Varianten
        row_name_candidates = [
            'Row Name', 'RowName', 'Name', 'Row', 'ID',
            'Weapon', 'Item', 'Equipment', 'Equip',
            'row name', 'rowname', 'name', 'row', 'id'
        ]

        self.row_name_col = None

        # Erste Suche: Exakte Übereinstimmung (case-insensitive)
        for col in self.df.columns:
            if col.lower() in [c.lower() for c in row_name_candidates]:
                self.row_name_col = col
                print(f"\nRow Name Spalte gefunden (exakt): '{col}'")
                print("Beispielwerte:")
                print(self.df[col].head())
                break

        # Zweite Suche: Teilstring-Übereinstimmung
        if not self.row_name_col:
            for col in self.df.columns:
                if any(candidate.lower() in col.lower() for candidate in row_name_candidates):
                    self.row_name_col = col
                    print(f"\nRow Name Spalte gefunden (teilweise): '{col}'")
                    print("Beispielwerte:")
                    print(self.df[col].head())
                    break

        # Letzte Option: Erste Spalte
        if not self.row_name_col and len(self.df.columns) > 0:
            self.row_name_col = self.df.columns[0]
            print(f"\nVerwende erste Spalte als Row Name: '{self.row_name_col}'")
            print("Beispielwerte:")
            print(self.df[self.row_name_col].head())

        # Suche nach Effect ID Spalten
        effect_id_candidates = [
            'residentSpEffectId',
            'SpEffectId',
            'EffectId',
            'SpEffect',
            'Effect',
            'resident',
            'residentspeffectid',
            'speffectid',
            'effectid'
        ]

        self.effect_id_col = None
        self.effect_id1_col = None

        # Erste Suche: Exakte Namen (case-insensitive)
        for col in self.df.columns:
            col_lower = col.lower()
            if col_lower in [c.lower() for c in effect_id_candidates]:
                if '1' in col or 'one' in col_lower:
                    self.effect_id1_col = col
                    print(f"\nEffect ID1 Spalte gefunden (exakt): '{col}'")
                else:
                    self.effect_id_col = col
                    print(f"\nEffect ID Spalte gefunden (exakt): '{col}'")

        # Zweite Suche: Teilstring-Übereinstimmung
        if not self.effect_id_col or not self.effect_id1_col:
            effect_cols = []
            for col in self.df.columns:
                col_lower = col.lower()
                if any(candidate.lower() in col_lower for candidate in effect_id_candidates):
                    effect_cols.append(col)

            # Sortiere die gefundenen Spalten
            effect_cols.sort(key=lambda x: ('1' in x, len(x)))

            if effect_cols:
                if not self.effect_id_col and len(effect_cols) > 0:
                    self.effect_id_col = effect_cols[0]
                    print(f"\nEffect ID Spalte gefunden (teilweise): '{self.effect_id_col}'")

                if not self.effect_id1_col and len(effect_cols) > 1:
                    self.effect_id1_col = effect_cols[1]
                    print(f"\nEffect ID1 Spalte gefunden (teilweise): '{self.effect_id1_col}'")

        # Wenn immer noch keine Spalten gefunden wurden, erstelle neue
        if not self.effect_id_col or not self.effect_id1_col:
            print("\nErstelle neue Effect ID Spalten...")

            if not self.effect_id_col:
                self.effect_id_col = 'residentSpEffectId'
                self.df[self.effect_id_col] = 0
                print(f"Neue Spalte erstellt: '{self.effect_id_col}'")

            if not self.effect_id1_col:
                self.effect_id1_col = 'residentSpEffectId1'
                self.df[self.effect_id1_col] = 0
                print(f"Neue Spalte erstellt: '{self.effect_id1_col}'")

        # Überprüfe, ob alle benötigten Spalten gefunden wurden
        success = (self.row_name_col is not None and
                   self.effect_id_col is not None and
                   self.effect_id1_col is not None)

        print("\nGefundene Spalten:")
        print(f"Row Name: '{self.row_name_col}'")
        print(f"Effect ID: '{self.effect_id_col}'")
        print(f"Effect ID1: '{self.effect_id1_col}'")
        print(f"Erfolg: {success}")

        if success:
            print("\nBeispielwerte für gefundene Spalten:")
            print("\nRow Name Spalte:")
            print(self.df[self.row_name_col].head())
            print("\nEffect ID Spalte:")
            print(self.df[self.effect_id_col].head())
            print("\nEffect ID1 Spalte:")
            print(self.df[self.effect_id1_col].head())

        return success

    def load_csv(self):
        """CSV-Datei laden"""
        file_path = filedialog.askopenfilename(
            title="CSV-Datei auswählen",
            filetypes=[("CSV Dateien", "*.csv"), ("Alle Dateien", "*.*")]
        )

        if not file_path:
            return

        try:
            self.status_var.set(f"Lade Datei...")
            self.root.update()

            # Versuche verschiedene Trennzeichen
            for sep in [',', ';', '\t', '|']:
                try:
                    # Versuche mit diesem Trennzeichen zu lesen
                    self.df = pd.read_csv(file_path, sep=sep)
                    if len(self.df.columns) > 1:  # Mehr als eine Spalte gefunden
                        print(f"Trennzeichen '{sep}' funktioniert!")
                        break
                except Exception as e:
                    print(f"Fehler mit Trennzeichen '{sep}': {str(e)}")
                    continue
            else:
                # Wenn keine Trennzeichen funktionieren, versuche es mit dem Standard
                self.df = pd.read_csv(file_path)

            self.file_path = file_path

            # Finde die korrekten Spaltennamen
            if not self.find_column_names():
                messagebox.showwarning("Warnung",
                                       "Konnte nicht alle benötigten Spalten finden. Die Anwendung wird versuchen, "
                                       "mit den verfügbaren Spalten zu arbeiten oder neue zu erstellen.")

            self.file_label.config(text=os.path.basename(file_path))
            self.apply_button.config(state=tk.NORMAL)
            self.save_button.config(state=tk.NORMAL)

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Datei erfolgreich geladen: {len(self.df)} Zeilen\n")

            if self.row_name_col:
                self.result_text.insert(tk.END, f"\nGefundene Spalten:\n")
                self.result_text.insert(tk.END, f"Row Name: '{self.row_name_col}'\n")
                self.result_text.insert(tk.END, f"Effect ID: '{self.effect_id_col}'\n")
                self.result_text.insert(tk.END, f"Effect ID1: '{self.effect_id1_col}'\n")

            self.status_var.set(f"Datei geladen: {os.path.basename(file_path)}")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Laden der Datei: {str(e)}")
            self.status_var.set("Fehler beim Laden der Datei")
            print(f"Fehler beim Laden: {str(e)}")
            import traceback
            traceback.print_exc()

    def save_csv(self):
        """Speichern der modifizierten CSV-Datei"""
        if self.df is None:
            messagebox.showwarning("Warnung", "Keine Daten zum Speichern vorhanden.")
            return

        file_path = filedialog.asksaveasfilename(
            title="CSV-Datei speichern",
            defaultextension=".csv",
            filetypes=[("CSV Dateien", "*.csv"), ("Alle Dateien", "*.*")]
        )

        if not file_path:
            return

        try:
            self.status_var.set(f"Speichere Datei...")
            self.root.update()

            # Einfaches Speichern der CSV-Datei
            self.df.to_csv(file_path, index=False)

            self.result_text.insert(tk.END, f"\n\nDatei erfolgreich gespeichert: {file_path}")
            self.status_var.set(f"Datei gespeichert: {os.path.basename(file_path)}")

            messagebox.showinfo("Erfolg", f"Datei erfolgreich gespeichert: {file_path}")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Speichern der Datei: {str(e)}")
            self.status_var.set("Fehler beim Speichern der Datei")
            print(f"Fehler beim Speichern: {str(e)}")
            import traceback
            traceback.print_exc()

    def show_search_replace_dialog(self):
        """Öffnet den Suchen und Ersetzen Dialog"""
        if self.df is None:
            messagebox.showwarning("Warnung", "Bitte zuerst eine Datei laden.")
            return

        dialog = tk.Toplevel(self.root)
        dialog.title("Suchen und Ersetzen")
        dialog.geometry("400x300")
        dialog.transient(self.root)  # Dialog ist abhängig vom Hauptfenster

        # Suchbereich
        search_frame = ttk.LabelFrame(dialog, text="Suchen und Ersetzen", padding="10")
        search_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Suchfeld
        ttk.Label(search_frame, text="Suchen nach:").grid(row=0, column=0, sticky=tk.W, pady=5)
        search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=search_var, width=30)
        search_entry.grid(row=0, column=1, sticky=tk.W, pady=5)

        # Ersetzen-Felder
        ttk.Label(search_frame, text=f"Neuer Wert für {self.effect_id_col}:").grid(row=1, column=0, sticky=tk.W, pady=5)
        effect_id_var = tk.StringVar()
        effect_id_entry = ttk.Entry(search_frame, textvariable=effect_id_var, width=30)
        effect_id_entry.grid(row=1, column=1, sticky=tk.W, pady=5)

        ttk.Label(search_frame, text=f"Neuer Wert für {self.effect_id1_col}:").grid(row=2, column=0, sticky=tk.W,
                                                                                    pady=5)
        effect_id1_var = tk.StringVar()
        effect_id1_entry = ttk.Entry(search_frame, textvariable=effect_id1_var, width=30)
        effect_id1_entry.grid(row=2, column=1, sticky=tk.W, pady=5)

        # Buttons
        button_frame = ttk.Frame(search_frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)

        def apply_search_replace():
            """Führt die Suchen und Ersetzen Operation aus"""
            search_term = search_var.get()
            effect_id = effect_id_var.get()
            effect_id1 = effect_id1_var.get()

            if not search_term or not effect_id or not effect_id1:
                messagebox.showwarning("Warnung", "Bitte alle Felder ausfüllen.", parent=dialog)
                return

            # Führe die Änderungen durch
            self.search_var.set(search_term)
            self.effect_id_var.set(effect_id)
            self.effect_id1_var.set(effect_id1)
            self.apply_changes()

            # Schließe den Dialog
            dialog.destroy()

        ttk.Button(button_frame, text="Anwenden", command=apply_search_replace).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Abbrechen", command=dialog.destroy).pack(side=tk.LEFT, padx=5)

        # Zentriere den Dialog auf dem Hauptfenster
        dialog.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - dialog.winfo_width()) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - dialog.winfo_height()) // 2
        dialog.geometry(f"+{x}+{y}")

        # Mache den Dialog modal
        dialog.grab_set()
        dialog.focus_set()
        search_entry.focus()

    def apply_changes(self):
        """Änderungen auf die CSV-Datei anwenden"""
        if self.df is None:
            messagebox.showwarning("Warnung", "Bitte zuerst eine Datei laden.")
            return

        search_term = self.search_var.get()
        effect_id = self.effect_id_var.get()
        effect_id1 = self.effect_id1_var.get()

        if not search_term:
            messagebox.showwarning("Warnung", "Bitte geben Sie einen Suchbegriff ein.")
            return

        if not effect_id or not effect_id1:
            messagebox.showwarning("Warnung", "Bitte geben Sie Werte für beide Effect IDs ein.")
            return

        try:
            self.status_var.set("Wende Änderungen an...")
            self.root.update()

            # Debug-Ausgabe
            print(f"\nSuche nach: '{search_term}' in Spalte '{self.row_name_col}'")
            print("Erste 10 Werte in der Spalte:")
            print(self.df[self.row_name_col].head(10).tolist())

            # Verbesserte Suche mit mehreren Methoden
            matching_rows = None

            # Methode 1: Exakte Übereinstimmung (case-insensitive)
            try:
                mask = self.df[self.row_name_col].astype(str).str.lower() == search_term.lower()
                if mask.sum() > 0:
                    matching_rows = self.df[mask]
                    print(f"\nExakte Übereinstimmung (case-insensitive): {mask.sum()} Zeilen gefunden")
            except Exception as e:
                print(f"Fehler bei exakter Suche: {str(e)}")

            # Methode 2: Teilstring-Suche (case-insensitive)
            if matching_rows is None or len(matching_rows) == 0:
                try:
                    mask = self.df[self.row_name_col].astype(str).str.lower().str.contains(
                        search_term.lower(),
                        na=False,
                        regex=False
                    )
                    if mask.sum() > 0:
                        matching_rows = self.df[mask]
                        print(f"\nTeilstring-Suche: {mask.sum()} Zeilen gefunden")
                        print("Gefundene Werte:")
                        print(matching_rows[self.row_name_col].tolist())
                except Exception as e:
                    print(f"Fehler bei Teilstring-Suche: {str(e)}")

            # Methode 3: Fuzzy Matching als letzter Ausweg
            if matching_rows is None or len(matching_rows) == 0:
                try:
                    matching_indices = []
                    search_lower = search_term.lower()
                    for idx, value in enumerate(self.df[self.row_name_col]):
                        try:
                            value_str = str(value).lower()
                            # Prüfe auf teilweise Übereinstimmung und Ähnlichkeit
                            if (search_lower in value_str or
                                    value_str in search_lower or
                                    any(term in value_str for term in search_lower.split())):
                                matching_indices.append(idx)
                        except:
                            continue

                    if matching_indices:
                        matching_rows = self.df.iloc[matching_indices]
                        print(f"\nFuzzy Matching: {len(matching_indices)} Zeilen gefunden")
                        print("Gefundene Werte:")
                        print(matching_rows[self.row_name_col].tolist())
                except Exception as e:
                    print(f"Fehler bei Fuzzy Matching: {str(e)}")

            # Überprüfe, ob Zeilen gefunden wurden
            if matching_rows is None or len(matching_rows) == 0:
                messagebox.showinfo("Information",
                                    f"Keine Einträge mit '{search_term}' in '{self.row_name_col}' gefunden.\n\n"
                                    f"Tipp: Überprüfen Sie die Schreibweise und versuchen Sie einen kürzeren Suchbegriff.\n\n"
                                    f"Beispielwerte aus der Spalte:\n" +
                                    "\n".join(str(x) for x in self.df[self.row_name_col].head().tolist()))
                self.status_var.set("Keine Übereinstimmungen gefunden")
                return

            # Ändere die Werte in den entsprechenden Spalten
            try:
                # Sicherere Methode zum Aktualisieren der Werte
                for idx in matching_rows.index:
                    self.df.at[idx, self.effect_id_col] = effect_id
                    self.df.at[idx, self.effect_id1_col] = effect_id1

                print(f"\nWerte aktualisiert für {len(matching_rows)} Zeilen")
            except Exception as e:
                print(f"Fehler beim Aktualisieren der Werte: {str(e)}")
                raise ValueError(f"Fehler beim Aktualisieren der Werte: {str(e)}")

            # Aktualisiere die Benutzeroberfläche
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"{len(matching_rows)} Einträge aktualisiert:\n\n")

            # Zeige die aktualisierten Zeilen an
            try:
                result_df = matching_rows[[self.row_name_col, self.effect_id_col, self.effect_id1_col]]
                self.result_text.insert(tk.END, result_df.to_string())
            except Exception as e:
                print(f"Fehler beim Anzeigen der Ergebnisse: {str(e)}")
                self.result_text.insert(tk.END,
                                        f"Konnte die Ergebnisse nicht anzeigen, aber {len(matching_rows)} "
                                        f"Einträge wurden aktualisiert.")

            self.save_button.config(state=tk.NORMAL)
            self.status_var.set(f"{len(matching_rows)} Einträge aktualisiert")

        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler bei der Anwendung der Änderungen: {str(e)}")
            self.status_var.set("Fehler bei der Anwendung der Änderungen")
            print(f"\nFehler bei apply_changes: {str(e)}")
            import traceback
            traceback.print_exc()

    def exit_application(self):
        """Beendet die Anwendung"""
        if messagebox.askokcancel("Beenden", "Möchten Sie die Anwendung wirklich beenden?"):
            self.root.destroy()


# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    app = EldenRingCSVManipulator(root)
    root.mainloop()