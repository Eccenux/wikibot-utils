import os, re
# pip install Unidecode
from unidecode import unidecode

def save_page_content(page, base_path):
	"""
	Save page contents to a file.
	
	@param page pywikibot page object.
	@param output_path Base directory.
	"""
	# safe name for a file
	titleTrans = page.title()
	titleTrans = unidecode(titleTrans)
	titleTrans = re.sub(r'[:/]', r'.', titleTrans)
	titleTrans = re.sub(r'[^a-zA-Z0-9.]', r'_', titleTrans)
	# must be limited due to limited size of paths on Windows (260 characters by default)
	titleLimit = 120
	file = "page_" + titleTrans[:titleLimit] + ".id=" + str(page.pageid) + ".txt"
	#print("\t", file)
	path = os.path.join(base_path, file)
	with open(path, "w+", encoding='utf-8') as text_file:
		text_file.write(page.text)
