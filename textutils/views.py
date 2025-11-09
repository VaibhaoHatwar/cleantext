from django.shortcuts import render
import string

# --- Utility functions ---
def remove_punctuation(text):
    """Remove all punctuation characters from the text."""
    return "".join(char for char in text if char not in string.punctuation)

def remove_newlines(text):
    """Remove all newline and carriage return characters."""
    return text.replace("\n", "").replace("\r", "")

def remove_extra_spaces(text):
    """Replace multiple spaces with a single space."""
    return " ".join(text.split())

# --- Main analyze view ---
def analyze(request):
    """
    Analyze text based on selected utilities:
    - Remove punctuation
    - Uppercase all
    - Lowercase all
    - Capitalize first letter
    - Remove new lines
    - Remove extra spaces
    - Count characters
    """
    djtext = request.GET.get('text', '')  # Get text from form

    # Get checkbox values
    removepunc = request.GET.get('removepunc')
    capitalizeall = request.GET.get('capitalizeall')
    lowercaseall = request.GET.get('lowercaseall')
    capitalizefirst = request.GET.get('capitalizefirst')
    newlineremove = request.GET.get('newlineremove')
    spaceremove = request.GET.get('spaceremove')
    charcount = request.GET.get('charcount')

    analyzed = djtext
    purpose_list = []

    # --- Text transformations ---
    if removepunc:
        analyzed = remove_punctuation(analyzed)
        purpose_list.append("Removed Punctuations")

    if newlineremove:
        analyzed = remove_newlines(analyzed)
        purpose_list.append("Removed New Lines")

    if spaceremove:
        analyzed = remove_extra_spaces(analyzed)
        purpose_list.append("Removed Extra Spaces")

    # --- Case transformations ---
    if capitalizeall and lowercaseall:
        analyzed = analyzed.upper()
        purpose_list.append("Capitalized All Letters (Lowercase ignored)")
    elif capitalizeall:
        analyzed = analyzed.upper()
        purpose_list.append("Capitalized All Letters")
    elif lowercaseall:
        analyzed = analyzed.lower()
        purpose_list.append("Lowercase All Letters")

    if capitalizefirst and not capitalizeall:
        analyzed = analyzed.capitalize()
        purpose_list.append("Capitalized First Letter")

    # --- Character count ---
    if charcount:
        purpose_list.append(f"Character Count: {len(analyzed)}")

    # Purpose summary
    purpose_text = ", ".join(purpose_list) if purpose_list else "No changes applied"

    return render(request, 'analyze.html', {
        'purpose': purpose_text,
        'analyzed_text': analyzed
    })

# --- Other views ---
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
