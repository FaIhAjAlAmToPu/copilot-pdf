# File-to-PDF Converter

This project is a Python application that converts various file types, including images and documents, into PDF format. It provides a simple interface for users to specify the locations of the files they wish to convert.

## Features

- Convert images (JPEG, PNG, etc.) to PDF
- Convert DOCX documents to PDF
- Support for other file types with appropriate conversion methods
- Easy-to-use command-line interface

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/file-to-pdf-converter.git
   cd file-to-pdf-converter
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command in your terminal:

```
python src/main.py
```

You will be prompted to enter the file paths of the files you want to convert. The application will automatically determine the file type and convert it to PDF.

## Supported File Types

- Images: JPEG, PNG, BMP, etc.
- Documents: DOCX
- Other file types can be added with appropriate converters.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.