from django.shortcuts import render

from .forms import AudioBookForm

import pyttsx3
import pdfplumber as plumber

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

            with plumber.open(f"./{book}") as pdf:
                pages = pdf.pages

                complete_text = ""

                for page in pages:
                    text = page.extract_text()

                    complete_text += text

                print("Extracted!")

            speaker.save_to_file(complete_text, './static/pdf.mp3')
            print("Saved.")

            # Run the Service.
            speaker.runAndWait()

    context = {
        'form': form,
        'file': False if not instance else True,
    }
    return render(request, 'audiobook/index.html', context)
