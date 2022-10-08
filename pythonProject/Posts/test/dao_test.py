import pytest

from posts.dao.post import PostDAO
from posts.dao.post import Post

def check_fields(post):
  fields = ["poster_name","poster_avatar","pic","content","views_count","likes_count","pk"]

  for field in fields:
      assert hasattr(post, field), f"Нет поля {field}"

class dao_test:

    @pytest.fixture
    def post_dao(self):
      post_dao_ex = PostDAO("./Posts/test/post_mock.json")
      return post_dao_ex

    def test_all(self,post_dao):

        posts=post_dao.get_all()
        assert type(posts) == list, "incorrect type"

        post=post_dao.get_all()[0]
        assert type(post) == Post, "incorrect type for single item"

    def get_all_fields(self, post_dao):

        posts = post_dao.get_all()
        post = post_dao.get_all()[0]
        check_fields(post)

    def get_all_correct_id(self, post_dao):

        posts = post_dao.get_all()

        correct_pks={1,2,3}
        pks = set([post.pk for post in posts])
        assert pks == correct_pks

    #Функция получения по pk

    def test_get_bu_pk_types(self, post_dao):
        post=post_dao.get_by_pk(1)
        assert type(post)== Post, "incorrect type for result single item"

    def test_get_bu_pk_fiels(self, post_dao):
        post=post_dao.get_by_pk(1)
        check_fields(post)

    def test_get_bu_pk_none(self, post_dao):
        post=post_dao.get_by_pk(999)
        assert post is None, "should be nobe for non existence pk"

    @pytest.mark.parametrize("pk", [1,2,3])
    def test_get_bu_pk_correcrt_id(self, post_dao, pk):
        post=post=post_dao.get_by_pk(pk)
        assert post.pk == pk, f"incorrect post.pk for requestion post with pk=={pk}"

    #Функция получения по поиску

    def test_search_in_content_types(self, post_dao):
        posts=post_dao.search_in_content("ага")
        assert type(posts) == list, "incorrect tyep for result"
        post = post_dao.get_all()[0]
        assert type(post) == Post,  "incorrect tyep for result for single item"

    def test_search_in_content_fields(self, post_dao):
        posts = post_dao.search_in_content("ага")
        post = post_dao.get_all()[0]
        check_fields(post)

    def test_search_in_content_not_found(self, post_dao):
        posts = post_dao.search_in_content("99909999")
        assert posts == [], "should be [] for not substring not found"

    @pytest.mark.parametrize("s","expected_pks",[
        ("Ага", {1}),
        ("Вышел", {2}),
        ("на", {1,2,3}),
    ])

    def test_search_in_content_results(self,post_dao,s, expected_pks):
        posts=post_dao.search_in_content(s)
        pks=set([post.pk for post in posts])
        assert pks == expected_pks, f"incorrect results serching for {s}"
