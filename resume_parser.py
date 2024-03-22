"""
A Resume Parser built to extract relevant metadata from resumes built on LaTex as PDF or DOCX
"""

import string
import re
import pypdf
import docx

class ResumeParser:
    """
    A Resume Parser built to extract relevant metadata from resumes built on LaTex as PDF or DOCX
    """
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.resume_text = None
        if self.file_path.endswith(".pdf"):
            self.resume_text = self.get_pdf_content()
        elif self.file_path.endswith(".docx"):
            self.resume_text = self.get_docx_content()
        else:
            print("File format is currently not supported")
        
        self.parse_resume_text()
        
    #Extract text from PDF
    def get_pdf_content(self):
        path = self.file_path
        content = ""
        # Load PDF into pypdf
        pdf = pypdf.PdfReader(open(path, "rb"))
        # Iterate pages
        for i in range(0, pdf._get_num_pages()):
            # Extract text from page and add to content
            page = pdf.pages[i]
            content += page.extract_text(extraction_mode="layout") + "\n"
        # Collapse whitespace
        content = " ".join(content.replace(u"\xa0", " ").strip().split())
        return content

    #Extract text from DOCX
    def get_docx_content(self):
        file_name = self.file_path
        doc = docx.Document(file_name)
        content = ""
        for para in doc.paragraphs:
            content += para.text
        return content
    
    def parse_resume_text(self):
        self.resume_content={}
        # Define regular expression patterns
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        github_pattern = r'github\.com/[A-Za-z0-9_.-]+'
        phone_pattern = r'\+\d{1,3}-\d{9,10}'
        linkedin_pattern = r'linkedin\.com/[A-Za-z0-9_.-]+'
        website_pattern = r'\b(?:https?://)?(?:www\.)?[\w.-]+\.[a-zA-Z]{2,}(?:/\S*)?\b'
        
        # Find matches using regex
        self.resume_content["email"] = re.findall(email_pattern, self.resume_text)
        self.resume_content["github"] = re.findall(github_pattern, self.resume_text)
        self.resume_content["phone"] = re.findall(phone_pattern, self.resume_text)
        self.resume_content["linkedin"] = re.findall(linkedin_pattern, self.resume_text)
        self.resume_content["websites"] = re.findall(website_pattern, self.resume_text)
        
        print(self.resume_content)
        
if __name__ == "__main__":
#To store extracted resumes
    #Select a path to the file - code needs os.path #to be addded
    RESUME_PATH = "assets/Ashwin_U_Iyer_s_Resume.pdf"
    #Invoking document parsers based on file format
    #Note: for TXT - do a normal f.read()
    parser = ResumeParser(RESUME_PATH)
    print(type(parser.resume_text))
    
