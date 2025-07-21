import fitz  # PyMuPDF
import json
import os

def extract_pdf_content(pdf_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    doc = fitz.open(pdf_path)
    data = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text()
        images = []
        for img_index, img in enumerate(page.get_images(full=True), start=1):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            img_filename = f"page{page_num}_image{img_index}.png"
            img_path = os.path.join(output_folder, img_filename)
            if pix.n < 5:  # this is GRAY or RGB
                pix.save(img_path)
            else:  # CMYK
                pix = fitz.Pixmap(fitz.csRGB, pix)
                pix.save(img_path)
            pix = None
            images.append(img_path)
        data.append({
            "page": page_num,
            "text": text,
            "images": images
        })
    with open("sample_output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    # Example usage
    extract_pdf_content("sample.pdf", "extracted_images")
