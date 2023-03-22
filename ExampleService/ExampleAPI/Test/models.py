from django.db import models

# Create your models here.
class TestModel(models.Model):
    """
    클래스 방식으로 디비에 모델 등록 (현재는 sqlite3)
    """
    name = models.CharField(max_length=50)
    body = models.TextField()

