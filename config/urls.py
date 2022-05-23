from django.contrib import admin
from django.urls import include, path

admin.site.site_header = "Store Front Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("store/", include("store.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("__debug__/", include("debug_toolbar.urls")),
]
