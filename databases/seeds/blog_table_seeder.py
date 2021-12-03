"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"title": "Blog 1", "body": "Blog Body 1"})
        Blog.create({"title": "Blog 2", "body": "Blog Body 2"})
        Blog.create({"title": "Blog 3", "body": "Blog Body 3"})