"""basemodel"""

from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, String, DateTime


class BaseModel(object):
    id = Column(
        String(60), primary_key=True, default=str(uuid4()), nullable=False
    )
    updated_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        else:
            if "__class__" in kwargs:
                del kwargs["__class__"]

            self.__dict__.update(kwargs)

            if "created_at" in kwargs:
                self.created_at = datetime.fromisoformat(kwargs["created_at"])
            else:
                self.created_at = datetime.utcnow()

            if "updated_at" in kwargs:
                self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
            else:
                self.updated_at = datetime.utcnow()

            if "id" in kwargs:
                self.id = kwargs["id"]
            else:
                self.id = str(uuid4())

    # def save(self):
    #     self.updated_at = datetime.utcnow()
    #     storage.save(self)

    def to_dict(self):
        new_dict = {}

        new_dict.update(self.__dict__)

        new_dict["created_at"] = datetime.isoformat(new_dict["created_at"])
        new_dict["updated_at"] = datetime.isoformat(new_dict["updated_at"])

        new_dict["__class__"] = self.__class__.__name__

        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]

        return new_dict
