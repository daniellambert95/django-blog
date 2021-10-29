from git import Repo

repo = Repo("/home/danjlambert95/django-blog/myblog/")
assert not repo.bare