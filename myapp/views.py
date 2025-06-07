import json

from django.shortcuts import render

from .forms import JsonUploadForm
from .models import Record


def index(request):
    success_message = None

    if request.method == "POST":
        form = JsonUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Получаем файл
            json_file = form.cleaned_data["json_file"]

            # Читаем и парсим JSON (сброс указателя файла перед чтением)
            json_file.seek(0)
            data = json.load(json_file)

            # Создаём объекты Record из данных
            for item in data:
                Record.objects.create(
                    name=item["name"],
                    date=item["date"].replace("_", "T"),  # форматируем строку в ISO
                )

            # Сообщение об успехе
            success_message = "JSON успешно загружен и сохранён."

            # Создаём пустую форму для новой загрузки
            form = JsonUploadForm()
    else:
        form = JsonUploadForm()

    return render(request, "index.html", {"form": form, "success_message": success_message})


def records_list(request):
    records = Record.objects.all()
    return render(request, "records_list.html", {"records": records})
