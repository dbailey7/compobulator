from django.conf.urls import url;
from compobulator_app import views;

app_name = 'compobulator_app';

urlpatterns = [
    url(r'^mp_archetype_list/$', views.ArchetypeListView.as_view(), name='urlan_list'),
    # url(r'^(?P<pk>[-\w]+)/$', views.ArchetypeDetailView.as_view(), name='urlan_detail'),
    url(r'^mp_archetype_form/', views.mp_archetype_form_view, name='url_arch_form'), # Need name for same reason in templates
    url(r'^(?P<pk>\d+)/$', views.ArchetypeDetailView.as_view(), name='url_arch_detail'),
    # url(r'^create/$', views.ArchetypeCreateView.as_view(), name='url_arch_create'),
    # url(r'^update/(?P<pk>\d+)/$', views.ArchetypeUpdateView.as_view(), name='url_arch_update'),
    # url(r'^delete/(?P<pk>\d+)/$', views.ArchetypeDeleteView.as_view(), name='url_arch_delete'),
    url(r'^mp_element_list/$', views.ElementListView.as_view(), name='urlen_list'),
    # url(r'^(?P<pk>[-\w]+)/$', views.ElementDetailView.as_view(), name='urlen_detail'),
    url(r'^mp_element_form/', views.mp_element_form_view, name='url_elem_form'), # Need name for same reason in templates
    url(r'^(?P<pk>\d+)/$', views.ElementDetailView.as_view(), name='url_elem_detail'),
    # url(r'^(?P<slug>[-\w]+)/$', views.ElementDetailView.as_view(), name='mp_element-detail'),
    # url(r'^create/$', views.ElementCreateView.as_view(), name='url_elem_create'),
    # url(r'^update/(?P<pk>\d+)/$', views.ElementUpdateView.as_view(), name='url_elem_update'),
    # url(r'^delete/(?P<pk>\d+)/$', views.ElmentDeleteView.as_view(), name='url_elem_delete'),

];
