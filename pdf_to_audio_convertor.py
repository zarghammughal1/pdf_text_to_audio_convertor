"""
    The code will covert the text of pdf into the audio. This can't convert images or tabe or any other than text into audio.
    Libraries that should be installed are:
        pip install PyPDF4
        pip install gTTS
"""

from PyPDF4 import PdfFileReader
from gtts import gTTS

# Function that convert the pdf text to audio.
def pdf_to_audio(file_name):
    """
    The code will covert the text of pdf into the audio.
    It will save the audio file with mp3 extension.
    """
    pdf = PdfFileReader(file_name)
    for page in range(pdf.getNumPages()):
        text = pdf.getPage(page).extractText()
        tts = gTTS(text=text, lang='en')
        tts.save(f"{page}.mp3")

# Function Calling
# Fil should be in pdf form
pdf_to_audio("File.pdf")
