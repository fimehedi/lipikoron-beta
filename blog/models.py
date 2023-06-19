from django.utils.timezone import datetime
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField


class category(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(unique=True, help_text="Must be Unique & English")

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class article(models.Model):
    author      = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )
    title       = models.CharField(max_length = 200)
    body        = RichTextUploadingField()
    posted_on   = models.DateTimeField(default=datetime.now())
    updated_on  = models.DateTimeField(auto_now = True, auto_now_add = False)
    category    = models.ForeignKey(category, on_delete = models.CASCADE)
    thumbnail   = models.FileField()
    likes       = models.ManyToManyField(get_user_model(), related_name='like_post', blank=True)
    views       = models.IntegerField(default=0, editable=False)
    bookmark    = models.ManyToManyField(get_user_model(), related_name='bookmark', blank=True)

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='published'
    )

    def delete(self, *args, **kwargs):
        self.thumbnail.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


class FeaturedPost(models.Model):
    post = models.OneToOneField(article, on_delete=models.CASCADE)

    POSITION_CHOICES = (
        (1, 'Top'),
        (2, 'Middle'),
        (3, 'Down'),
    )

    position = models.IntegerField(
        choices=POSITION_CHOICES,
        unique=True
    )

    def __str__(self):
        return f"{self.post} on {self.position} position"


class comment(models.Model):
    post            = models.ForeignKey(article, on_delete = models.CASCADE)
    user            = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post_comment    = models.TextField(max_length = 250)
    posted_on       = models.DateTimeField(auto_now = False, auto_now_add = True)

    def __str__(self):
        return self.user.get_full_name() + 'Comment on ' + self.post.title

class Report(models.Model):
    user    = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post_id = models.ForeignKey(article, on_delete=models.CASCADE)
    report  = models.TextField()

    def __str__(self):
        return self.report[:30]
