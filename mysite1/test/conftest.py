import pytest
import django.db
from django.contrib.auth.models import User


@pytest.fixture
def sample_name():
    username = 'Hana'
    return username


@pytest.fixture
def create_user(db, django_user_model):
    def make_user(**kwargs):
        return django_user_model.objects.create_user(**kwargs)
    return make_user
