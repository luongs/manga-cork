from mangacork import utils

def test_build_img_path():
        chapter = "chapter1"
        page = "3"
        expected_output = "/chapter1/3"
        assert utils.build_img_path(chapter,page) == expected_output
