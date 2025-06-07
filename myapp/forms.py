import json
from datetime import datetime

from django import forms


class JsonUploadForm(forms.Form):
    json_file = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={
                "class": (
                    "block w-full text-sm text-gray-500 "
                    "file:py-3 file:px-4 "
                    "file:rounded-xl file:border-0 "
                    "file:text-sm file:font-semibold "
                    "file:bg-gradient-to-r file:from-blue-100 file:to-indigo-100 "
                    "file:text-indigo-700 "
                    "hover:file:bg-gradient-to-r hover:file:from-indigo-100 hover:file:to-blue-100 "
                    "cursor-pointer"
                )
            }
        )
    )

    def clean_json_file(self):
        file = self.cleaned_data["json_file"]
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            raise forms.ValidationError("Файл не является валидным JSON.")

        if not isinstance(data, list):
            raise forms.ValidationError("JSON должен быть списком объектов.")

        for i, item in enumerate(data):
            if not isinstance(item, dict):
                raise forms.ValidationError(f"Элемент {i} не является объектом.")

            name = item.get("name", None)
            date = item.get("date", None)

            if not name:
                raise forms.ValidationError("Поле 'name' - обязательное")

            if not date:
                raise forms.ValidationError("Поле 'date' - обязательное")

            if not isinstance(name, str) or len(name) >= 50:
                raise forms.ValidationError(
                    f"Поле 'name' элемента {i} должно быть строкой менее 50 символов."
                )

            if not isinstance(date, str):
                raise forms.ValidationError(f"Поле 'date' элемента {i} должно быть строкой.")

            try:
                datetime.strptime(date, "%Y-%m-%d_%H:%M")
            except ValueError:
                raise forms.ValidationError(
                    f"Поле 'date' элемента {i} должно быть в формате YYYY-MM-DD_HH:mm."
                )

        file.seek(0)
        return file
