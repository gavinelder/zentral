from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^groups/$', views.GroupsView.as_view(), name='groups'),
    url(r'^groups/(?P<group_id>\d+)/machines/$', views.GroupMachinesView.as_view(), name='group_machines'),
    url(r'^business_units/$', views.MBUView.as_view(), name='mbu'),
    url(r'^business_units/review_merge/$', views.ReviewMBUMergeView.as_view(), name='review_mbu_merge'),
    url(r'^business_units/merge/$', views.MergeMBUView.as_view(), name='merge_mbu'),
    url(r'^business_units/create/$', views.CreateMBUView.as_view(), name='create_mbu'),
    url(r'^business_units/(?P<pk>\d+)/update/$', views.UpdateMBUView.as_view(), name='update_mbu'),
    url(r'^business_units/(?P<pk>\d+)/machines/$', views.MBUMachinesView.as_view(), name='mbu_machines'),
    url(r'^business_units/(?P<pk>\d+)/api_enrollment/$',
        views.MBUAPIEnrollmentView.as_view(),
        name='mbu_api_enrollment'),
    url(r'^machine/(?P<serial_number>\S+)/events/$', views.MachineEventsView.as_view(), name='machine_events'),
    url(r'^machine/(?P<serial_number>\S+)/$', views.MachineView.as_view(), name='machine'),
    url(r'^probes/$', views.ProbesView.as_view(), name='probes'),
    url(r'^probes/(?P<probe_key>[\S ]+)/$', views.ProbeView.as_view(), name='probe'),
]


main_menu_cfg = {
    'items': (
        ('index', 'Machines'),
        ('groups', 'Groups'),
        ('mbu', 'Business units'),
        ('probes', 'Probes'),
    )
}
