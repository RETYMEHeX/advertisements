from django.urls import path
from .views import index, top_sellers, post_adv

urlpatterns = [
    path('', index, name="main"),
    path('top-sellers/', top_sellers, name="sellers"),
    path('advertisement-post/', post_adv, name="post_adv")
]