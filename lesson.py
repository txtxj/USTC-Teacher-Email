from config import POOL, TEACHER_NAME
import json
import re


class Lesson:
	def __init__(self, session):
		self.session = session
		self.lesson_id = []
		self.email = None
		self.teacher_name = TEACHER_NAME.split(" ")
		self.headers = {
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
		}

	def get_lesson_id(self):
		sn = \
			re.findall("\d+",
					   self.session.get("https://jw.ustc.edu.cn/for-std/lesson-search", headers=self.headers).url)[0]
		for name in self.teacher_name:
			params = {
				"teacherNameLike": name,
			}
			for p in POOL:
				source = "https://jw.ustc.edu.cn/for-std/lesson-search/semester/{}/search/{}".format(p, sn)
				rsp = self.session.get(source, headers=self.headers, params=params)
				result = json.loads(rsp.content.decode("utf-8"))
				if len(result["data"]) == 0:
					continue
				for course in result["data"]:
					course_id = course["id"]
					teachers = course["teacherAssignmentList"]
					teachers = [teacher["person"]["nameZh"] for teacher in teachers]
					if name in teachers:
						self.lesson_id.append(course_id)
						break
				else:
					continue
				break

	def find_all(self):
		self.get_lesson_id()
		email_list = dict()
		for tid in self.lesson_id:
			params = {
				"lessonId": tid,
			}
			url = "https://jw.ustc.edu.cn/ws/course-adjustment-apply/get-teacher-info"
			rsp = self.session.get(url, headers=self.headers, params=params)
			pairs = json.loads(rsp.content.decode("utf-8"))
			for s in pairs:
				# use 'email_list = dict(email_list, **s)' instead
				email_list = email_list | s
		result = []
		for name in self.teacher_name:
			if name in email_list:
				result.append("{}: {}".format(name, email_list[name]))
		return result
