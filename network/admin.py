from django.contrib import admin
from .models import User, Post, Follow, Like
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'id', 'email', )


admin.site.register(User, UserAdmin)


class UserPost(admin.ModelAdmin):
    list_display = ('title', 'user', 'likes', 'created_on', 'updated_at')

    def likes(self):
        return self.get_total_likes()  # .get_total_likes()
    empty_value_display = '-0-'


admin.site.register(Post, UserPost)


class UserLike(admin.ModelAdmin):
    list_display = ('post', 'likes', 'created_at', 'updated_at')

    def likes(self, obj):
        return obj.post.get_total_likes()

    empty_value_display = '-0-'


admin.site.register(Like, UserLike)


class UserFollows(admin.ModelAdmin):
    list_display = ('following', 'follower',)
    list_filter = ('following',)


admin.site.register(Follow, UserFollows)
