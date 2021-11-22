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
	name = models.CharField(max_length=100, null=True)

	def __str__(self):
		return f'{self.name}'

class Post(models.Model):
	CHOICES = (
		('published', 'Published'), 
		('draft', 'Draft'),
	)

	title = models.CharField(max_length=50, null=True)
	content = models.CharField(max_length = 1000, null=True)
	auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	status = models.CharField(max_length=10, choices=CHOICES, default='publish', null=True)
	published = models.DateTimeField(default=timezone.now, null=True)
	created = models.DateTimeField(auto_now_add=True, null=True)
	# slug = models.AutoSlugField(populate_from = ['title',], unique_for_date='created', null=True)
	slug = models.SlugField(null=True, unique_for_date='created')
	updated = models.DateTimeField(auto_now = True, null=True)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
	image = models.ImageField(upload_to = user_directory_path, default='posts/default.jpg')


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
	content = models.TextField(null=True)
	published = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)
	name = models.CharField(max_length=100, null=True)


	class Meta:
		ordering = ('published',)


	def __str__(self):
		return f'Comment by {self.name}'




