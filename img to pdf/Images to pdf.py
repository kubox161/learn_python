# from fpdf import fpdf
# pdf = fpdf()
# # imagelist is the list with all image filenamesfor image in imagelist:
#     pdf.add_page()
#     pdf.image(image,x,y,w,h)
# pdf.output("yourfile.pdf", "F")


# from PIL import Image
# im1 = Image.open("/IMG_20210824_123340.jpg")
# im2 = Image.open("/IMG_20210824_123352.jpg")
# im3 = Image.open("/IMG_20210824_123413.jpg")
# im_list = [im2,im3]
# pdf1_filename = "/bbd1.pdf"
# im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)


# convert all files matching a glob
import os
import img2pdf
import glob
with open("name.pdf", "wb") as f:
    f.write(img2pdf.convert(glob.glob("C:/Users/user/PycharmProjects/learn_python/*.jpg")))