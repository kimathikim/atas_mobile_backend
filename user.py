from app.models.user import User

user = User()
user.email = "brain@jiji"
user.password = "root"
user.first_name = "Brain"
user.last_name = "Kimathi"
user.save()
print(user)
