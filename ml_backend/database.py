import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm


DATABASE_URL = 'postgresql://admin:pass@192.168.1.8:5432/test_app'

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()
