import pytest

from mangacork import utils

@pytest.fixture
def sample_page():
    sample_page = {'chapter': "chapter1", 'page': 3}
    return sample_page

def test_build_img_path(sample_page):
        chapter = sample_page["chapter"]
        page = sample_page["page"]
        expected_output = "/chapter1/3"
        assert utils.build_img_path(chapter,page) == expected_output
