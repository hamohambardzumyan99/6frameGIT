# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class StaffApp(CMSApp):
    name = _('Staff')
    urls = ['blog.urls', ]
    app_name = 'staff'


apphook_pool.register(StaffApp)
