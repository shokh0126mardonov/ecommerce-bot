from .database import Base,engine
from .models import User

def create_models():
    Base.metadata.create_all(engine)