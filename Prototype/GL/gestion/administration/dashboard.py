from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from admin_tools.utils        import get_admin_site_name
from admin_tools.dashboard    import modules, Dashboard, AppIndexDashboard

class CustomIndexDashboard(Dashboard):
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout     = 'inline',
            draggable  = False   ,
            deletable  = False   ,
            collapsible= False   ,
            children=[
                [_('Log out'), reverse('%s:logout' % site_name)],
                [_('Change password'), reverse('%s:password_change' % site_name)],
        ]))

        self.children.append(modules.AppList(_('Applications'  ), exclude=('django.contrib.*',),))
        self.children.append(modules.AppList(_('Administration'), models =('django.contrib.*',),))
        self.children.append(modules.RecentActions(_('Recent Actions'), 10))

        self.children.append(modules.LinkList(
            _('Support'),
            children=[{
                    'title': _('Django documentation'),
                    'url': 'http://docs.djangoproject.com/',
                    'external': True,
                },{
                    'title': _('Django admin-tools doumentation'),
                    'url': 'http://django-admin-tools.readthedocs.org/en/latest/index.html',
                    'external': True,
                },{
                    'title': _('Extending Django Admin Interface'),
                    'url': 'http://www.djangobook.com/en/1.0/chapter17/',
                    'external': True,
                },{
                    'title': _('Test-Driven Django Tutorial'),
                    'url': 'http://www.tdd-django-tutorial.com/',
                    'external': True,
                },{
                    'title': _('Selenium documentation'),
                    'url': 'http://seleniumhq.org/docs/',
                    'external': True,
                },
            ]
        ))


class CustomAppIndexDashboard(AppIndexDashboard):
    title = ''
    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
        )]

    def init_with_context(self, context):
        return super(CustomAppIndexDashboard, self).init_with_context(context)
