from readPDF import readPdf
d = readPdf
path = ""
def callback(str):
    print(str + "")

d.readPdf(path, callback)
