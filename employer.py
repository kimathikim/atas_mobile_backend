from app.models.user import User
from app.models import storage
user = User()
user.email = "bkimathi@kabarak.ac.k"
user.password = "Kimathi@202"
user.first_name = "BraN"
user.last_name = "Kimthkk"
user.user_type = "Employer"
user.save()
print(user)
print(storage.get(User, user.id))
