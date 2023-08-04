from models import storage
from models.user import User
from sqlalchemy.exc import SQLAlchemyError


class UserRepo:

    session = None
    me = 'utilty'

    def __init__(self):
        self.session = storage.get_session()

    def findByEmail(self, email: str) -> User:
        if email:
            try:
                query = self.session.query(User).filter_by(email=email)
                return query.first()
            except SQLAlchemyError:
                raise SQLAlchemyError('fecthing user by email failed', self.me)


user_repo = UserRepo()
