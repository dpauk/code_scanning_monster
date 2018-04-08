import re

from code_scanning_monster.code_scanning_monster import CodeScanningMonster


REGEX_TEMPLATE = 'http:\/\/.*{replacement}[^\s]+'


class DetectHttp(CodeScanningMonster):
    def __init__(self, url):
        super.__init__()
        super.get_code_to_scan(owner, repo)

    def detect_http(self, detection_string, string_to_test):
        current_template = REGEX_TEMPLATE.replace('{replacement}', detection_string)

        all_matching_values = set()

        # split the string so that multiple URLs can be detected
        split_string = string_to_test.split()

        for _ in split_string:
            matches = re.search(current_template, _)
            if matches is not None:
                all_matching_values.add(matches.group(0))

        return all_matching_values


if __name__ == '__main__':
    dh = DetectHttp()
    results = dh.detect_http('bbc', 'Read the news at http://www.bbc.co.uk or at http://www.bbc.com')
    print(results)
    for result in results:
        print(result)
