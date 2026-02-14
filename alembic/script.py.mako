{% extends "migration.tmpl" %}

{% block autogenerate_content %}
    {% if conn.has_changes() %}
        context['task'].add_command("regenerate")
    {% endif %}
{% endblock %}

{% block upgrade %}
    pass
{% endblock %}

{% block downgrade %}
    pass
{% endblock %}