def increment_page_number(page):
    page, page_number = page.split('-')
    # Add leading zeroes to keep expected page format
    page_number = str(int(page_number) + 1).zfill(3)
    next_page = '{page}-{page_number}'.format(
        page=page, page_number=page_number)

    return next_page


def build_img_path(chapter, page):
    return '/{}/{}'.format(chapter, page)
