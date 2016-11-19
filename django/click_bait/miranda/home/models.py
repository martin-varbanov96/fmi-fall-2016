from django.db import models

class Post(models.Model):
	topic_title = models.CharField(max_length=50)
	topic_text = models.TextField()
	topic_pub_date = models.DateTimeField('date published')
	topic_resume = models.TextField()
	topic_likes = models.IntegerField()
	topic_image_url = models.TextField()
	topic_seo_title = models.TextField(blank=True)
	topic_seo_description = models.TextField(blank=True)
	topic_seo_keywords = models.TextField(blank=True)
	
	def __str__(self):
		return "Post " + self.topic_title + " with resume: " + self.topic_resume + " has been published on: "

class Image(models.Model):
	image_name = models.TextField(max_length=50)
	image_alt = models.TextField(max_length=200)
	image_path = models.TextField()

class Image_Post(models.Model):
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)