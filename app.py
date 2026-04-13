from fastapi import FastAPI,Depends,HTTPException
from model import Users,UserCreate
from database import session,engine
import database_models
from sqlalchemy.orm import Session

app=FastAPI()

database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def greet():
    return "Welcome User"

@app.get("/users")
def get_all_users(db: Session =Depends(get_db)):
    db_users=db.query(database_models.Users).all()
    return db_users

# @app.get("/users/{id}")
# def get_user(id: int,db: Session =Depends(get_db)):
#     db_user=db.query(database_models.Users).filter(database_models.Users.id==id)
#     if db_user:
#         return db_user
#     return "User Not Found"

# @app.get("/users/{id}")
# def get_user(id: int, db: Session = Depends(get_db)):
#     db_user = db.query(database_models.Users).filter(database_models.Users.userID == id).first()

#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")

#     return db_user

@app.get("/users/{id}")
def get_user(id: str, db: Session = Depends(get_db)):
    db_user = db.query(database_models.Users).filter(database_models.Users.userID == id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return db_user

# @app.post("/user/register")
# def new_user(user:Users,db: Session =Depends(get_db)):
#     db.add(database_models.Users(**user.model_dump()))
#     db.commit()
#     return user


@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = database_models.Users(
        name=user.name,
        age=user.age,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# @app.put("/user")
# def update_user(id:int,user:Users,db: Session =Depends(get_db)):
#     db_user=db.query(database_models.Users).filter(database_models.Users.id==id)
#     if db_user:
#         db_user.name=user.name
#         db_user.age=user.age
#         db_user.password=user.password
#         db.commit()
#         return "User Info Updated"
#     else:
#         return "No User Found"

# @app.put("/users/{id}")
# def update_user(id: int, user: Users, db: Session = Depends(get_db)):
#     db_user = db.query(database_models.Users).filter(database_models.Users.userID == id).first()

#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")

#     db_user.name = user.name
#     db_user.age = user.age
#     db_user.password = user.password

#     db.commit()
#     db.refresh(db_user)

#     return {"message": "User updated successfully"}

@app.put("/users/{id}")
def update_user(id: str, user: Users, db: Session = Depends(get_db)):
    db_user = db.query(database_models.Users).filter(database_models.Users.userID == id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.name = user.name
    db_user.age = user.age
    db_user.password = user.password

    db.commit()
    return {"message": "User updated"}

# @app.delete("/user")
# def delete_user(id:int,db: Session =Depends(get_db)):
#     db_user=db.query(database_models.Users).filter(database_models.Users.id==id)
#     if db_user:
#         db.delete(db_user)
#         db.commit()
#     else:
#         return "User not found"

# @app.delete("/users/{id}")
# def delete_user(id: int, db: Session = Depends(get_db)):
#     db_user = db.query(database_models.Users).filter(database_models.Users.userID == id).first()

#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")

#     db.delete(db_user)
#     db.commit()

@app.delete("/users/{id}")
def delete_user(id: str, db: Session = Depends(get_db)):
    db_user = db.query(database_models.Users).filter(database_models.Users.userID == id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()

    return {"message": "User deleted"}

# @app.patch("/users/{id}")
# def update(id: str,name:str=None,age:int=None,password:str=None,db: Session = Depends(get_db)):
#     db_user = db.query(database_models.Users).filter(database_models.Users.userID == id).first()
    
#     if not db_user:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     if name:
#         db_user[id][name]=name
#     if age:
#         db_user[id][age]=age
#     if password:
#         db_user[id][password]=password

#     return db_user
            
from fastapi import HTTPException

@app.patch("/users/{id}")
def update(
    id: str,
    name: str = None,
    age: int = None,
    password: str = None,
    db: Session = Depends(get_db)
):
    db_user = db.query(database_models.Users).filter(database_models.Users.userID == id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if name is not None:
        db_user.name = name

    if age is not None:
        db_user.age = age

    if password is not None:
        db_user.password = password

    db.commit()
    db.refresh(db_user)

    return db_user    

