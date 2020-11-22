from django.contrib import admin
# Register your models here.
from .models import List, Category, Comment, User, Bid, Watchlist


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'email', )


admin.site.register(User, UserAdmin)


class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'current_bid', 'updated_on',
                    'category', 'created_on', 'status')

    def current_bid(self, obj):
        return obj.price.price
    # get_price.admn_order_field = "-price"
    # get_price.short_discription = "current price"
    list_filter = ("status", 'category')
    search_fields = ['title', 'author']
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(List, ListAdmin)


class BidAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'price',)
    list_filter = ('title',)


admin.site.register(Bid, BidAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('types', 'id',)


admin.site.register(Category, CategoryAdmin)


class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'id')


admin.site.register(Watchlist, WatchlistAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('auclist', 'name', 'created_on')


admin.site.register(Comment, CommentAdmin)
