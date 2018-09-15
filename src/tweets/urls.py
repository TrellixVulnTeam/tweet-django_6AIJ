from django.urls import path 
from .views import TweetDetailView , TweetListView , TweetCreateView , TweetUpdateView , TweetDeleteView
from django.views.generic.base import RedirectView
app_name = 'tweets'

urlpatterns = [
    #spath('admin/', admin.site.urls),
    path('<int:pk>/', TweetDetailView.as_view(), name='detail'),
    path('search/', TweetListView.as_view(), name='list'),
    path('new/',TweetCreateView.as_view() , name ='create' ),
    path('<int:pk>/delete/',TweetDeleteView.as_view(), name = 'delete'),
    path('<int:pk>/update/',TweetUpdateView.as_view() , name = 'update'),
    path('',RedirectView.as_view(url='/') )

]

