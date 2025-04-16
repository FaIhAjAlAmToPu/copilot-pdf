import os
from converters.image_to_pdf import convert_image_to_pdf
from converters.doc_to_pdf import convert_doc_to_pdf
from converters.other_to_pdf import convert_other_to_pdf
from utils.file_handler import get_file_type

def main():
    file_paths = input("Enter the file paths separated by commas: ").split(',')
    output_directory = input("Enter the output directory for the PDF files: ")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for file_path in file_paths:
        file_path = file_path.strip()
        file_type = get_file_type(file_path)

        if file_type == 'image':
            output_path = os.path.join(output_directory, os.path.basename(file_path).replace(os.path.splitext(file_path)[1], '.pdf'))
            convert_image_to_pdf(file_path, output_path)
        elif file_type == 'document':
            output_path = os.path.join(output_directory, os.path.basename(file_path).replace(os.path.splitext(file_path)[1], '.pdf'))
            convert_doc_to_pdf(file_path, output_path)
        else:
            output_path = os.path.join(output_directory, os.path.basename(file_path).replace(os.path.splitext(file_path)[1], '.pdf'))
            convert_other_to_pdf(file_path, output_path)

    print("Conversion completed!")

if __name__ == "__main__":
    main()