#Preferably runs well on the local device 
#likely vscode

import PyPDF2

# Function to split PDF into individual pages
def split_pdf(input_pdf_path):
    # Open the input PDF
    with open(input_pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        
        # Iterate through all the pages in the PDF
        for page_num in range(len(reader.pages)):
            writer = PyPDF2.PdfWriter()
            current_page = reader.pages[page_num]
            
            # Add the current page to the writer
            writer.add_page(current_page)
            
            # Output file name for each page (e.g., page_1.pdf, page_2.pdf, etc.)
            output_pdf_path = f'page_{page_num + 1}.pdf'
            
            # Write the single page to a new PDF file
            with open(output_pdf_path, 'wb') as output_pdf:
                writer.write(output_pdf)
                
            print(f'Page {page_num + 1} saved as {output_pdf_path}')

# Example usage
input_pdf_path = "C:/Users/patel/OneDrive/Desktop/5-Lab-file[1].pdf"  # Path to your input PDF
split_pdf(input_pdf_path)
