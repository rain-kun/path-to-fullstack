from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django import forms
from django.forms import ValidationError

from .models import User, Category, List, STATUS, Bid, Watchlist, Comment

#    ###### form classes ######


class GetBid(forms.Form):
    bid = forms.DecimalField(max_digits=10, decimal_places=2)


class NewComment(forms.Form):
    comment = forms.CharField(label="discription", widget=forms.Textarea(
        attrs={"rows": 6, "cols": 28}), required=False)


class CreateList(forms.Form):
    """docstring for CreateList."""

    # def __init__(self, arg):
    #     super(CreateList, self).__init__()
    #     self.arg = arg

    title = forms.CharField(max_length=200)
    img_url = forms.CharField(max_length=500, required=False)
    bid = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    discription = forms.CharField(label="discription", widget=forms.Textarea(
        attrs={"rows": 6, "cols": 20}), required=False)
    status = forms.ChoiceField(
        choices=STATUS, label="", initial='0', widget=forms.Select(), required=True)


def index(request):
    return render(request, "auctions/index.html", {
        "lists": List.objects.filter(status=1),
    })

#    ###### session handeling ######


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

#    ###### create list ######
@login_required
def newlist(request):
    if request.method == "POST":
        title = request.POST["title"]
        discription = request.POST["discription"]
        bid = request.POST["bid"]
        img_url = request.POST["img_url"]
        category = request.POST['category_listing']
        status = request.POST["status"]
        try:
            c = Category.objects.get(types=category)
            b = Bid(title=title, price=bid, author=request.user.username)
            b.save()
            li = List.objects.create(title=title, author=request.user, price=b,
                                     url=img_url, discription=discription, category=c, status=status)
            li.save()
        except ValidationError as e:
            return render(request, "auctions/newlist.html", {
                "forms": CreateList(),
                "tag": category.objects.all(),
                "errors": e.message_dict
            })

        # b.save()

        return HttpResponseRedirect(reverse("index"))
    return render(request, "auctions/newlist.html", {
        "form": CreateList(),
        "tags": Category.objects.all(),

    })

#    ###### show categories ######


def categories(request, name):
    if int(name) > 0:
        return render(request, "auctions/categories.html", {
            "lists": List.objects.filter(status=1, category_id=name),
        })

    return render(request, "auctions/categories.html", {
        "tags": Category.objects.all(),

    })

#    ###### watchlist ######
@login_required
def watchlist(request):
    try:
        w = Watchlist.objects.filter(user=request.user)
    except IntegrityError as e:
        print(e)
        return render(request, "auctions/watchlist.html", {
            "watchlist": w,
            "error": e,
        })
    return render(request, "auctions/watchlist.html", {
        "watchlist": w,
    })


@login_required
def viewfromwatchlist(request, title):
    try:
        list = List.objects.get(title=title)
        id = list.id
    except IntegrityError as e:
        print(e)
    return HttpResponseRedirect(reverse("details", args=[id]))


@login_required
def watchlist_handle(request, id):

    if request.method == "POST":
        # title = request.POST.get('title', False)
        try:
            if not Watchlist.objects.filter(user=request.user, item=id):
                it = List.objects.get(id=id)
                print(it.title)
                wa = Watchlist.objects.create(
                    user=request.user, title=it.title)
                wa.item.add(it)
                print("added to watchlist")
            elif Watchlist.objects.filter(user=request.user, item=id):
                it = List.objects.get(id=id)
                wa = Watchlist.objects.filter(user=request.user, item=it)
                wa.delete()
                print("deleted from watchlist")
        except IntegrityError as e:
            print("watchlist_handle fail")
            print(e)
            return HttpResponseRedirect(reverse("details", args=[id]), {
            })
        return HttpResponseRedirect(reverse("details", args=[id]))

# done in watchlist_handle together
# @login_required
# def watchlist_remove(request, id):
#
#     if request.method == "POST":
#         try:
#             if Watchlist.objects.filter(user=request.user).filter(item=id):
#                 it = List.objects.get(id=id)
#                 wa = Watchlist.objects.filter(user=request.user, item=it)
#                 wa.delete()
#                 print("deleted from watchlist")
#         except IntegrityError:
#             print("watchlist fail")
#             return HttpResponseRedirect(reverse("details", args=[id]), {
#             })
#         return HttpResponseRedirect(reverse("details", args=[id]))
#     return HttpResponseRedirect(reverse("details", args=[id]))

#    ###### details ######


def viewdetail(request, id):
    ll = List.objects.get(id=id)
    us = str(ll.author)
    if request.method == "POST":
        bid = request.POST["bid"]
        try:
            a = str(ll.price.price)
            if float(bid) > float(a):
                b = Bid(title=ll.title, price=bid,
                        author=request.user.username)
                b.save()
                ll.price = b
                ll.save()
            else:
                return render(request, "auctions/productdetails.html", {
                    "form": CreateList(),
                    "list": List.objects.get(id=id),
                    "currentuser": request.user.username == us,
                    "comments": Comment.objects.filter(auclist=id),
                    "error": "*Bid have to be bigger then the current bid.*",
                    "total_bids": Bid.objects.filter(title=ll.title).count(),
                })

        except ValidationError as e:
            return render(request, "auctions/productdetails.html", {
                "forms": GetBid(),
                "list": List.objects.get(id=id),
                "currentuser": request.user.username == us,
                "comments": Comment.objects.filter(auclist=id),
                "total_bids": Bid.objects.filter(title=ll.title).count(),
                "watchlist": True if Watchlist.objects.filter(user=request.user, item=id) else False,
                "errors": e.message_dict,
            })

        return HttpResponseRedirect(reverse("details", args=[id]))
    if not request.user.is_authenticated:
        return render(request, "auctions/productdetails.html", {
            "form": CreateList(),
            "list": List.objects.get(id=id),
            # "currentuser": request.user.username == us,
            "comments": Comment.objects.filter(auclist=id),
            "total_bids": Bid.objects.filter(title=ll.title).count(),
            # "watchlist": True if Watchlist.objects.filter(user=request.user, item=id) else False,
        })
    else:
        return render(request, "auctions/productdetails.html", {
            "form": CreateList(),
            "list": List.objects.get(id=id),
            "currentuser": request.user.username == us,
            "comments": Comment.objects.filter(auclist=id),
            "total_bids": Bid.objects.filter(title=ll.title).count(),
            "watchlist": True if Watchlist.objects.filter(user=request.user, item=id) else False,
        })


# ###### save the status ######
@login_required
def savestatus(request, id):
    if request.method == "POST":
        status = request.POST["status"]
        try:
            li = List.objects.get(id=id)
            li.status = status
            li.save()
        except IntegrityError as e:
            return render(request, "auctions/productdetails.html", {
                "forms": GetBid(),
                "list": List.objects.get(id=id),
                "errors": e.message_dict
            })
        return HttpResponseRedirect(reverse_lazy("details", args=[id]))

    # return "<h4>No access fia get gateway.</h4>"


@login_required
def comments(request, id):
    if request.method == "POST":
        user = request.user.username
        comment = request.POST["discription"]
        try:
            au = List.objects.get(id=id)
            c = Comment.objects.create(auclist=au, name=user, body=comment)
            c.save()
            print("comment save")
        except IntegrityError as e:
            print(e)
            return HttpResponseRedirect(reverse("details", args=[id]))

        return HttpResponseRedirect(reverse("details", args=[id]))
