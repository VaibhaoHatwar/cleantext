from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', '')
    analyzed = djtext
    params = {'purpose': 'Analyzed Text', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
