"""
mysite/url.pyから派生するurlを格納するファイル
"""
from django.urls import path
from . import views

##urlディスパッチャ
app_name = 'equipments'
urlpatterns = [
  path('', views.index, name='index'),
  path('approve/',views.approval,name='approval'),
  path('mylist/',views.mylist,name='mylist'),
  path('approve/<int:equipment_id>/approve/',views.approve ,name='approve'),
  path('approve/<int:equipment_id>/return/',views.returngoods ,name='return'),
  path('<int:equipment_id>/', views.detail, name='detail'),
  path('<int:equipment_id>/act/', views.act, name='act'),
  ]
