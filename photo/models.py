from django.db import models

# Create your models here.

# 장고의 기본 유저 모델
from django.contrib.auth.models import User
from django.urls import reverse


# 외래키(ForeignKey) - User 테이블에서 해당 유저를 찾을 수 있는 주키
# 주키(PrimaryKey) -
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[self.id])