from gestion.models      import *
from annoying.decorators import *

@render_to("admin/reports/product_report.html")
def product_report(request):
	return {'product_list' : Produit.objects.all()}

@render_to("admin/reports/component_report.html")
def component_report(request):
	return {'component_list' : Composant.objects.all()}
