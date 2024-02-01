from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def create_pdf_from_jpg(input_image_path, output_pdf_path):
    # Open the JPG image using Pillow
    image = Image.open(input_image_path)

    # Create a PDF file
    pdf_canvas = canvas.Canvas(output_pdf_path, pagesize=letter)

    # Set the size of the PDF page to match the image size
    pdf_canvas.setPageSize((image.width, image.height))

    # Draw the image onto the PDF canvas
    pdf_canvas.drawInlineImage(input_image_path, 0, 0, width=image.width, height=image.height)

    # Save the PDF file
    pdf_canvas.save()

if __name__ == "__main__":
    # Specify the path to the input JPG image
    input_image_path = "./collage.jpg"

    # Specify the output path for the PDF
    output_pdf_path = "./output.pdf"

    # Create the PDF from the JPG image
    create_pdf_from_jpg(input_image_path, output_pdf_path)

    print(f"PDF created at: {output_pdf_path}")