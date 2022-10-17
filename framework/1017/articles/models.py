from imagekit.models import ProcessedImageField
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from imagekit.processors import ResizeToFill
from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ## imgge 필드 지정 > Pillow 라이브러리 필요
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    image_thumbnail = ImageSpecField(
		                            source = 'image', 		   # 원본 ImageField 명
		                            processors = [Thumbnail(100, 100)], # 처리할 작업목록
		                            format = 'JPEG',		   # 최종 저장 포맷
		                            options = {'quality': 60}) # 저장 옵션
    # thumbnail = ProcessedImageField(upload_to='images/', blank=True,
    #                             processors=[ResizeToFill(400, 300)],
    #                             format='JPEG',
    #                             options={'quality': 80})