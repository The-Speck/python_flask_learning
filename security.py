from user import User

users = [
  User(1, 'Alice', '1234')
]

usernameMap = { u.username: u for u in users }
useridMap = { u.id: u for u in users }
 
def authenticate(username, password):
  user = usernameMap.get(username, None)
  if user and user.password == password:
    return user

def identity(payload):
  userId = payload['identity']
  return useridMap.get(userId, None)
