from django.urls import path
from . import views
urlpatterns = [
    path('',views.ArticleViews,name="articles"),
    path('articles/<int:pk>',views.ArticleDetailsViews,name="detail_articles"),
    path('requestForm/',views.form,name="requestForm"),
    path('editForm/<int:pk>/',views.editForm.as_view(),name="editForm"),
    path('delete/<int:pk>/',views.deleteForm,name="delete"),
    path('signup/',views.signupView,name="signup"),
    path('password_change',views.passwordChange,name="password_change")
]