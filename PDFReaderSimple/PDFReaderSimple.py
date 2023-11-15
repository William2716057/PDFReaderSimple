import PyPDF2

def ExtractText(pdf_file_path: str) -> str:

    with open(pdf_file_path, 'rb') as file_object:
        PDFRead = PyPDF2.PdfReader(file_object)
        total_text = ""

        for page_num in range(len(PDFRead.pages)):
            page = PDFRead.pages[page_num]
            text_content = page.extract_text()
            total_text += text_content

        return total_text

if __name__ == '__main__':
    pdf_text = ExtractText('sample.pdf')
    print(pdf_text)