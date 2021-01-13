from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("watchlist", views.watchlist, name = "watchlist"),
    path("listing/<int:listing_id>", views.viewlisting, name="listing"),
    path("addwatchlist/<int:listing_id>", views.addwatchlist, name = "addwatchlist"),
    path("addcomment/<int:listing_id>", views.addcomment, name = "addcomment"),
    path("makebid/<int:listing_id>", views.makebid, name = "makebid"),
    path("category/<str:category>", views.category, name = "category"),
    path("closelisting/<int:listing_id>", views.closelisting, name = "closelisting"),
    path("closelistings", views.closedlistings, name = "closedlistings")
]
