import qrcode

"""Paste your link here"""
print ("Link : " )
link = input()

"""Name the files in the directory"""
print ("File Name : ")
name = input()

"""Your file automatically the extension is (.jpg) . you can edit to other image files """
makel = qrcode.make(link)
makel.save(name +".jpg")