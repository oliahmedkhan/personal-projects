import os
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
import pandas as pd
def is_scanned(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        first_page = pdf.pages[0]
        text = first_page.extract_text()
        return not bool(text)

def extract_from_text_pdf(pdf_file):
    all_data = []
    with pdfplumber.open(pdf_file) as pdf:
        for i, page in enumerate(pdf.pages):
            table = page.extract_table()
            if table:
                df = pd.DataFrame(table[1:], columns=table[0])
                df.dropna(how='all', inplace=True)
                df = df.fillna("")
                df['Page'] = i + 1
                all_data.append(df)

    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        return final_df
    else:
        return None

def extract_from_scanned_pdf(pdf_file):
    images = convert_from_path(pdf_file)
    ocr_text = []
    for image in images:
        text = pytesseract.image_to_string(image)
        ocr_text.extend([line.strip() for line in text.splitlines() if line.strip()])
    structured_rows = []
    for line in ocr_text:
        row = line.split()
        if len(row) >= 3:
            marks = row[-1]
            subject = row[-2]
            name = " ".join(row[:-2])
            structured_rows.append([name, subject, marks])

    if structured_rows:
        df = pd.DataFrame(structured_rows, columns=["Name", "Subject", "Marks"])
        return df
    else:
        return None

def main():
    pdf_file = input("Enter PDF filename (e.g. marksheet.pdf): ").strip()

    if not os.path.exists(pdf_file):
        print("❌ File not found.")
        return

    print(" Checking if PDF is scanned or text...")
    if is_scanned(pdf_file):
        print("Scanned PDF detected. Using OCR...")
        df = extract_from_scanned_pdf(pdf_file)
    else:
        print("Text-based PDF detected. Extracting directly...")
        df = extract_from_text_pdf(pdf_file)

    if df is not None:
        base_name = os.path.splitext(pdf_file)[0]
        excel_file = base_name + "_converted.xlsx"
        csv_file = base_name + "_converted.csv"
        df.to_excel(excel_file, index=False)
        df.to_csv(csv_file, index=False)
        print(f" Done! Saved as:\n→ {excel_file}\n→ {csv_file}")
    else:
        print("No data found or failed to extract.")

if __name__ == "__main__":
    main()
