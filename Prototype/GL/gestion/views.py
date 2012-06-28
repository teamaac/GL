from annoying.decorators import render_to

@render_to("site/index.html")
def index(request):
    return {}