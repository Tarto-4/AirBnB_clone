from datetime import datetime
import uuid

class BaseModel:
  def __init__(self):
    self.id = str(uuid.uuid4())
    self.created_at = datetime.now()
    self.updated_at = self.created_at

  def __str__(self):
    return f"[{' '.join(self.__class__.__name__.split(' '))}] ({self.id}) {self.__dict__}"

  def save(self):
    self.updated_at = datetime.now()

  def to_dict(self):
    data = dict(self.__dict__)
    data["__class__"] = self.__class__.__name__
    for key, value in data.items():
      if isinstance(value, datetime):
        data[key] = value.isoformat()
    return data
