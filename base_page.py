import webapp2
import os
import jinja2


class BaseHandler(webapp2.RequestHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_variables = {}

    @webapp2.cached_property
    def jinja2(self):
        fp = os.path.dirname(__file__) + '/templates'
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(fp),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True
        )

    def render(self, template, template_variables={}):
        template = self.jinja2.get_template(template)
        self.response.write(template.render(template_variables))
