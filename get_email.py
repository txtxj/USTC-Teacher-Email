from login import Login
from lesson import Lesson
from config import STUID, PASSWORD

# Log in and get the cookies
login = Login(STUID, PASSWORD)
session = login.login()

# Get teacher email
lesson = Lesson(session)
email_list = lesson.find_all()

# output
for p in email_list:
	print(p)

