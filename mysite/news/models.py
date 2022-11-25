from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150)  # Varcharm длинной не более 150 символов
    content = models.TextField(blank=True)   # Длинный текст. blank - может быть не заполнен
    created_at = models.DateTimeField(auto_now_add=True)  # Дата и время будут созданы один раз и меняться не будут
    update_at = models.DateTimeField(auto_now=True)  # Дата и время будут созданы и изменятся при редактировании
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # Только изображения. FileField разные файлы. Создает 3 папки
    is_published = models.BooleanField(default=True)
