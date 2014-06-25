from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jalocsBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'post.views.showGeneralResume', name='home'),
    url(r'^(?P<category>\w+)/$', 'post.views.getCategoryResume', name='category_resume'),
    url(r'^(?P<category>\w+)/(?P<post_id>\d+)', 'post.views.getPostContent', name='post_content'),
    url(r'^hello/', TemplateView.as_view(template_name='main.html')),

    url(r'^admin/', include(admin.site.urls)),
)
