from login import Login
from lesson import Lesson
from config import STUID, PASSWORD

# Log in and get the cookies
login = Login(STUID, PASSWORD)
login.login()
cookies = login.cookies

# Get teacher email
lesson = Lesson(cookies)
email_list = lesson.find_all()

# output
for p in email_list:
	print(p)

