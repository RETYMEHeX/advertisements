from django.urls import path
from .views import index, top_sellers, post_adv, adv_detail

urlpatterns = [
    path('', index, name="main"),
    path('top-sellers/', top_sellers, name="sellers"),
    path('advertisement-post/', post_adv, name="post_adv"),
    path('advertisement/<int:pk>', adv_detail, name="adv-detail")
]