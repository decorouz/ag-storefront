import pytest
from django.contrib.auth.models import User
from rest_framework import status


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post("/store/collections/", collection)

    return do_create_collection


@pytest.fixture
def authenticate(api_client):
    def do_authenticate(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))

    return do_authenticate


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_return_401(self, create_collection):
        response = create_collection({"title": "a"})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_nit_admin_return_403(self, create_collection, authenticate):
        authenticate()

        response = create_collection({"title": "a"})

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, create_collection, authenticate):
        authenticate(is_staff=True)

        response = create_collection({"title": ""})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["title"] is not None

    def test_if_data_is_valid_return_201(self, create_collection, authenticate):
        authenticate(is_staff=True)

        response = create_collection({"title": "a"})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["id"] > 0
