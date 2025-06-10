import fitz  # PyMuPDF
import os

def extract_images(pdf_path, output_folder='extracted_images'):
    os.makedirs(output_folder, exist_ok=True)
    doc = fitz.open(pdf_path)
    image_paths = []
    for page_number in range(len(doc)):
        for img_index, img in enumerate(doc.get_page_images(page_number)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image['image']
            image_ext = base_image['ext']
            image_path = os.path.join(output_folder, f"page{page_number+1}_img{img_index+1}.{image_ext}")
            with open(image_path, 'wb') as img_file:
                img_file.write(image_bytes)
            image_paths.append(image_path)
    return image_paths 