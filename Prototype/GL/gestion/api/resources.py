import sys
import inspect
import gestion.models
import tastypie.resources
import tastypie.authorization
import tastypie.authentication

for model in inspect.getmembers(gestion.models, lambda c: inspect.isclass(c) and not c._meta.abstract):
	class X(tastypie.resources.ModelResource):
		def determine_format(self, request): 
			return "application/json" 
		class Meta:
			queryset       = model[1].objects.all()
			resource_name  = model[1].__name__
			authorization  = tastypie.authorization.DjangoAuthorization()
			authentication = tastypie.authentication.BasicAuthentication()
	X.__name__ = model[1].__name__+"Resource"
	setattr(sys.modules[globals()['__name__']], X.__name__, X)
	X = None