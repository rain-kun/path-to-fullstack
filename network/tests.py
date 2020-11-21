from django.test import Client, TestCase
from django.db.models import Max
from .models import User, Post, Like, Follow
# Create your tests here.


class PostTestCase(TestCase):

    def setUp(self):
        # create users
        u1 = User.objects.create(
            username="U1", email="U1@mail.com", password="u1password")
        u2 = User.objects.create(
            username="U2", email="U2@mail.com", password="u2password")
        u3 = User.objects.create(
            username="U 3", email="U3@mail.com", password="u3password")

        # create posts
        p1 = Post.objects.create(title="T1", user=u1, text="aaaa")
        p2 = Post.objects.create(title="T2", user=u2, text="bbbb")
        p3 = Post.objects.create(title="T3", user=u3, text="cccc")
        p4 = Post.objects.create(title="T4", user=u2, text="")

        # create likes
        # p1l = Like.objects.create(post=p1, user=user.set().add(u1, u2))
        # p2l = Like.objects.create(post=p2, user={u3, u2})
        # p3l = Like.objects.create(post=p3, user={u1, u2, u3})

        # create Follows
        u1f1 = Follow.objects.create(following=u1, follower=u2)
        u1f2 = Follow.objects.create(following=u1, follower=u3)
        u2f1 = Follow.objects.create(following=u2, follower=u1)

    def test_post_count(self):
        u = User.objects.get(username="U2")
        self.assertEqual(u.postby.count(), 2)

    # def test_post_like_count(self):
    #     p = Post.objects.get(title="T3")
    #     self.assertEqual(p.get_total_likes(), 2)

    def test_user_following_count(self):
        u = User.objects.get(username="U1")
        self.assertEqual(u.following.count(), 2)

    def test_user_follower_count(self):
        u = User.objects.get(username="U1")
        self.assertEqual(u.follower.count(), 1)

    def test_valid_post(self):
        # u = User.objects.get(username="U1")
        p = Post.objects.get(title="T1")
        self.assertTrue(p.is_valid_post())

    def test_invalid_post(self):
        # u = User.objects.get(username="U2")
        p = Post.objects.get(title="T4")
        self.assertFalse(p.is_valid_post())

    def test_index(self):
        c = Client()
        response = c.get("")
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.context["page_obj"], "Page 1 of 1")

    def test_user_page(self):
        u = User.objects.get(username="U2")

        c = Client()
        response = c.get(f"/user/{u.username}")
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.context["u.email"], u.email)

    # def test_invalid_user_page(self):
        # u = User.objects.get(id=5)
        # max_uname = User.objects.all().aggregate(Max("id"))["username"]

        # c = Client()
        # response = c.get(f"/user/U-1")
        # self.assertEqual(response.status_code, 404)

    # def test_like_count(self):
    #     c = Client()
    #     response = c.get("")
    #     self.assertEqual(response.context["page_obj"](1))
