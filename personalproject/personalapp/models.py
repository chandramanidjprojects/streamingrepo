from django.db import models
from django.db.models import Count
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from PIL import Image
from django.contrib.auth import get_user_model
from django.utils import timezone
class BaseManager(BaseUserManager):
    def create_user(self,email,password,admin=False,staff=False,active=True):
        if not email:
            raise ValueError('email required')
        if not password:
            raise ValueError('password required') 
        user=self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.admin=admin
        user.staff=staff
        user.active=active
        user.save(using=self._db)
        return user       
    def create_superuser(self,email,password):
        user=self.create_user(email,password,admin=True,staff=True,active=True)
        return user
class User(AbstractBaseUser):
    email=models.EmailField(max_length=255,unique=True)
    username=models.CharField(max_length=255,blank=True,null=True)
    profile=models.ImageField(default='mani.jpg',upload_to='profile_pictures')
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    active=models.BooleanField(default=True)
    active_state=models.BooleanField(default=False)
    user_subscription=models.BooleanField(default=False)
    updated_at=models.DateTimeField(default=timezone.now)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=BaseManager()
    
    def __str__(self):
        return self.email
    def has_module_perms(self,apps_label):
        return True
    def has_perm(self,perm,obj=None):
        return True        
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active

class Post(models.Model):
    post_by=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    file=models.FileField(blank=True,null=True,upload_to='posts')
    date_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.file}'
    
class PostLike(models.Model):
    like_by=models.IntegerField()
    like_to=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_like')

class Comment(models.Model):
    comment_by=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,null=True,blank=True)
    comment_to=models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True)
    comment_text=models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.comment_to}'
    @property
    def get_comment_by_info(self):
        return {'name':self.comment_by.username,'profile':f'http://192.168.43.58:8000{self.comment_by.profile.url}'}    















