def get_file_type(file_path):
    import mimetypes
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type:
        return mime_type.split('/')[0]
    return None

def save_pdf(output_path, pdf_content):
    with open(output_path, 'wb') as pdf_file:
        pdf_file.write(pdf_content)