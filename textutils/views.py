from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to 🧹CleanText</h1><p>This is the home page.</p><a href='about'>About Page</a>")

def about(request):
    return HttpResponse("<h2>About 🧹CleanText</h2><p>This app helps clean your text easily!</p><a href='/'>Back to Home Page</a>")
