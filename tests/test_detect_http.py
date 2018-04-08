import pytest

from code_scanning_monster.detect_http import DetectHttp


@pytest.fixture
def set_up():
    detect_http = DetectHttp()
    return detect_http


def test_http_detected_http_url_only(set_up):
    assert set_up.detect_http('bbc', 'http://www.bbc.co.uk') == {'http://www.bbc.co.uk'}


def test_http_detected_htp_url_and_string(set_up):
    assert set_up.detect_http('bbc', 'Read the news at http://www.bbc.co.uk') == {'http://www.bbc.co.uk'}


def test_http_detected_multiple_http_urls(set_up):
    assert set_up.detect_http('bbc', 'Read the news at http://www.bbc.co.uk or at http://www.bbc.com') == {'http://www.bbc.co.uk', 'http://www.bbc.com'}


def test_no_url(set_up):
    assert set_up.detect_http('bbc', 'Read the news at the bbc') == set()


def test_only_https(set_up):
    assert set_up.detect_http('bbc', 'Read the news at https://www.bbc.co.uk') == set()


def test_multiple_https(set_up):
    assert set_up.detect_http('bbc', 'Read the news at https://www.bbc.co.uk or at https://www.bbc.com') == set()


def test_mixture_of_http_and_https(set_up):
    assert set_up.detect_http('bbc', 'Read the news at http://www.bbc.co.uk or at https://www.bbc.com') == {'http://www.bbc.co.uk'}
