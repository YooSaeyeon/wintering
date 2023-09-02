from django.db import models

# Create your models here.
class post(models.Model):
    name = models.CharField(verbose_name="성함", max_length=128)
    phoneNumber = models.CharField(verbose_name="전화번호 뒷자리", max_length=128)
    inviterName = models.CharField(verbose_name="초대자이름", max_length=128)

    COMPLETE_CHOICES = (
        ('예', '예'),
        ('아니요', '아니요'),
    )

    complete = models.CharField(
        verbose_name="입금을 하셨나요?",
        choices=COMPLETE_CHOICES,
        max_length=10,
        default='아니요'  # 기본값을 '아니요'로 설정
    )

    def __str__(self):
        return self.phoneNumber