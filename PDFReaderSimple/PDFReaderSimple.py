import PyPDF2
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter 
cnt = Counter()
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
    PDFText = ExtractText('sample.pdf')
    print(PDFText)


#for text in PDFText.split():
    #cnt[text] += 1
    #most common words
    #cnt.most_common(10)
    #print(cnt.most_common)
