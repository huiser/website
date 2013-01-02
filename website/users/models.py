from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

class WebsiteUserManager(BaseUserManager):
    def create_user(self, email, password, firstname, lastname):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=WebsiteUserManager.normalize_email(email),
            firstname=firstname,
            lastname=lastname)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, firstname, lastname):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=WebsiteUserManager.normalize_email(email),
            firstname=firstname,
            lastname=lastname)
        user.set_password(password)
        user.is_staff = True
        user.save(using=self._db)
        return user

class WebsiteUser(AbstractBaseUser):
    email = models.EmailField(unique=True, db_index=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    start = models.DateField(auto_now_add = True)
    end = models.DateField(null = True, blank = True)
    #superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))

    objects = WebsiteUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['firstname', 'lastname', 'start', ]

    def get_full_name(self):
        fullname = u"%s %s" % (self.firstname, self.lastname)
        return fullname.strip()

    def get_short_name(self):
        return self.lastname
