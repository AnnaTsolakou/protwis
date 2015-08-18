from django.conf.urls import patterns, url

from similaritymatrix import views


urlpatterns = patterns('',
    url(r'^targetselection', views.TargetSelection.as_view(), name='targetselection'),
    url(r'^segmentselection', views.SegmentSelection.as_view(), name='segmentselection'),
    url(r'^render', views.render_matrix, name='render'),
    url(r'^csv', views.render_csv_matrix, name='csv'),
)