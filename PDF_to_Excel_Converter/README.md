# 🧾 PDF to Excel/CSV Converter (Text + Scanned PDFs)

This Python project converts tabular data from both **text-based PDFs** and **scanned PDFs (images)** into clean **Excel (.xlsx)** and **CSV (.csv)** files.

## ✅ Features

- 📄 Detects if the PDF is text-based or scanned
- 🧠 Uses **OCR (Tesseract)** to extract data from scanned PDFs
- 🔍 Uses **pdfplumber** for accurate table extraction from text PDFs
- 📊 Outputs both `.xlsx` and `.csv` formats
- 🚀 Easy to use: just run the script and enter your PDF filename

---

## 🛠️ Requirements

Install all required Python packages:

```bash
pip install pdfplumber pytesseract pdf2image pandas
```
