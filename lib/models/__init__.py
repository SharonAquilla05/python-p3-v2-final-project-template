from .database import database

database.create_tables()

from .categories import Category
from .tasks import Task
from .users import User
