__author__ = 'uiandwe'
from django.conf import settings
from django.db import connection
from django.template import Template, Context



class SimpleMiddleware(object):
    def __init__(self):
        pass
        # One-time configuration and initialization.

    def process_request(self, request):
        return

    def process_view(self, request, view_func, view_args, view_kwargs):

        print(request, view_args, view_func, view_kwargs)

        respose = None
        return respose


    def process_template_response(self, request, response):
        print(request, response)
        return response


    def process_response(self, request, response):

        if settings.DEBUG and connection.queries:
            execution_sql_time = sum([float(q['time']) for q in connection.queries])
            t = Template(
            """
            {{nb_sql}} requet{{nb_sql|pluralize:"e,es"}} en {{execution_sql_time}} second{{execution_sql_time|pluralize:"e,es"}}:
            {% for sql in sql_log %}
            [{{forloop.counter}}] {{sql.time}}s: {{sql.sql|safe}}
            {% endfor %}
            """)
            print("---------------")
            print(t.render(Context({'sql_log':connection.queries,'nb_sql':len(connection.queries),'execution_sql_time':execution_sql_time})))
            print("---------------")
        print(request, response)
        return response