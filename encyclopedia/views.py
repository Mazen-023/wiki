from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import random
import html2text
from markdown2 import Markdown

from . import util

# Convert makrdown to HTML
markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })


#  Display the contents of that encyclopedia entry
def entry(request, title):

    # Render 404 error if the requested entry does not exist
    if util.get_entry(title) == None:
        return render(request, "encyclopedia/error.html", {
            "message": "The entry's page you requested is not available. Please try a valid one."
        })
    else:
        # Get entry content using util function
        content = util.get_entry(title)
        
        # Render the content entry if it does exist
        return render(request, "encyclopedia/page.html", {
            "title": title,
            "content": markdowner.convert(content)
        })
    
    
# Search feature
def search(request):
    # store the input value
    query = request.GET.get("q")

    # Check if the query is empty
    if not query:
        return HttpResponseRedirect(reverse("wiki:index"))
    
    # Go to search result
    if util.get_entry(query) == None:
        list = []
        # Check the title substring
        for entry in util.list_entries():
            if query.lower() in entry.lower():
                list.append(entry)

        return render(request, "encyclopedia/search.html",{
            "list": list
        })

    # Query match, Redirect to the entry's page
    return HttpResponseRedirect(reverse("wiki:entry", args=[query]))
        
    
# Create New Page
def new(request):
    if request.method == "POST":

        # store form values
        title = request.POST.get("title")
        content = request.POST.get("content")

        # Check if fields are empty
        if not title or not content:
            return HttpResponseRedirect(reverse('wiki:new'))
        
        # Show error message if the entry aleady exist
        if util.get_entry(title) != None:
            return render(request, "encyclopedia/error.html", {
                "message": "This entry is already exist"
            })
        
        # Save the entry to disk
        util.save_entry(title, content)

        # Take the user to the new page
        return HttpResponseRedirect(reverse("wiki:entry", args=[title]))

    return render(request, 'encyclopedia/new.html')


# Pass Through the entry information to the edit page
def edit(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    
    return render(request, "encyclopedia/edit.html", {
        # Convert HTML to Markdown
        "content": html2text.html2text(content),
        "title": title
    })


# update Page
def update(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        # Save the changes
        util.save_entry(title, content)

        # Redirected to entry's page
        return HttpResponseRedirect(reverse("wiki:entry", args=[title]))

    return render(request, "encyclopedia/edit.html", {
        "content": content
    })


# Select random entry
def randomSelect(request):
    entries = util.list_entries()
    
    # Number of elements to randomly select
    k = 1

    # Select k random elements from the list
    title = random.sample(entries, k)[0]

    return HttpResponseRedirect(reverse("wiki:entry", args=[title]))