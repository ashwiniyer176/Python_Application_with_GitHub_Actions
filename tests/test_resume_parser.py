"""
Test cases for reume_parser module
"""
import os
import sys

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)
from resume_parser import ResumeParser

def test_resume_parser_for_pdf():
    """
    Test if the resume parser is capable of parsing a pdf
    """
    RESUME_PATH = "assets/Ashwin_U_Iyer_s_Resume.pdf"
    #Invoking document parsers based on file format
    #Note: for TXT - do a normal f.read()
    parser = ResumeParser(RESUME_PATH)
    assert type(parser.resume_text) == str