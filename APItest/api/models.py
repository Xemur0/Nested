from django.db import models

# Create your models here.


class Post(models.Model):
    """Модель статьи"""
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Статья"

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Комментарии
    Родитель коммента, к нему привязка дочернего по id
    """
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=500)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL,
        blank=True, null=True, related_name='children',
    )
    post = models.ForeignKey(Post, verbose_name="Статья",
                             on_delete=models.CASCADE, related_name='comment')
    level = 0

    def __str__(self):
        return f"{self.name} - {self.post}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
