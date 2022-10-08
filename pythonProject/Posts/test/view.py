from flask import Blueprint, render_template
from werkzeug.exceptions import abort


from posts.dao.comm import Comment
from posts.dao.post import Post
from posts.dao.comm.dao import CommentDAO
from posts.dao.post.dao import PostDAO

from config import DATA_PATH_POSTS,DATA_PATH_COMMENTS

#создаем блупринт
bp_posts = Blueprint("Posts", __name__,template_folder="templats")

#создаем обьекты доступа к данным
post.dao = PostDAO(DATA_PATH_POSTS)
comm.dao = CommantDaoDAO(DATA_PATH_COMMENTS)




@bp_posts.route("/")
def page_posts_index():
    """страничка всех постов"""
    all_posts = post.dao.get_all()
    return render_template("posts_index.html", posts=all_posts)

@bp_posts.route("/Posts/<int:pk>/")
def page_posts_single(pk):
    """страничка одного поста"""
    post: Post | None = post.dao.get_by_pk()
    comments: list[Comment] = comm.dao.get_comments_by_post_pk(pk)

    if post is None:
        abort(404)

    return render_template("posts_post.html", posts=post, comments=comments, comments_length = len(comments))
"""возвращает посты пользователя"""
@bp_posts.route("/users/<user_name>")
def page_posts_by_user(user_name: int):
    posts: list[Comment] = post.dao.get_by_poster(user_name)
    return render_template("posts_search.html", posts=posts, user_name=user_name)


@bp_posts.route("/search/")
def page_posts_search():

    s: str = request.args.get("s","")
       if s == "":
           posts=[]
       else:
           posts:list[Post] = post.dao.search_in_content(s)


    posts = post.dao.get_by_poster(user_name)
    return render_template("posts_user-feed.html", posts=posts, s=s, posts_length=len(posts))