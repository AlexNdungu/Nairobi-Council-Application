from io import BytesIO
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse


from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


""" def check_email_exists(request, backend, details, uid, user=None, *args, **kwargs):
    email = details.get('email', '')
    provider = backend.name

    # check if social user exists to allow logging in (not sure if this is necessary)
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    # check if given email is in use
    count = User.objects.filter(username=email).count()

    success_message = messages.success(request, 'Sorry User With That Email Already Exists')

    # user is not logged in, social profile with given uid doesn't exist
    # and email is in use
    if not user and not social and count:
        return HttpResponseRedirect(reverse('App1:register', success_message))     """