import pywikibot
from pywikibot import pagegenerators as pg

def list_template_links(site_obj, tmpl_name, namespaces=-1):
	"""
	Create a generator of pages using or linking the template.
	
	@param site_obj pywikibot.Site()
	@param tmpl_name Template name without namespace.
	@param namespaces Optional array of namespace numbers.

	@returns Generator that can be used to iterate over pages.
		The generator will load 50 pages at a time for iteration.
		Note that a next batch will be loaded automatically by the generator as you iterate.
	"""
	name = "{}:{}".format(site_obj.namespace(10), tmpl_name)
	tmpl_page = pywikibot.Page(site_obj, name)
	ref_gen = tmpl_page.getReferences(follow_redirects=False)
	if namespaces != -1:
		filter_gen = pg.NamespaceFilterPageGenerator(ref_gen, namespaces=namespaces)
		generator = site_obj.preloadpages(filter_gen, pageprops=True)
	else:
		generator = site_obj.preloadpages(ref_gen, pageprops=True)
	return generator
