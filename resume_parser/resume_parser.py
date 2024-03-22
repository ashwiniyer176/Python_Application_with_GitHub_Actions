"""
A Resume Parser built to extract relevant metadata from resumes built on LaTex as PDF or DOCX
"""
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

    def get_pdf_content(self) -> str:
        """
        Extract all the text in a PDF resume

        Returns:
            str: All the content of the resume as a string
        """
        path = self.file_path
        content = ""
        # Load PDF into pypdf
        with open(path,"rb") as resume_file:
            pdf = pypdf.PdfReader(resume_file)
            # Iterate pages
            for i, page in enumerate(pdf.pages):
                page_number = i
                print(f"Extracting page number:{page_number}")
                # Extract text from page and add to content
                content += page.extract_text(extraction_mode="layout") + "\n"
            # Collapse whitespace
            content = " ".join(content.replace("\xa0", " ").strip().split())
            return content

    def get_docx_content(self)-> str:
        """
        Extract all the text in a PDF resume

        Returns:
            str: All the content of the resume as a string
        """
        file_name = self.file_path
        doc = docx.Document(file_name)
        content = ""
        for para in doc.paragraphs:
            content += para.text
        return content
    def parse_resume_text(self)-> dict:
        """
        Parses the extraccted text and find key fields

        Returns:
            dict: Dictionary containing fields as key and information as values
        """
        resume_content={}
        # Define regular expression patterns
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        github_pattern = r'github\.com/[A-Za-z0-9_.-]+'
        phone_pattern = r'\+\d{1,3}-\d{9,10}'
        linkedin_pattern = r'linkedin\.com/[A-Za-z0-9_.-]+'
        website_pattern = r'\b(?:https?://)?(?:www\.)?[\w.-]+\.[a-zA-Z]{2,}(?:/\S*)?\b'
        # Find matches using regex
        resume_content["email"] = re.findall(email_pattern, self.resume_text)
        resume_content["github"] = re.findall(github_pattern, self.resume_text)
        resume_content["phone"] = re.findall(phone_pattern, self.resume_text)
        resume_content["linkedin"] = re.findall(linkedin_pattern, self.resume_text)
        resume_content["websites"] = re.findall(website_pattern, self.resume_text)
        print(resume_content,"\n")
        return resume_content
    