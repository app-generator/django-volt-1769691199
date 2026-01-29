# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Dinghy_Type(models.Model):

    #__Dinghy_Type_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    py = models.IntegerField(null=True, blank=True)

    #__Dinghy_Type_FIELDS__END

    class Meta:
        verbose_name        = _("Dinghy_Type")
        verbose_name_plural = _("Dinghy_Type")


class League(models.Model):

    #__League_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    desciption = models.CharField(max_length=255, null=True, blank=True)

    #__League_FIELDS__END

    class Meta:
        verbose_name        = _("League")
        verbose_name_plural = _("League")


class Race(models.Model):

    #__Race_FIELDS__
    date_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    #__Race_FIELDS__END

    class Meta:
        verbose_name        = _("Race")
        verbose_name_plural = _("Race")


class Race_Participant(models.Model):

    #__Race_Participant_FIELDS__
    participant = models.CharField(max_length=255, null=True, blank=True)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    dinghy = models.ForeignKey(Registered_Dinghy, on_delete=models.CASCADE)
    role = models.ForeignKey(Race_Role, on_delete=models.CASCADE)

    #__Race_Participant_FIELDS__END

    class Meta:
        verbose_name        = _("Race_Participant")
        verbose_name_plural = _("Race_Participant")


class Race_Role(models.Model):

    #__Race_Role_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Race_Role_FIELDS__END

    class Meta:
        verbose_name        = _("Race_Role")
        verbose_name_plural = _("Race_Role")


class Registered_Dinghy(models.Model):

    #__Registered_Dinghy_FIELDS__
    sail_number = models.CharField(max_length=255, null=True, blank=True)
    dinghy_type = models.ForeignKey(Dinghy_Type, on_delete=models.CASCADE)

    #__Registered_Dinghy_FIELDS__END

    class Meta:
        verbose_name        = _("Registered_Dinghy")
        verbose_name_plural = _("Registered_Dinghy")



#__MODELS__END
