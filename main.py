
from pypdf import PdfReader

reader = PdfReader("assets/Ashwin_U_Iyer_s_Resume.pdf")

# See what is there:
print(str(reader.metadata))
print(reader.get_page_number())
# Or just access specific values:
print(reader.metadata.creation_date)  # that is actually a datetime object!