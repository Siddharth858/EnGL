#presently we support manual adding:
import json

with open("listening_files.json","r") as f:
	list_file = json.load(f)
	total_lessons = list_file['total_lessons']


with open("listening_files.json","w+") as f:
	#list_file['Lesson_2'] = ["Flag Football","01:16","Medium"]
	list_file['Lesson_1'] = ["How to look inside Brain","04:52","Medium"]
	list_file['Lesson_2'] = ["Mining Minerals from sea water","02:53","Medium"]
	list_file['Lesson_3'] = ["The job we will lose","04:30","Medium"]
	list_file['Lesson_4'] = ["Print Your own medicine","02:59","Medium"]
	list_file['Lesson_5'] = ["My underwater Robot","04:13","Medium"]
	#list_file['Lesson_6'] = ["Playing Tennis tournament","02:45","Medium"]
	#list_file['Lesson_7'] = ["Problems with my english","07:51","Medium"]
	#list_file['Lesson_8'] = ["Stephanies likes and dislikes","01:47","Medium"]
	#list_file['Lesson_9'] = ["Vietnamese food","03:56","Medium"]
	#list_file['Lesson_10'] = ["What is bio-chemistry","02:02","Medium"]
	#list_file['total_lessons'] = 5
	list_file['total_lessons'] = total_lessons + 2			#Change with lesson want to add
	json.dump(list_file,f)
