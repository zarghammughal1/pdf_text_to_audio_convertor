"""
    The code will covert the text of pdf into the audio.
    Libraries that should be installed are:
        pip install PyPDF4
        pip install gTTS
"""

from PyPDF4 import PdfFileReader
from gtts import gTTS

def pdf_to_audio(file_name):
    pdf = PdfFileReader(file_name)
    for page in range(pdf.getNumPages()):
        text = pdf.getPage(page).extractText()
        tts = gTTS(text=text, lang='en')
        tts.save(f"{page}.mp3")

pdf_to_audio("File.pdf")