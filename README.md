# Jungle Devs - Django Reddit Challenge

## Description
**Challenge goal**: The idea of the challenge is to implement a very simplified version of [Reddit](https://www.reddit.com),
meaning you will have *Users*, *Topics*, *Posts* and *Comments*. with this you're expected to test your knowledge on
the basic concepts involved in a Django backend application, and to also learn even more.
Always!

**Target level**: This is an entry level course, no prior knowledge of programming is needed.

**Final accomplishment**: By the end of this challenge, you’ll be able to understand the basics of Django and how to create your own RESTful API with basic CRUD functionalities.

## Acceptance criteria
- Separate your project into 4 Django apps, one for each entity:
  - User
  - Topic
  - Post
  - Comment
- Have all the required fields for each entity as described on this README
- Use the URL structure described on this README with Nested URL Routers

## Prerequisites

- [Python 3.7](https://www.python.org)
- [Docker](https://www.docker.com)
- [Docker Compose](https://docs.docker.com/compose/)
- [Virtualenv](https://github.com/pypa/virtualenv/)
- [Git](https://git-scm.com/)

## Instructions to Run

- Create the virtual environment and activate it

        virtualenv -p python3 venv
        source venv/bin/activate
- Install the requirements `pip install -r requirements.txt`
- Start the dockers `docker-compose up` with the database and the localstack
- Run the server with `python manage.py runserver 8000`

You need a `.env`file with your environment variables, here's an example file:
```
LOAD_ENVS_FROM_FILE='True'
ENVIRONMENT='development'
SECRET_KEY='#*=backend-challenge=*#'
DEFAULT_FROM_EMAIL='Challenge <challenge@jungledevs.com>'
DATABASE_URL='postgres://postgres:postgres@localhost:5432/backend-challenge-001'
SENTRY_DSN='sentry_key'
AWS_STORAGE_BUCKET_NAME='django-be'
```

## Additional Information
Here are some useful stuff to keep in mind while completing this challenge:

* Try to keep your code [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), so the creation of
[abstract helper](https://realpython.com/modeling-polymorphism-django-python/#abstract-base-model) [models](https://docs.djangoproject.com/en/3.0/topics/db/models/#abstract-base-classes) is more than welcome
to avoid repetition of fields in your models
* Remember that only the author of a topic, post or comment should be able to modify or delete it!
If you have any doubts, check the
[Authentication and Permissions part](https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/)
on the Django REST tutorial
* For better structuring and visualization, you may use
[Nested Serializers](https://www.django-rest-framework.org/api-guide/relations/#nested-relationships) to customize your
responses beyond the primary keys

### Entities

As mentioned in the description, this challenge will have four entities (each one should be a separate app).
Here are brief descriptions of what they are and what are the expected properties of each (keep in mind that you can
improve them as you wish!):

* *User*: can be used plain from what is offered by Django;
* *Topic*: the equivalent of a sub-reddit. The suggest fields are:
    * Name
    * Title
    * Author
    * Description
    * URLName - the name we want to use to reach it through the browser (check [SlugField](https://docs.djangoproject.com/en/2.1/ref/models/fields/#slugfield))
    * Created_at
    * Updated_at
* *Post*: the equivalent of a *Reddit thread*, a *post* belongs to a *specific topic* and is *created by an user*. The
suggested fields are:
    * Title
    * Content
    * Created_at
    * Updated_at
    * Topic
* *Comment*: the equivalent of a comment, a comment belongs to a *specific post* (which belongs to a *specific topic*)
and is *created by an user*. The suggested fields are:
    * Title
    * Content
    * Created_at
    * Updated_at
    * Post

### URLs

We want to have a behavior similar to *Reddit (not necessarily equal)*, so ideally we'd like a structure like this:

* */topics/* - lists all available topics
* */topics/{urlname}/* - details (as well as some posts) from a specific topic (identified by *urlname*)
* */topics/{urlname}/posts/* - lists all posts from a specific topic
* */topics/{urlname}/posts/{post_id}/* - lists details and some comments from a post
* */topics/{urlname}/posts/{post_id}/comments/* - lists all comments from a post
* */topics/{urlname}/posts/{post_id}/comments/{comment_id}/* - lists details from a comment


If you have any doubts on how to implement these structures, check the
[Nested Routers documentation](https://github.com/alanjds/drf-nested-routers) and the
[lookup field section on the Routers documentation](https://www.django-rest-framework.org/api-guide/routers/#simplerouter).

### Request Examples
#### Topic
- [POST] /topics/
    ```json
    {
        "name": "topic-name",
        "title": "topic-title",
        "description": "topic-description"
    }
    ```
    - The topic author is passed from token setted in `Authorization` header.
- [PUT] /topics/url_name/
    - url_name is a slug based on name field
    - only the author has permission to update
    ```json
    {
        "name": "updated-topic-name",
        "title": "updated-topic-title",
        "description": "updated-topic-description"
    }
    ```
- [PATCH] /topics/url_name/
    - url_name is a slug based on name field
    - only the author has permission to update
    - All fields are optional
    - Ex.:
    ```json
    {
        "title": "single-update-topic-title",
    }
    ```
- [GET] /topics/
    - List all topics
- [GET] /topics/url_name/
    - Retrieve a single topic
- [DELETE] /topics/url_name/

#### Post
- [POST] /topics/url_name/posts/
    - url_name is a slug of topic
    ```json
    {
        "title": "post-title",
        "content": "post-content"
    }
    ```
    - The topic author is passed from token setted in `Authorization` header.
- [PUT] /topics/url_name/posts/pk/
    - url_name is a slug of topic
    - only the author has permission to update
    ```json
    {
        "title": "updated-post-title",
        "content": "updated-post-content"
    }
    ```
- [PATCH] /topics/url_name/posts/pk/
    - url_name is a slug of topic
    - All fields are optional
    - only the author has permission to update
    - Ex.:
    ```json
    {
        "title": "single-update-post-title",
    }
    ```
- [GET] /topics/url_name/posts/
    - List all posts of topic passed
- [GET] /topics/url_name/posts/pk/
    - Retrieve the post passed of topic passed
- [DELETE] /topics/url_name/posts/pk/

#### Comment
- [POST] /topics/url_name/posts/post_pk/comments/
    - url_name is a slug of topic
    - post_pk is the primary key of post
    ```json
    {
        "title": "comment-title",
        "content": "comment-content"
    }
    ```
    - The topic author is passed from token setted in `Authorization` header.
- [PUT] /topics/url_name/posts/post_pk/comments/pk/
    - url_name is a slug of topic
    - post_pk is the primary key of post
    - only the author has permission to update
    ```json
    {
        "title": "updated-comment-title",
        "content": "updated-comment-content"
    }
    ```
- [PATCH] /topics/url_name/posts/post_pk/comments/pk/
    - url_name is a slug of topic
    - post_pk is the primary key of post
    - only the author has permission to update
    - All fields are optional
    - Ex.:
    ```json
    {
        "title": "single-update-comment-title",
    }
    ```
- [GET] /topics/url_name/posts/post_pk/comments/
    - List all comments of post passed
- [GET] /topics/url_name/posts/post_pk/comments/pk/
    - Retrieve comment of post passed
- [DELETE] /topics/url_name/posts/post_pk/comments/pk/
