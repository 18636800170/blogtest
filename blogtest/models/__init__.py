from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
assert isinstance(db, SQLAlchemy)

# class Modle(object):
#
#     @classmethod
#     def get(cls,pk):
#         return cls.query.get(pk)
#
#     def add(self):
#         db.session.add(self)
#
#     def commit(self):
#         try:
#             db.session.commit()
#         except Exception:
#             db.session.rollback()
#             return Exception
#
#
#     @classmethod
#     def delete(cls):
#         db.session.delete(cls)
