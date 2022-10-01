import pywikibot
from pywikibot import pagegenerators as pg

def get_template_page(site_obj, tpl_name):
	name = "{}:{}".format(site_obj.namespace(10), tpl_name)
	tpl_page = pywikibot.Page(site_obj, name)
	return tpl_page

def list_template_links(site_obj, tpl_name, namespaces=-1):
	"""
	Create a generator of pages using or linking the template.
	
	@param site_obj pywikibot.Site()
	@param tpl_name Template name without namespace.
	@param namespaces Optional array of namespace numbers.

	@returns Generator that can be used to iterate over pages.
		The generator will load 50 pages at a time for iteration.
		Note that a next batch will be loaded automatically by the generator as you iterate.
	"""
	tpl_page = get_template_page(site_obj, tpl_name)
	ref_gen = tpl_page.getReferences(follow_redirects=False)
	if namespaces != -1:
		filter_gen = pg.NamespaceFilterPageGenerator(ref_gen, namespaces=namespaces)
		generator = site_obj.preloadpages(filter_gen, pageprops=True)
	else:
		generator = site_obj.preloadpages(ref_gen, pageprops=True)
	return generator

def list_template_embedded(site_obj, tpl_name, namespaces=None, content=False):
	"""
	Create a generator of pages using (embeding) the template.
	
	@param site_obj pywikibot.Site()
	@param tpl_name Template name without namespace.
	@param namespaces (optional) array of namespace numbers (defaults to any namespace).
	@param content (optional) if True, retrieve the content of the current version
            of each embedding page (default False)

	@returns Generator that can be used to iterate over pages.
		The generator will load 50 pages at a time for iteration.
		Note that a next batch will be loaded automatically by the generator as you iterate.
	"""
	tpl_page = get_template_page(site_obj, tpl_name)
	generator = tpl_page.embeddedin(namespaces=namespaces, content=content)
	return generator
