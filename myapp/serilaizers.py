from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from myapp.models import *


class stdnts(serializers.ModelSerializer):
    class Meta:
        model=students
        fields=('id','first_name','last_name','course','email','contact')