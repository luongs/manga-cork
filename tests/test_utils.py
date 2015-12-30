import pytest

from mangacork import utils

@pytest.fixture
def sample_page_bad_format():
    sample_page = {'chapter': "chapter1", 'page': 3}
    return sample_page

@pytest.fixture
def sample_page_good_format():
    sample_page = {'chapter':'manga_ch1', 'page':'x_v001-009'}
    return sample_page

@pytest.fixture
def last_page_list_empty():
    return []

@pytest.fixture
def sample_last_page_list():
    return ['x_v002-010', 'x_v001-009']

def test_build_img_path(sample_page_bad_format):
    chapter = sample_page_bad_format["chapter"]
    page = sample_page_bad_format["page"]
    expected_output = "/chapter1/3"
    assert utils.build_img_path(chapter,page) == expected_output

def test_increment_page_number_bad_format(sample_page_bad_format):
    with pytest.raises(ValueError):
        current_page = utils.build_img_path(sample_page_bad_format["chapter"],
                                            sample_page_bad_format["page"])
        utils.increment_page_number(current_page)


def test_increment_page_number_good_format(sample_page_good_format):
    chapter = sample_page_good_format["chapter"]
    page = sample_page_good_format["page"]
    current_page = utils.build_img_path(chapter, page)
    next_page = utils.increment_page_number(current_page)
    expected_output = '/manga_ch1/x_v001-010'
    assert next_page == expected_output

def test_last_page_empty_list(last_page_list_empty, sample_page_good_format):
    page = sample_page_good_format["page"]
    assert utils.is_last_page(page, last_page_list_empty) == False

def test_last_page_list(sample_page_good_format, sample_last_page_list) :
    page = sample_page_good_format["page"]
    assert utils.is_last_page(page, sample_last_page_list) == True
