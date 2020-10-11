from django.shortcuts import render

from .forms import AudioBookForm

import pyttsx3
import PyPDF2

# Start the TTS Service.
speaker = pyttsx3.init()

rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate - 20)


def upload_file(request):
    form = AudioBookForm()
    instance = None

    if request.method == 'POST':
        form = AudioBookForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save()
            book = instance.file_field.url
            print(book)

            with open(f"src/{book}", 'rb') as pdf:
                reader = PyPDF2.PdfFileReader(pdf)
                pages = reader.numPages

                complete_text = ""

                for page in reader.pages:
                    # page = reader.getPage(pg)
                    text = page.extractText()
                    print(text)

                    complete_text += text

                print("Extracted!")

            speaker.save_to_file(complete_text, 'src/static/pdf.mp3')
            print("Saved.")

            # Run the Service.
            speaker.runAndWait()

    context = {
        'form': form,
        'file': False if not instance else True,
    }
    return render(request, 'audiobook/index.html', context)
