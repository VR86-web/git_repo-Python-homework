from django.urls import path

from urlsAndViews.departments.views import index, view_with_name, view_with_name_variable, view_with_int_pk, \
    view_with_slug, redirect_to_softuni, redirect_to_view

urlpatterns = [
    path('', index, name='home'),
    path('softuni/', redirect_to_softuni),
    path('<int:pk>/', view_with_int_pk),
    path('redirect-to-view/', redirect_to_view),
    path('<slug:slug>/', view_with_slug),
    path('<variable>/', view_with_name_variable),
    path('<param>/', view_with_name),
    path('<path:variable>/', view_with_name)
]