from sqlalchemy import create_engine, text


db_connection_string = "mysql+pymysql://uts8nfyaqrwj5lobaxvq:pscale_pw_4HSqAzt68pnzYCEtEqnFYCjfpIq04EQza1RYMWmobvH@aws.connect.psdb.cloud/quinncareers?charset=utf8mb4"
# 创建数据库引擎和会话


engine = create_engine(db_connection_string, connect_args = {'ssl':{"ssl_ca":'/etc/ssl/cert.pem'}})

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  result_all = result.all()
  
# Session = sessionmaker(bind=engine)
# session = Session()


# 定义映射类
# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)
#     email = Column(String)

#     def __repr__(self):
#         return f"<User(name='{self.name}', age={self.age}, email='{self.email}')>"

# 创建表
# Base.metadata.create_all(engine)

# 添加新用户
# new_user = User(name='Alice', age=25, email='alice@example.com')
# session.add(new_user)
# session.commit()

# 查询所有用户
# users = session.query(User).all()
# print(users)