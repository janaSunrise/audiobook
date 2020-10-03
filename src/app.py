import pyttsx3
import PyPDF2
from colorama import Fore, init

import json
import sys

# Initialize colorama
init(autoreset=True)

# read the JSON File
with open('config.json', 'r') as file:
    data = json.load(file)

book = data["book_location"].strip()

# Do all the error handling.
if book == "":
    print(f"{Fore.RED} The PDF File location isnt provided in the config.json file. Please add it.")
    sys.exit(1)

if not book.endswith(".pdf"):
    print(f"{Fore.RED} The File Provided in the config.json File, isn't a PDF File.")
    sys.exit(1)

# Start the TTS Service.
speaker = pyttsx3.init()

# If all checks are successful, Open the PDF File
with open(book, 'rb') as pdf:
    pdfReader = PyPDF2.PdfFileReader(pdf)
    print(f"{Fore.YELLOW} Opening the PDF Book - {book.split('/')[-1]}")

    pages = pdfReader.numPages

    try:
        page = int(input("Enter which page number to start: "))
    except ValueError:
        print(f"{Fore.YELLOW} The Page number must be an integer!")

    if page <= 0 and (pages - page) < 0:
        print(f"{Fore.RED} Invalid page number! It must be between 1 and {pages - 1}")
        sys.exit(1)

    for pg in range(page, pages):
        # Extract the Data.
        page = pdfReader.getPage(pg)
        text = page.extractText()

        # Make the text be spoken!
        speaker.say(f"Reading Page {pg} {text}")
        print(f"{Fore.CYAN} Reading Page {pg}")

        # Run the Service.
        speaker.runAndWait()

print(f"\n{Fore.GREEN} Successfully Read the book specified.")
