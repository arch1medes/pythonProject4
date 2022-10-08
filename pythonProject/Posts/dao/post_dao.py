import json
from json import JSONDecoderError

from posts.dao.post import Post
from exceptions.exceptions import DataSourceError

class PostDAO:

    def __init__(self, path):
        self.path = path

    def _load(self):
          """Загружает из json и возвращет список словарь"""

          try:
              with open(self.path, 'r', endcoding='utf-8') as file:
                  posts_data = json.load(file)
          except (FileNotFoundError, JSONDecoderError):
              raise DataSourceError(f'Не можем получить данные из файла {self.path}')

              return data

    def _load_posts(self):
       """возвращет экзмепляры"""

       posts_data = self._load_data
       list_of_posts = [Post(**post_data) for post_data in data]
       return list_of_posts


    def get_all(self):
        """
        получает все посты
        :return:
        """
        posts = self._load_posts()
        return posts

    def get_by_pk(self, pk):
        """пост по pk"""

        if type(pk) != int:
         raise TypeError("pk должен быть int")

         posts = self._load_posts()
         for post in posts:
           if post.pk == pk:

         return post

    def search_in_content(self,substring):
      """ищет посты с substring"""

        substring= str(substring).lower()
        posts=self._load_posts()

        matching_posts=[post for post in posts if substring in post.content.lower()]

        return matching_posts

    def find_by_poster(self, user_name):
         """ищет по посту"""

         user_name = str(user_name).lower()
         posts = self._load_posts()

         matching_posts=[post for post in posts if post.poster_name.lower() == user_name]

         return matching_posts



