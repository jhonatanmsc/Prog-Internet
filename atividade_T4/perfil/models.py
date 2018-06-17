from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.ForeignKey('Address', related_name='profile_in_address',on_delete=models.CASCADE)
    profiles = models.ManyToManyField('auth.User')
    profile = models.ForeignKey('auth.User', blank=True, null=True, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def save_from_json(cls, id, name, email, address, *args, **kwargs):
        return cls.objects.create(pk=id, name=name, email=email, address=Address.save_from_json(**address))

class Address(models.Model):
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)

    def __str__(self):
        return self.street

    @classmethod
    def save_from_json(cls, street, suite, city, zipcode, *args, **kwargs):
        return cls.objects.create(street=street, suite=suite, city=city, zipcode=zipcode)

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    body = models.CharField(max_length=300)
    post = models.ForeignKey('Post', related_name='comments_in_post', verbose_name='Todos os comentários',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def save_from_json(cls, postId, id, name, email, body, *args, **kwargs):
        return cls.objects.create(pk=id, name=name, email=email, body=body, post=Post.objects.get(pk=postId))

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    user = models.ForeignKey('User', related_name='user_posts',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @classmethod
    def save_from_json(cls, userId, id, title, body, *args, **kwargs):
        return cls.objects.create(pk=id, title=title, body=body, user=User.objects.get(pk=userId))