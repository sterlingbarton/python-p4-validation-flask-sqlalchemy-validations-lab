from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints

    @validates('name')
    def validate_name(self, key, value):
        print(value)
        if value == '':
            raise ValueError('Must have a name value')
        return value

    @validates('phone_number')
    def validate_phone(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError('Phone number must be exactly 10 digits')
        return phone_number

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'


class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints

    @validates('content')
    def validate_content(self, key, value):
        if len(value) < 250:
            raise ValueError('Content must be at least than 250 characters')
        return value

    @validates('summary')
    def validate_summary(self, key, value):
        if len(value) >= 250:
            raise ValueError('Summary must be less than 250 characters')
        return value

    @validates('category')
    def validate_category(self, key, value):
        if value == 'Fiction' or value == 'Non-Fiction':
            return value
        raise ValueError('Category must be either Fiction or Non-Fiction')

    @validates('title')
    def validate_title(self, key, value):
        if value == '' and "Won't Believe" or "Secret" or "Top" or "Guess" not in value:
            raise ValueError('Must have a title')
        return value

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
