from django.db import models
from django.conf import settings
from django.urls import  reverse


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.TextField(null=False)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to='diary/post/%Y%m%d')
    created_at = models.DateTimeField() # auto 풀었음
    updated_at = models.DateTimeField(auto_now=True)
    #auto_now 는 자동으로 디비에 저장된다.
    #register to admin

    # Java 의 toString 과 같은 기능
    def __str__(self):
        return self.message

    class Meta: #inner class 로 기본정렬을 지정. 쿼리를 날릴때 마다 order_by 를 자동으로 날린다.
        ordering=['-created_at']

    # def get_absolute_url(self):
    #     return reverse('instagram:post_detail', args=[self.pk])
    # def message_length(self):
    #     return len(self.message)
    # message_length.short_description ="메세지 글자수"