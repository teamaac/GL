# coding= utf-8
from chartit             import *
from gestion.models      import *
from annoying.decorators import *
from django.db.models    import Sum, Avg

def component_name(id):
	return ComposantVersion.objects.get(pk=id).__unicode__()

@render_to("admin/reports/component_report.html")
def component_report(request):
	data_source_1     = DataPool(series= [{'options': {'source': ComposantVersion.objects.all()}, 'terms': [ 'id', 'cout']}])
	component_chart_1 = Chart(
		datasource     = data_source_1, 
		series_options = [{'options':{'type': 'pie', 'stacking': False}, 'terms'  :{'id': ['cout']}}],
		chart_options  = {'title': {'text': 'Cout Composant % total composants'}},
			x_sortf_mapf_mts = (None, component_name, True))
	return {'component_list' : Composant.objects.all(), 'product_chart': [component_chart_1,]}

@render_to("admin/reports/product_report.html")
def product_chart_view(request):
	product_list = ProduitVersionComposantVersion.objects.all()

	product_data_1 = PivotDataPool(
		series= [{'options': {'source': product_list, 
			'categories' : ['produit_version__produit__titre',],
			'legend_by'  : 'produit_version__version__label'}, 'terms' : {'Cout' : Sum('composant_version__cout')}}])

	product_data_2 = PivotDataPool(
		series= [{'options': {'source': product_list, 
			'categories' : ['produit_version__produit__titre', 'produit_version__version__label'],
			'legend_by'  : 'produit_version__version__label'}, 'terms'  : {'Cout' : Sum('composant_version__cout')}}])

	product_chart_1 = PivotChart(
		datasource     = product_data_1,
		series_options = [{'options': {'type': 'column', 'stacking': True, 'xAxis': 0, 'yAxis': 0},'terms' : ['Cout']}],
		chart_options  = {'title'   : {'text': 'Coût par versions cumullées de produit'},
			'xAxis': { 'title': 'Version produit'}, 'yAxis': { 'title': 'Cout des composant'}})

	product_chart_2 = PivotChart(
		datasource     = product_data_2,
		series_options = [{'options': {'type': 'column', 'stacking': True, 'xAxis': 0, 'yAxis': 0},'terms' : ['Cout']}],
		chart_options  = {'title': { 'text':  'Coût par versions de produit'},
			'xAxis': { 'title': 'Version produit'}, 'yAxis': { 'title': 'Cout des composant'}})
	return {'product_list' : Produit.objects.all(), 'product_chart': [product_chart_1, product_chart_2]}