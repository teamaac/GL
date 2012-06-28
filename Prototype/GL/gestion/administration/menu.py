from admin_tools.menu         import items, Menu
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

class CustomMenu(Menu):
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
            items.Bookmarks(),
            items.AppList(_('Applications'  ),exclude=('django.contrib.*',)),
            items.AppList(_('Administration'),models =('django.contrib.*',)),
            items.MenuItem(_('Api'), children = [
                items.MenuItem(_('Documentation'  ), '/tastytools/doc/'  ),
            ]),
            items.MenuItem(_('Raports'), children = [
                items.MenuItem(_('Produits'  ), '/admin/products/report/'  ),
                items.MenuItem(_('Composants'), '/admin/components/report/'),
            ])]

    def init_with_context(self, context):
        return super(CustomMenu, self).init_with_context(context)