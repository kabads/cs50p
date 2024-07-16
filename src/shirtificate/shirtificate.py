from fpdf import FPDF
from PIL import Image, ImageOps
import sys


def get_name():
    return (input("Name: "))


def process_image(input_file):
    try:
      with Image.open(input_file, mode='r', formats=None) as im_input, Image.open("shirtificate.png", mode='r', formats=None) as shirt:
            im_input = ImageOps.fit(im_input, shirt.size)
            # shirt = shirt.resize(im_input.size)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)


def create_PDF(name, image="shirtificate.png"):
    img = Image.open(image)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    


    pdf.image(img, x=10, y=10, w=190, h=250)
    pdf.set_font("helvetica", "B", 26)
    pdf.set_text_color(220, 255, 255)
    
    
    # Center Text on X axis
    page_width = pdf.w
    to_print = name + " took CS50"
    text_width = pdf.get_string_width(to_print)
    remaining_space = page_width - text_width
    
    x_centered = (page_width - text_width)
    x_position = (x_centered + remaining_space) / 2
    pdf.set_xy(x_position - (text_width / 2), 110)
    pdf.cell(text_width, 0, to_print)
    pdf.output("shirtificate.pdf")


def main():
    name = get_name()
    create_PDF(name)


if __name__ == '__main__':
    main()