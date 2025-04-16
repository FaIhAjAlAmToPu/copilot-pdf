def convert_image_to_pdf(image_path, output_path):
    from PIL import Image

    # Open the image file
    with Image.open(image_path) as img:
        # Convert the image to RGB if it's in a different mode
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        # Save the image as a PDF
        img.save(output_path, "PDF")