from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
import os
from models import User
from schemas import UserCreate, UserLogin

class AuthService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    @staticmethod
    def register_user(user_data: UserCreate, db):
        # Registration logic here
        pass
    
    @staticmethod
    def login_user(credentials: UserLogin, db):
        # Login logic here
        pass