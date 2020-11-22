from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
import markdown2

from . import util


class SearchResult(forms.Form):
    """docstring for SearchResult."""

    search = forms.CharField(label="Search Item",
                             widget=forms.TextInput(attrs={'style': 'max-width:190px'})
                             )


class CreateNewEntry(forms.Form):
    """docstring for CreateNewEntry."""
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={'rows': 4, 'cols': 20}))


def index(request):
    form = SearchResult(request.GET)
    if form.is_valid():
        title = form.cleaned_data["search"]
        title = title.replace(" ", "_")
        if util.get_entry(title):
            return render(request, "encyclopedia/entrys.html", {
                "title": title,
                "head": "All Pages",
                "pagename": title,
                "entry":  markdown2.markdown(util.get_entry(title)),
                "form": SearchResult()
            })
        else:
            entries = [i for i in util.list_entries() if title in i]
            return render(request, "encyclopedia/index.html", {
                "title": "Related Encyclopedia",
                "head": "Related Pages",
                "entries": entries,
                "form": SearchResult()
            })
    return render(request, "encyclopedia/index.html", {
        "title": "Encyclopedia",
        "head": "All Pages",
        "entries": util.list_entries(),
        "form": SearchResult()
    })


def pages(request, pagename):
    if util.get_entry(pagename):
        title = pagename.replace("_", " ")
        return render(request, "encyclopedia/entrys.html", {
            "title": title,
            "pagename": pagename,
            "entry":  markdown2.markdown(util.get_entry(pagename)),
            "form": SearchResult(),
        })
    else:
        return render(request, "encyclopedia/entrys.html", {
            "form": SearchResult(),
        })


def newpage(request):
    if request.method == "POST":
        form = CreateNewEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            title = title.replace(" ", "_")
            if util.get_entry(title):
                return render(request, "encyclopedia/new_page.html", {
                    "form": SearchResult(),
                    "newentryform": CreateNewEntry(),
                    "error": "page already exists, try a different Title name."
                })
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("pages", kwargs={"pagename": title}))
    return render(request, "encyclopedia/new_page.html", {
        "form": SearchResult(),
        "newentryform": CreateNewEntry(),
    })


def rand_entry(request):
    list = util.list_entries()
    rand = random.randrange(0, len(list))
    title = list[rand]
    pagename = title.replace(" ", "_")
    return render(request, "encyclopedia/entrys.html", {
        "title": title.replace("_", " "),
        "pagename": pagename,
        "entry":  markdown2.markdown(util.get_entry(title)),
        "form": SearchResult(),
    })


def edit_entry(request, name):
    if request.method == "POST":
        form = CreateNewEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            title = title.replace(" ", "_")
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("pages", kwargs={"pagename": title}))

    content = util.get_entry(name)
    data = {'title': name,
            'content': content}
    return render(request, "encyclopedia/edit_entry.html", {
        "title": name,
        "pagename": name.replace(" ", "_"),
        "form": SearchResult(),
        "newentryform": CreateNewEntry(data),
    })
