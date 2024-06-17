from app.models.user import User
from app.models import storage
user = User()
user.email = "brain@j"
user.password = "rot"
user.first_name = "Brai`"
user.last_name = "Kimathkk"
user.save()
print(user)
print(storage.get(User, user.id))
