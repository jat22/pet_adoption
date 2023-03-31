from models import Pet, db
from app import app

db.drop_all()
db.create_all()

pet1 = Pet(name="Fido", 
           species="dog", 
           photo_url="https://hgtvhome.sndimg.com/content/dam/images/hgtv/fullset/2022/6/16/1/shutterstock_1862856634.jpg.rend.hgtvcom.966.644.suffix/1655430860853.jpeg", notes="He loves treats and pets!")
pet2 = Pet(name="Milo", 
           species="cat", 
           photo_url="https://images.unsplash.com/photo-1586042091284-bd35c8c1d917?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8c21hbGwlMjBjYXR8ZW58MHx8MHx8&w=1000&q=80", notes="Sunny spots are his fav")
pet3 = Pet(name="Porkie", 
           species="porcupine", 
           photo_url="https://www.eekwi.org/sites/default/files/styles/original/public/2019-12/porcupine.jpg?itok=P5gAT7Jx", notes="He loves treats and pets!")
pet4 = Pet(name="Happy", 
           species="fish", 
           photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdUo8-54WaymntAYOi--_xzl-G_19CvQG1MZj1eu4UnkUmT5FkK96lrL8CERfWfpDmYE66Eut5BkM&usqp=CAU&ec=48600113", notes="Come swim with me")

db.session.add_all([pet1, pet2, pet3, pet4])
db.session.commit()