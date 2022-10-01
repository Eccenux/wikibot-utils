import os, re
# pip install Unidecode
from unidecode import unidecode

def make_safe_filename(title):
	"""
	Safe name for a file.
	"""
	titleTrans = title
	titleTrans = unidecode(titleTrans)
	titleTrans = re.sub(r'[:/]', r'.', titleTrans)
	titleTrans = re.sub(r'[^a-zA-Z0-9.]', r'_', titleTrans)
	return titleTrans

def save_page_content(page, base_path, suffix = ""):
	"""
	Save page contents to a file.
	
	@param page pywikibot page object.
	@param output_path Base directory.
	"""
	# safe name for a file
	titleTrans = make_safe_filename(page.title())
	# must be limited due to limited size of paths on Windows (260 characters by default)
	titleLimit = 120
	file = "page_" + titleTrans[:titleLimit] + ".id=" + str(page.pageid) + suffix + ".txt"
	#print("\t", file)
	path = os.path.join(base_path, file)
	with open(path, "w+", encoding='utf-8') as text_file:
		text_file.write(page.text)

def save_list(list_data, base_path, list_name, append = True):
	"""
	Save a list (array) to a file.
	
	@param page pywikibot page object.
	@param output_path Base directory.
	"""
	file = make_safe_filename(list_name)
	#print("\t", file)
	path = os.path.join(base_path, file)
	access_mode = "w+"
	if append:
		access_mode = "a+"
	with open(path, access_mode, encoding='utf-8') as text_file:
		size = text_file.tell()
		if size > 0:
			text_file.write(",\n")
		text_file.write(str(list_data))
