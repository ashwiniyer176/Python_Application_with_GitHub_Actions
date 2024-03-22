"""
Module to script everything. Entrypoint to this parser
"""

from resume_parser import ResumeParser

if __name__ == "__main__":
#To store extracted resumes
    #Select a path to the file - code needs os.path #to be addded
    RESUME_PATH = "assets/Ashwin_U_Iyer_s_Resume.pdf"
    #Invoking document parsers based on file format
    #Note: for TXT - do a normal f.read()
    parser = ResumeParser(RESUME_PATH)
    print(type(parser.resume_text))
