from django.db import models
from django.contrib.auth.models import User
from django.db.models.expressions import OrderBy 
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify



def user_directory_path(inst, file_name):
	return f'posts/{inst.id}/{file_name}'


def get_registred_user(request):
	loged_user = request.user 
	return loged_user

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return f'{self.name}'

class Post(models.Model):
	CHOICES = (
		('published', 'Published'), 
		('draft', 'Draft'),
	)

	title = models.CharField(max_length=50)
	content = models.TextField(max_length = 1000)
	auther = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.CharField(max_length=10, choices=CHOICES, default='publish')
	# slug = models.AutoSlugField(populate_from = ['title',], unique_for_date='created', null=True)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
	image = models.ImageField(upload_to = user_directory_path, default='posts/default.jpg')
	published = models.DateTimeField(default=timezone.now)
	updated = models.DateTimeField(auto_now = True)
	created = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(unique_for_date='created')


	def get_absolute_url(self):
		return reverse('blog:postDetail',args=[self.slug])

	class Meta:
		ordering = ('-published',)

	def __str__(self):
		return self.title 


	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		self.status = 'published'
		super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	content = models.TextField()
	published = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)
	name = models.CharField(max_length=100)


	class Meta:
		ordering = ('published',)


	def __str__(self):
		return f'Comment by {self.name}'




