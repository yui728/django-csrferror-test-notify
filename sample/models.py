from django.db import models

# Create your models here.
class Sample(models.Model):
    """サンプルアプリケーションモデル"""
    class Meta:
        # テーブル名
        db_table = 'sample'

    message = models.CharField(verbose_name='メッセージ', max_length=255)