from enum import Enum


class UserType(Enum):
    AUTHOR = 'author'
    READER = 'reader'
    ADMIN = 'admin'


class PostStatus(Enum):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    DELETED = 'deleted'
