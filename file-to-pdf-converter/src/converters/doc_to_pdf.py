from docx import Document
from fpdf import FPDF

def convert_doc_to_pdf(doc_path, output_path):
    # Create a PDF object
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Load the DOCX file
    doc = Document(doc_path)
    
    # Add each paragraph to the PDF
    for para in doc.paragraphs:
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, para.text)
    
    # Save the PDF to the specified output path
    pdf.output(output_path)