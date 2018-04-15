#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
 * @author: Lightwing Ng
 * email: rodney_ng@iCloud.com
 * created on Apr 15, 2018, 11:10 PM
 * Software: PyCharm
 * Project Name: Tutorial
管理应用app中的所有URL映射
"""

from django.conf.urls import url
from app.admin import admin_site

from . import views

urlpatterns = {
    url(r'moments_input', views.moments_input),  # 视图函数的路由映射
    url(r'', views.welcome),
    url(r'^myadmin/', admin_site.urls),
}
