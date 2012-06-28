{% block slide %}
<div id="{% block slide_id %}{% endblock %}" class="slide">
	<div class="container">
		<div class="one_half">
			<img src="{{ MEDIA_URL }}images/{% block slide_image %}{% endblock %}" width="440" height="400"/>
		</div>
		<div class="one_half last_column"><br /><br /><br /><br /><br />
			<p class="slide-title-normal">{% block slide_title %}{% endblock %}</p><br/>
			<p class="slide-subtitle-big">{% block slide_text  %}{% endblock %}</p><br/>
		</div>
	</div>
</div>
{% endblock %}