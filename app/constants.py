from enum import Enum


class UserType(Enum):
    AUTHOR = 'author', 'Author'
    READER = 'reader', 'Reader'
    ADMIN = 'admin', 'Admin'


class PostStatus(Enum):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'published', 'Published'
    ARCHIVED = 'archived', 'Archived'
    DELETED = 'deleted', 'Deleted'
