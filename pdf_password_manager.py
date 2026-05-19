"""
PDF Password Manager
Joshua-1100 2026-05-19
--------------------
A simple GUI tool to add or remove passwords from PDF files.
Requires: pypdf, tkinter (built into Python)

Install dependency: pip install pypdf
"""

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pypdf import PdfReader, PdfWriter


# ── Core PDF logic ──────────────────────────────────────────────────────────

def protect_pdf(file_path: str, password: str) -> str:
    """Encrypt a PDF and save it as <original_name>_protected.pdf."""
    reader = PdfReader(file_path)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.encrypt(password)

    base, ext = os.path.splitext(file_path)
    out_path = f"{base}_protected{ext}"
    with open(out_path, "wb") as f:
        writer.write(f)
    return out_path


def unprotect_pdf(file_path: str, password: str) -> str:
    """Decrypt a PDF and save it as <original_name>_unlocked.pdf."""
    reader = PdfReader(file_path)
    if not reader.is_encrypted:
        raise ValueError("File is not password-protected.")
    result = reader.decrypt(password)
    if result.name == "NOT_DECRYPTED":
        raise ValueError("Incorrect password.")

    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    base, ext = os.path.splitext(file_path)
    out_path = f"{base}_unlocked{ext}"
    with open(out_path, "wb") as f:
        writer.write(f)
    return out_path


# ── GUI ──────────────────────────────────────────────────────────────────────

class PDFPasswordManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Password Manager")
        self.resizable(False, False)
        self.configure(padx=20, pady=20)

        self.selected_files: list[str] = []
        self.mode = tk.StringVar(value="protect")

        self._build_ui()

    def _build_ui(self):
        # ── Mode selection ──
        mode_frame = ttk.LabelFrame(self, text="Action", padding=10)
        mode_frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        ttk.Radiobutton(
            mode_frame, text="🔒  Add password (protect)",
            variable=self.mode, value="protect"
        ).pack(anchor="w")
        ttk.Radiobutton(
            mode_frame, text="🔓  Remove password (unlock)",
            variable=self.mode, value="unprotect"
        ).pack(anchor="w")

        # ── File selection ──
        file_frame = ttk.LabelFrame(self, text="Selected Files", padding=10)
        file_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        self.file_listbox = tk.Listbox(
            file_frame, width=60, height=6,
            selectmode=tk.EXTENDED, activestyle="none"
        )
        self.file_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(file_frame, orient="vertical",
                                  command=self.file_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.file_listbox.configure(yscrollcommand=scrollbar.set)

        btn_frame = ttk.Frame(self)
        btn_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        ttk.Button(btn_frame, text="Browse…", command=self._browse_files).pack(side="left", padx=(0, 5))
        ttk.Button(btn_frame, text="Remove Selected", command=self._remove_selected).pack(side="left", padx=(0, 5))
        ttk.Button(btn_frame, text="Clear All", command=self._clear_files).pack(side="left")

        # ── Password entry ──
        pw_frame = ttk.LabelFrame(self, text="Password", padding=10)
        pw_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        ttk.Label(pw_frame, text="Password:").grid(row=0, column=0, sticky="w", padx=(0, 8))
        self.pw_var = tk.StringVar()
        self.pw_entry = ttk.Entry(pw_frame, textvariable=self.pw_var, show="•", width=30)
        self.pw_entry.grid(row=0, column=1, sticky="w")

        self.show_pw = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            pw_frame, text="Show password",
            variable=self.show_pw, command=self._toggle_pw_visibility
        ).grid(row=0, column=2, padx=(10, 0))

        # ── Status log ──
        log_frame = ttk.LabelFrame(self, text="Results", padding=10)
        log_frame.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        self.log = tk.Text(log_frame, width=60, height=6, state="disabled",
                           wrap="word", relief="flat")
        self.log.pack(fill="both", expand=True)

        self.log.tag_configure("success", foreground="#2e7d32")
        self.log.tag_configure("error",   foreground="#c62828")
        self.log.tag_configure("info",    foreground="#1565c0")

        # ── Run button ──
        ttk.Button(
            self, text="Run", command=self._run,
            style="Accent.TButton"
        ).grid(row=5, column=0, columnspan=2, pady=(0, 5))

    # ── Helpers ──────────────────────────────────────────────────────────────

    def _browse_files(self):
        paths = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        for p in paths:
            if p not in self.selected_files:
                self.selected_files.append(p)
                self.file_listbox.insert(tk.END, os.path.basename(p))

    def _remove_selected(self):
        selected_indices = list(self.file_listbox.curselection())
        for i in reversed(selected_indices):
            self.file_listbox.delete(i)
            self.selected_files.pop(i)

    def _clear_files(self):
        self.file_listbox.delete(0, tk.END)
        self.selected_files.clear()

    def _toggle_pw_visibility(self):
        self.pw_entry.config(show="" if self.show_pw.get() else "•")

    def _log(self, message: str, tag: str = "info"):
        self.log.config(state="normal")
        self.log.insert(tk.END, message + "\n", tag)
        self.log.see(tk.END)
        self.log.config(state="disabled")

    def _clear_log(self):
        self.log.config(state="normal")
        self.log.delete("1.0", tk.END)
        self.log.config(state="disabled")

    def _run(self):
        if not self.selected_files:
            messagebox.showwarning("No Files", "Please select at least one PDF file.")
            return

        password = self.pw_var.get()
        if not password:
            messagebox.showwarning("No Password", "Please enter a password.")
            return

        action = self.mode.get()
        self._clear_log()
        self._log(f"{'Protecting' if action == 'protect' else 'Unlocking'} {len(self.selected_files)} file(s)…\n", "info")

        success_count = 0
        error_count = 0

        for file_path in self.selected_files:
            name = os.path.basename(file_path)
            try:
                if action == "protect":
                    out = protect_pdf(file_path, password)
                else:
                    out = unprotect_pdf(file_path, password)
                self._log(f"✓  {name}  →  {os.path.basename(out)}", "success")
                success_count += 1
            except ValueError as e:
                self._log(f"✗  {name}:  {e}", "error")
                error_count += 1
            except Exception as e:
                self._log(f"✗  {name}:  Unexpected error — {e}", "error")
                error_count += 1

        self._log(
            f"\nDone: {success_count} succeeded, {error_count} failed.\n"
            f"Output files saved alongside originals.",
            "info"
        )


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = PDFPasswordManager()
    app.mainloop()
