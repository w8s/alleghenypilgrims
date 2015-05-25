from django.db import models
from django.contrib.auth.models import User
# from dauxer.core.models import DauxerUser
from django.conf import settings
from django.forms import ModelForm

class PilgrimUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username',
                 'first_name',
                 'last_name',
                 'email'
                 ]
