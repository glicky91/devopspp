
import pytest


def general_1():
    value = 10
    return value


def general_2():
    some_int = 10
    return some_int


def test_1():
    assert general_2() == general_1()


def test_2(sample_name):
    assert sample_name == 'Hana'


@pytest.mark.django_db
def test_fixture_create_user(create_user):
    user = create_user(email='foo@bar.com', password='bar')
    assert user.is_authenticated is True  # <-- this should be False but it's True
    assert user.is_anonymous is True      # <-- this fails
