from django.db import models

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Science', 'Science'),
        ('Business', 'Business'),
        ('Health', 'Health'),
        ('Education', 'Education'),
    ]

    title = models.CharField(max_length=200)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField()
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default='Technology',  # or set to blank=True if not mandatory
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.link == '':
            self.link = None
        super().save(*args, **kwargs)
