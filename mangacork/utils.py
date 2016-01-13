import logging
import os

from wtforms.validators import ValidationError

logger = logging.getLogger(__name__)

class Unique(object):
    def __init__(self, model, field, message=u'This element already exists'):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        check = self.model.query.filter(self.field == field.data).first()
        if check:
            raise ValidationError(self.message)

def increment_page_number(page):
    '''
    String -> String
    Returns the page incremented by one
    Expected page format: chapter-pagexxx
    '''
    try:
        page, page_number = page.split('-')
    except ValueError:
        raise ValueError('- expected in filename')
        logger.debug('- expected in filename')

    # Add leading zeroes to keep expected page format
    page_number = str(int(page_number) + 1).zfill(3)
    next_page = '{page}-{page_number}'.format(
        page=page, page_number=page_number)

    return next_page


def build_img_path(chapter, page):
    '''
    String, String -> String
    produces an image path to match endpoints using chapter and page strings
    '''
    return '/{}/{}'.format(chapter, page)


def is_last_page(current_page, last_page_list):
    '''
    String, List -> Boolean
    returns true if the current page matches a value in the last page list
    '''
    if current_page in last_page_list:
        return True
    return False
