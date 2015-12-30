import pytest

from mangacork import utils

@pytest.fixture
def page_bad_format():
    page = {'chapter': "chapter1", 'page': 3}
    return page

@pytest.fixture
def page_good_format():
    page = {'chapter':'manga_ch1', 'page':'x_v001-009'}
    return page

@pytest.fixture
def page_no_zeroes():
    page_no_zeroes = {'chapter':'manga_ch1', 'page':'x_v1-9'}
    return page_no_zeroes


@pytest.fixture
def last_page_list_empty():
    return []

@pytest.fixture
def last_page_list():
    return ['x_v002-010', 'x_v001-009']

def test_build_img_path(page_bad_format):
    chapter = page_bad_format["chapter"]
    page = page_bad_format["page"]
    expected_output = "/chapter1/3"
    assert utils.build_img_path(chapter,page) == expected_output

def test_increment_page_number_bad_format(page_bad_format):
    with pytest.raises(ValueError):
        current_page = utils.build_img_path(page_bad_format["chapter"],
                                            page_bad_format["page"])
        utils.increment_page_number(current_page)


def test_increment_page_number_good_format(page_good_format):
    chapter = page_good_format["chapter"]
    page = page_good_format["page"]
    current_page = utils.build_img_path(chapter, page)
    next_page = utils.increment_page_number(current_page)
    expected_output = '/manga_ch1/x_v001-010'
    assert next_page == expected_output


def test_increment_page_number_no_zero(page_no_zeroes):
    chapter = page_no_zeroes["chapter"]
    page = page_no_zeroes["page"]
    current_page = utils.build_img_path(chapter,page)
    next_page = utils.increment_page_number(current_page)
    expected_output = '/manga_ch1/x_v1-010'
    assert next_page == expected_output

def test_last_page_empty_list(last_page_list_empty, page_good_format):
    page = page_good_format["page"]
    assert utils.is_last_page(page, last_page_list_empty) == False


def test_last_page_list(page_good_format, last_page_list) :
    page = page_good_format["page"]
    assert utils.is_last_page(page, last_page_list) == True

