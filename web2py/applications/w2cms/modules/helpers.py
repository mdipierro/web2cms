'''
Created on Oct 30, 2011
@author: samu
'''

from gluon import *

def use_custom_view(viewname):
    """Decorator to be used to customize the view to be used
    to render a given controller.
    """
    def _use_newcontroller(func):
        def _newcontroller():
            current.response.view = '%s.%s' % (viewname, current.request.extension)
            return func()
        return _newcontroller
    return _use_newcontroller

STATIC_BLOCKS = {}
STATIC_BLOCKS['right_sidebar'] = [
    ('My Block %d' % i, "Lorem ipsum content goes here! #%d" % i)
    for i in xrange(4)
]

def get_region_content(region_name, custom_db=None, request_context=None):
    """Get the content for a given region / page.
    
    :param region_name: An identifier of the region, such as 'left_sidebar' or
        'my_example_region'
    :param request_context: The ``request`` object. Defaults to current.request
    """
    raise DeprecationWarning
#    
#    if request_context is None:
#        request_context = current.request
#    
#    if custom_db is None and 'db' in globals():
#        custom_db = db
#    
#    blocks = db(db.block.region==region_name).select(db.block.ALL, orderby=db.block.weight)
#
#    if blocks:
#        return XML("\n".join([
#            current.response.render('generic/block.html', dict(block=block))
#            for block in blocks
#        ]))
#
#    return ''
    
def get_region(region_name, custom_db=None, request_context=None):
    """For HTML requests only, return the region content wrapper in a <div>,
    if any content is present, or an empty string if not.
    """
    raise DeprecationWarning
#    if request_context is None:
#        request_context = current.request
#    
#    region_content = get_region_content(
#        region_name=region_name,
#        custom_db=custom_db,
#        request_context=request_context)
#    if region_content:
#        if request_context.extension == 'html':
#            return DIV(region_content, _id=region_name)
#    return ""


def get_comments(db, obj_type, obj_delta):
    """Get list of comments to a given object"""
    raise DeprecationWarning

def recursive_update(d1,d2):
    """Recursively update a dictionary or dict-like object."""
    if not hasattr(d2, '__getitem__'):
        raise ValueError, "d2 is not a dict-like"
    for k in d2.keys():
        try:
            recursive_update(d1[k], d2[k])
        except:
            d1[k] = d2[k]
