from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("posts", views.posts, name="posts-page"), # We can use the feature name, so we can then build these paths dynamically from views.py with the reverse function or from the styling templates with the url tag for example
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page") #Same way we have the int and str transformers, we have the slug transformer which will look for and apply the syntax "/characters-and-or-numbers". Again, slug is a broadly name to refer to the dynamic segment that carries on the value which will ultimately be use as a parameter from our view 
]