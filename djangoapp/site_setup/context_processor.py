# This model creates a new dictionary with the site_setup context globally available to all templates.
from site_setup.models import SiteSetup


# THIS MAKES A DB QUERY EVERY TIME A PAGE IS LOADED, SO BE SURE IF YOU REALLY NEED IT
def site_setup(request):
    setup = SiteSetup.objects.order_by("-id").first()

    return {
        "site_setup": setup,
    }
