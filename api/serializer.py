from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer, EmailField, CharField


class UserLoginSerializer(ModelSerializer):
    username = CharField()
    email = EmailField()
