import pytest

import main


class TestApi:

      posts_keys = {"poster_name","poster_avatar","pic","content","views_count","likes_count","pk"}

      @pytest.fixture
      def app_instance(self):
          app = main.app
          app.config["DATA_PATH_POSTS"] = os.path.join("Posts", "test, "post_mock")
          test_client = app.test_client()
          return test_client

      def test_posts_has_correct_status(self, app_instance):
          result = app_instance.get("/api/Posts", follow_redirect=True)
          assert result.status_code == 200


      def test_posts_has_correct_keys(self, app_instance):
          result = app_instance.get("/api/Posts", follow_redirect=True)
          list_of_posts = resutl.get_json()

          for post in list_of_posts:
              assert post.keys() == self.post_keys, "неправильные ключи у словаря"


      #один  пост

      def test_single_has_correct_status(self, app_instance):
          result = app_instance.get("/api/Posts/1", follow_redirect=True)
          assert result.status_code == 200

      def test_single_test_non_existent_shows_404(self, app_instance):
          result = app_instance.get("/api/Posts/0", follow_redirect=True)
          assert result.status_code == 404

      def test_single_test_has_correct_keys(self, app_instance):
          result = app_instance.get("/api/Posts/1", follow_redirect=True)
          post =  result.get_json()
          post_keys = set(post.keys())
          assert post_keys == self.post_keys

      @pytest.mark.parametrize("pk", [(1), (2), (3), (4)])
      def test_single_test_has_correct_data(self, app_instance):
          result = app_instance.get(f"/api/Posts/{pk}", follow_redirect=True)
          post = result.get_json()
          assert post["pk"] == pk, f"Неправильный pk при запросе поста {pk}"