import django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for user profile"""
    
    def create_user(self,email,name,password=None):
        """Create new user"""
        if not email:
            raise ValueError('Users must have an Email') #checking if passed email has value not null nor empty
        
        email = self.normalize_email(email) # normalize_email normalizes second half after the @ in the email
        user = self.model(email=email, name=name) # Creating the user using model
        
        user.set_password(password) # Setting password Hashed
        user.save(using=self._db) # standard django way to save, to enable multiple databases of needed
        
        return user
    
    def create_superuser(self,email,name,password):
        """Create new superuser with given details"""
        
        user = self.create_user(email,name,password) # creating standard user first
        
        user.is_superuser = True # Came from PermissionsMixin to our UserProfile model
        user.is_staff = True
        user.save(using=self._db)
        
        return user    


class UserProfile (AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        """Retrive full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrive short name of user"""
        return self.name
    
    def __str__(self):
        """Retutn string represntation for our username
        """
        return self.email
    
    
class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        """Return the model as string"""
        return self.status_text