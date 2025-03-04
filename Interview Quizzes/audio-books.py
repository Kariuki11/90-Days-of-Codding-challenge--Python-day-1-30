# Import necessary libraries
from gtts import gTTS  # Google Text-to-Speech
import PyPDF2  # PDF reading library

# Open and read the PDF file safely
pdf_path = 'Kenneth-Kariuki_Resume (6).pdf'

with open(pdf_path, 'rb') as pdf_file:
    # Create a PDF Reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    count = len(pdf_reader.pages)  # Get total number of pages
    text_list = []

    # Extract text from each page
    for i in range(count):
        try:
            page = pdf_reader.pages[i]  # Access page using new method
            text = page.extract_text()  # Extract text
            if text:  # Avoid adding None values
                text_list.append(text)
        except Exception as e:
            print(f"Error processing page {i}: {e}")

# Convert extracted text into a single string
text_string = " ".join(text_list)

# Debugging: Print extracted text to check if it's empty
print("Extracted Text:", text_string)

# Handle empty text case
if not text_string.strip():
    raise ValueError("No text extracted from the PDF. The document might be scanned or encrypted.")

# Set language to English
language = 'en'

# Convert text to speech
my_audio = gTTS(text=text_string, lang=language, slow=False)

# Save as an MP3 file
audio_filename = "Audio.mp3"
my_audio.save(audio_filename)

print(f"Audio file saved as '{audio_filename}'")
































# #Importing Libraries
# #Importing Google Text to Speech library
# from gtts import gTTS

# #Importing PDF reader PyPDF2
# import PyPDF2

# #Open file Path
# pdf_File = open('Kenneth-Kariuki_Resume (6).pdf', 'rb') 

# #Create PDF Reader Object
# # pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
# pdf_Reader = PyPDF2.PdfReader(pdf_File)
# # count = pdf_Reader.numPages # counts number of pages in pdf
# count = len(pdf_Reader.pages)  # counts number of pages in pdf
# textList = []

# #Extracting text data from each page of the pdf file
# for i in range(count):
#    try:
#     page = pdf_Reader.getPage(i)    
#     textList.append(page.extractText())
#    except:
#        pass

# #Converting multiline text to single line text
# textString = " ".join(textList)

# print(textString)

# #Set language to english (en)
# language = 'en'

# #Call GTTS
# myAudio = gTTS(text=textString, lang=language, slow=False)

# #Save as mp3 file
# myAudio.save("Audio.mp3")