from django.shortcuts import render

def home(request):
    """
    Render the homepage where users enter text and select utilities.
    """
    return render(request, 'index.html')


def analyze(request):
    """
    Analyze the text based on selected utilities:
    - Remove punctuation
    - Capitalize first letter
    - Remove new lines
    - Remove extra spaces
    - Count characters
    """
    # Get text from the form or use 'off' as default
    djtext = request.GET.get('text') or 'off'

    # Check which checkboxes were selected
    removepunc = request.GET.get('removepunc')
    capitalizefirst = request.GET.get('capitalizefirst')
    newlineremove = request.GET.get('newlineremove')
    spaceremove = request.GET.get('spaceremove')
    charcount = request.GET.get('charcount')

    analyzed = djtext

    # Remove punctuation
    if removepunc:
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`|'''
        analyzed = "".join(char for char in analyzed if char not in punctuations)

    # Capitalize first letter of the text
    if capitalizefirst:
        analyzed = analyzed.capitalize()

    # Remove new lines
    if newlineremove:
        analyzed = analyzed.replace("\n", "").replace("\r", "")

    # Remove extra spaces
    if spaceremove:
        analyzed = " ".join(analyzed.split())

    # Count characters
    purpose = []
    if removepunc:
        purpose.append("Removed Punctuations")
    if capitalizefirst:
        purpose.append("Capitalized First Letter")
    if newlineremove:
        purpose.append("Removed New Lines")
    if spaceremove:
        purpose.append("Removed Extra Spaces")
    if charcount:
        purpose.append(f"Character Count: {len(analyzed)}")

    if not purpose:
        purpose_text = "No changes applied"
    else:
        purpose_text = ", ".join(purpose)

    params = {'purpose': purpose_text, 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
