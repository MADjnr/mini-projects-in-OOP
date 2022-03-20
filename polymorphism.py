


class File:
    def __init__(self, name, extension):
        self.name = name
        self.extension = extension

    def open():
        print("Opening a generic file...")


class PDFFile(File):

    def __init__(self, name):
        File.__init__(self, name, ".pdf")

    def open(self):
        print("Opening a PDF File...")


class TextFile(File):

    def __init__(self, name):
        File.__init__(self, name, ".txt")

    def open(self):
        print("Opening a Text File...")


def open_files(files):
    for file in files:
        file.open()
        return file


pdf1 = PDFFile("Brochure")
pdf2 = PDFFile("Course Advertising")
text1 = TextFile("List of Students")

files = [pdf1, text1, pdf2]

openfile = open_files(files)