from app.models.user import User
from app.models import storage
user = User()
user.email = "bkimathi@kabarak.ac.ke"
user.password = "Kimathi@2022"
user.first_name = "Brai`"
user.last_name = "Kimathkk"
user.user_type = "Employee"
user.save()
print(user)
print(storage.get(User, user.id))
