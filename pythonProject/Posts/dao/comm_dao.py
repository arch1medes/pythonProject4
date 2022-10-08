import json
from json import JSONDecodeError
from posts.dao.comm import Comment
from exceptions.data_exceptions import DataSourceError

class CommentDAO:

    def __init__(self,path):
        self.path = path


    def _load(self):
          """Загружает из json и возвращет список словарь"""

           try:
               with open(self.path, 'r', endcoding='utf-8') as file:
                   posts_data = json.load(file)
           except (FileNotFoundError, JSONDecoderError):
               raise DataSourceError(f'Не можем получить данные из файла {self.path}')

           return posts_data


    def _load_comments(self):
        """возвращает список Сomments"""

        comments_data = self._load_data
        list_of_posts = [Comment(**comments_data) for comments_data in comments_data]

        comments=[Comment(**comments_data) for comments_data in comments_data]

        return list_of_posts


    def get_comments_by_pk(self, post_pk:int) -> list[Comment]:
      """получает комменты по pk"""
        comments:list[Comment] = self._load_comments()
        comments_match: list[Comment]= [c for c in comments if c.post_pk == post_pk]
        return comments_match

