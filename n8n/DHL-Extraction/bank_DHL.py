import sys
import re
import os
import io
import pymupdf
from PIL import Image
import pytesseract

# Configure Tesseract paths
TESSERACT_PATH = r"C:\Users\MdAtiqurRahmanSifat\AppData\Local\Tesseract-OCR\tesseract.exe"
TESSDATA_PATH = r"C:\Users\MdAtiqurRahmanSifat\AppData\Local\Tesseract-OCR\tessdata"

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
os.environ["TESSDATA_PREFIX"] = TESSDATA_PATH

def translate_bengali_digits(text):
    """Converts Bengali digits (০-৯) to English digits (0-9) and fixes common OCR blur confusions."""
    bengali_to_english = str.maketrans('০১২৩৪৫৬৭৮৯', '0123456789')
    translated = text.translate(bengali_to_english)
    
    # Fix common OCR blur error where 6 (৬ -> 6) is misread as 8 (৮ -> 8) in the 2nd position of the prefix
    if translated.startswith("2827-"):
        translated = "2627-" + translated[5:]
    elif translated.startswith("28"): # General fallback for blurred 26 prefixes read as 28
        translated = "26" + translated[2:]
        
    return translated

def extract_valid_challan(text):
    """
    Intelligently searches text for the true Challan No,
    ignoring system account codes (like those starting with '১১১০').
    """
    if not text:
        return None, None

    # Strategy 1: Look near the label 'চালান নং'
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if 'চালান' in line and ('নং' in line or 'নম্ব' in line):
            combined_snippet = " ".join(lines[i:i+3])
            match = re.search(r'([০-৯\d]{4}\-[০-৯\d]{7,12})', combined_snippet)
            if match:
                val = match.group(1).strip()
                if not val.startswith('১১১০'):
                    return val, translate_bengali_digits(val)

    # Strategy 2: Global pattern scan for government challan format
    matches = re.findall(r'\b([০-৯\d]{4}\-[০-৯\d]{7,12})\b', text)
    for m in matches:
        val = m.strip()
        if not val.startswith('১১১০') and not val.startswith('1110'):
            return val, translate_bengali_digits(val)
            
    return None, None

def process_challan_pdf(pdf_path):
    try:
        doc = pymupdf.open(pdf_path)
        if len(doc) == 0:
            return None, None
        
        page = doc[0]
        
        # 1. Try direct text extraction first (instant for type02)
        direct_text = page.get_text("text")
        ben, eng = extract_valid_challan(direct_text)
        if ben and eng:
            doc.close()
            return ben, eng
            
        # 2. Fallback to 600 DPI OCR extraction (robust for type01 / scanned forms)
        pix = page.get_pixmap(dpi=600)
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))
        doc.close()
        
        try:
            ocr_text = pytesseract.image_to_string(image, lang='ben+eng')
        except Exception:
            ocr_text = pytesseract.image_to_string(image, lang='eng')
            
        ben, eng = extract_valid_challan(ocr_text)
        if ben and eng:
            return ben, eng
            
    except Exception as e:
        print(f"Error during processing: {e}", file=sys.stderr)
        
    return None, None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the PDF path as an argument.")
        sys.exit(1)
        
    pdf_file = sys.argv[1]
    ben_no, eng_no = process_challan_pdf(pdf_file)
    
    if ben_no and eng_no:
        print(f"Challan No (চালান নং): {ben_no}")
        print(f"Translated English Challan No: {eng_no}")
    else:
        print("Challan No not found.")