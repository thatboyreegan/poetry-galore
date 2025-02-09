from sqlalchemy import Column, ForeignKey, Integer, String

from app import db
from app.models.base_model import BaseModel
from app.models.poem import poem_category


class Category(db.Model, BaseModel):
    __tablename__ = "categories"

    name = Column(String(100), nullable=False)

    poem_categories = db.relationship("Poem", secondary=poem_category)
