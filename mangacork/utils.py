import os

#TODO: Add tests and error handling if pages don't match format expected
def increment_page_number(page):
    try:
        page, page_number = page.split('-')
    except ValueError:
        raise ValueError('- expected')

    # Add leading zeroes to keep expected page format
    page_number = str(int(page_number) + 1).zfill(3)
    next_page = '{page}-{page_number}'.format(
        page=page, page_number=page_number)

    return next_page


def build_img_path(chapter, page):
    return '/{}/{}'.format(chapter, page)


def is_last_page(current_page, last_page_list):
    if current_page in last_page_list:
        return True

    return False
