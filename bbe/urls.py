from django.urls import path
from bbe import views
from bbe import api_views

app_name = "bbe"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("login", views.Login.as_view(), name="login"),
    path("mon-client", views.Profile.as_view(), name="profile"),
    path("register", views.Register.as_view(), name="register"),
    path("logout", views.Logout.as_view(), name="logout"),
    path(
        "api/product/all/<str:f>", api_views.get_all_products, name="api_all_products"
    ),
    path(
        "api/product/image/<int:pk>",
        api_views.get_product_image,
        name="api_image_product",
    ),
    path(
        "api/product/search/<str:filter_query>",
        api_views.search_product,
        name="search_product",
    ),
]
