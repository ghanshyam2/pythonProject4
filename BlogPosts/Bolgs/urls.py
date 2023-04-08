from django.urls import path
from Bolgs import views
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    path('openapi', get_schema_view(
            title="Your Project",
            description="API for all things …",
            version="1.0.0"
        ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>',views.PostDetails.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)