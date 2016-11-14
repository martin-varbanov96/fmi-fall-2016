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


# TODO::May need image class in future