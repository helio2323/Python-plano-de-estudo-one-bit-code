import PyPDF2 as pdf
from PyPDF2 import PdfReader
from PIL import Image

def convert_img_pdf(image_file):
    my_image = Image.open(image_file)
    img = my_image.convert("RGB")
    filename = f"{os.path.splitext(image_file)[0]}.pdf"
    img.save(filename)

convert_img_pdf("files/IM14.jpg")