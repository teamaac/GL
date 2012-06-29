import tastypie
import settings
import tastypie.api
import tastypie.resources
import {{ models_module }}

{% for resource in resources_map -%}
class {{ resource.resource_class }}(tastypie.resources.ModelResource):
    {% for field in resource.fk_model_fields -%}
    {{ field.field }} = tastypie.fields.ForeignKey('{{ api_module }}.resources.{{ field.mapped_resource }}', '{{ field.field }}', full={{ resource.full_reverse }})
    {% endfor -%}
    {% for field in resource.mm_model_fields -%}
    {{ field.field }} = tastypie.fields.ToManyField('{{ api_module }}.resources.{{ field.mapped_resource }}', '{{ field.field }}', full={{ resource.full_reverse }})
    {% endfor -%}
    def determine_format(self, request):
        return "application/json"
    class Meta:
        queryset      = {{ models_module }}.{{ resource.model_name }}.objects.all()
        resource_name = '{{ resource.resource_name }}'

{% endfor -%}

resources_api = tastypie.api.Api(api_name=settings.API_NAME)
{% for resource in resources_map -%}
resources_api.register({{ resource.resource_class }}())
{% endfor -%}