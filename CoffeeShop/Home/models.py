from django.db import models


class AboutUs(models.Model):
    title = models.CharField(verbose_name="Chủ đề" ,max_length=200)
    content = models.TextField(verbose_name="Nội dung")
    image = models.ImageField(verbose_name="Hình ảnh", upload_to='about_us_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title
    class Meta:
        # tên model biểu thị trong admin
        verbose_name_plural = "Giới thiệu (About us)"

class OurTeam(models.Model):
    memberName = models.CharField(verbose_name="Tên thành viên" ,max_length=200)
    position = models.CharField(verbose_name="Vị trí" ,max_length=200)
    avatar = models.ImageField(verbose_name="Ảnh đại diện", upload_to='our_team_images/', blank=True, null=True)
    facebook = models.URLField(verbose_name="Facebook", blank=True, null=True)
    instagram = models.URLField(verbose_name="Instagram", blank=True, null=True)
    twitter = models.URLField(verbose_name="Twitter", blank=True, null=True)
    email = models.EmailField(verbose_name="Email", blank=True, null=True)


    def __str__(self):
        return self.memberName
    class Meta:
        verbose_name_plural = "Thành viên đội (Team Members)"