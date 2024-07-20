from django.db import models
from ckeditor.fields import RichTextField
from pytube import Playlist


class CourseCategory(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class Course(models.Model):
    image = models.ImageField(upload_to="course_images/", null=True, blank=True)
    category = models.ForeignKey(
        CourseCategory,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    playlist_url = models.CharField(max_length=500)

    def __str__(self):
        return self.title
    
    def save(self):
        super().save()
        if not self.departments.all():
            playlist = Playlist(self.playlist_url)
            cd = CourseDepartment.objects.create(title='Umumiy', course=self)
            for video in playlist.videos:
                title = video.title
                print(video.initial_data)
                try:
                    description = video.initial_data['contents']['twoColumnWatchNextResults']['results']['results']['contents'][1]['videoSecondaryInfoRenderer']['attributedDescription']['content']
                except:
                    description = " "
                video_link = video.embed_url
                CoursePart.objects.create(
                    course_department=cd,
                    title=title,
                    thumb_image=video.thumbnail_url,
                    description=description,
                    video_link=video_link
                )

class CourseDepartment(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='departments'
    )
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class CoursePart(models.Model):
    course_department = models.ForeignKey(
        CourseDepartment,
        on_delete=models.CASCADE,
        related_name='parts'
    )
    title = models.CharField(max_length=150)
    thumb_image = models.ImageField(upload_to='course_part_thumb/')
    description = models.TextField()
    video_link = models.TextField()

    def __str__(self):
        return self.title

class NewsCategory(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="news_category")

    def __str__(self):
        return self.title

class News(models.Model):
    category = models.ForeignKey(
        NewsCategory,
        on_delete=models.CASCADE,
        related_name='news'
    )
    thumb = models.ImageField(upload_to='news_image/')
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title

class Test(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='tests'
    )
    title = models.CharField(max_length=150)

class Question(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    text = RichTextField()

class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='choices'
    )
    text = RichTextField()
    is_correct = models.BooleanField(default=False)