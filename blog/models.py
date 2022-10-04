from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    #auto_now_add = True (추가 되었을 시 자동으로 시간 추가)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author: 추후 작성
    def __str__(self):
        return f'[{self.pk}] {self.title}'
