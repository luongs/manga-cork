import os


def increment_page_number(page):
    page, page_number = page.split('-')
    # Add leading zeroes to keep expected page format
    page_number = str(int(page_number) + 1).zfill(3)
    next_page = '{page}-{page_number}'.format(
        page=page, page_number=page_number)

    return next_page


def build_img_path(chapter, page):
    return '/{}/{}'.format(chapter, page)


# Seems inefficient to read file after each page?
# Can this be done only once per chapter?
def is_last_page(chapter, current_page):
    filepath = '{}/mangacork/static/images/{}.txt'.format(os.getcwd(), chapter)
    last_page = ''

    with open(filepath) as f:
        last_page = f.read()

    if current_page == last_page:
        return True

    return False
