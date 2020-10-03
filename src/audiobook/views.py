from django.shortcuts import render, redirect

from .forms import AudioBookForm


def upload_file(request):
    form = AudioBookForm()

    if request.method == 'POST':
        form = AudioBookForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data.get('file_field'))
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'audiobook/index.html', context)
