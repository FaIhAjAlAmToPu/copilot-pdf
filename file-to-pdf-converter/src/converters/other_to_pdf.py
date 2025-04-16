from pathlib import Path
import os
from utils.file_handler import get_file_type, save_pdf
from converters.image_to_pdf import convert_image_to_pdf
from converters.doc_to_pdf import convert_doc_to_pdf

def convert_other_to_pdf(file_path, output_path):
    file_type = get_file_type(file_path)

    if file_type in ['image/jpeg', 'image/png', 'image/gif']:
        convert_image_to_pdf(file_path, output_path)
    elif file_type in ['application/vnd.openxmlformats-officedocument.wordprocessingml.document']:
        convert_doc_to_pdf(file_path, output_path)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    save_pdf(output_path)