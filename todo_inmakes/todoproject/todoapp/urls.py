
from django.urls import path

from todoapp import views

appname="todoapp"

urlpatterns = [
    path('',views.add,name="add"),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('listview/',views.Tlistview.as_view(),name="listview"),
    path('detailview/<int:pk>',views.Tdetailview.as_view(),name="detailview"),
    path('updateview/<int:pk>',views.Tupdateview.as_view(),name="updateview"),
    path('deleteview/<int:pk>',views.Tdeleteview.as_view(),name="deleteview")
]
