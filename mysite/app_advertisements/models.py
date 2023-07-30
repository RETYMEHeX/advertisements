from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=60)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    is_auction = models.BooleanField("Уместен ли торг", help_text="Отметьте если торг по обЪявлению уметсен.")
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)
    @admin.display(description="Дата публикации")
    def created_date(self):
        from django.utils import timezone

        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html("<span style='color: green; font-weight: bold;'>Сегодня в {}</span>", created_time)
        return self.created_at.strftime("%d.%m.%Y - %H:%M")

    @admin.display(description="Дата обновления публикации")
    def updated_date(self):
        from django.utils import timezone

        if self.created_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html("<span style='color: yellow; font-weight: bold;'>Сегодня в {}</span>", created_time)
        return self.updated_at.strftime("%d.%m.%Y - %H:%M")

    class Meta:
        db_table = "advertisements"

    def __str__(self):
        return f"id={self.id}, title={self.title}, price={self.price}"
