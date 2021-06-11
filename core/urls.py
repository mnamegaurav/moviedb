from django.urls import path, include

from core.views import MoviesAPIView, CommentsAPIView

apiurlpatterns = [

    # GET/POST
    path('movies/', MoviesAPIView.as_view(), name='movies_api_view'),

    # GET/POST
    path('comments/', CommentsAPIView.as_view(), name='comments_api_view'),
]

urlpatterns = [
    path('api/', include(apiurlpatterns))
]
