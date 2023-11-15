import PyPDF2
import matplotlib.pyplot as plt
import numpy as np

#xpoints = np.array([0, 6])
#ypoints = np.array([0, 250])

#plt.plot(xpoints, ypoints)
#plt.show()

def ExtractText(pdf_file_path: str) -> str:

    with open(pdf_file_path, 'rb') as file_object:
        PDFRead = PyPDF2.PdfReader(file_object)
        Total = ""

        for page_num in range(len(PDFRead.pages)):
            page = PDFRead.pages[page_num]
            Content = page.extract_text()
            Total += Content

        return Total

if __name__ == '__main__':
    pdf_text = ExtractText('sample.pdf')
    print(pdf_text)