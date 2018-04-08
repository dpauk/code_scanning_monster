import os
import zipfile

from io import BytesIO

import requests


GITHUB_PUBLIC_API_ZIP = 'https://api.github.com/repos/{owner}/{repo}/zipball/master'


class CodeScanningMonster(object):
    """
    This is the parent class of all the code scanning monsters.
    It should never be instantiated on its own - it's just a class for other
        classes to inherit from.
    """

    def __init__(self):
        pass

    def get_code_to_scan(self, site, owner, repo):
        """
        Uses:
        - GitHub API v3
        """
        if 'github_public' in site:
            self._get_github_public_code(owner, repo)

    def get_files_to_scan(self, extensions_to_scan='py'):
        self.files_to_scan = self._get_files_with_extension(extensions_to_scan)

    # TODO: make the class into a context manager
    def delete_temp_directory(self):
        pass

    def _get_files_with_extension(self, extensions_to_scan):
        files_with_extension = set()

        for root, dirs, files in os.walk(self.zip_path):
            for file in files:
                if f'.{extensions_to_scan}' in file:
                    file_path = os.path.join(root, file)
                    files_with_extension.add(file_path)
        
        return files_with_extension

    def _get_github_public_code(self, owner, repo):
        """Gets a zip from a public github repo"""
        zip_to_pull_owner = GITHUB_PUBLIC_API_ZIP.replace('{owner}', owner)
        zip_to_pull = zip_to_pull_owner.replace('{repo}', repo)

        temp_path = self._get_temp_directory()

        self.zip_path = os.path.join(temp_path, f'{owner}_{repo}')

        self._get_code_and_unzip(zip_to_pull, self.zip_path)

    def _get_temp_directory(self):
        # TODO: This should pull from an environmental variable rather than a local temp
        current_path = os.getcwd()
        temp_path = os.path.join(current_path, 'temp')
        return temp_path

    def _get_code_and_unzip(self, api_url, temp_directory):
        # TODO: deal with request failures
        request = requests.get(api_url)
        unzipped_data = zipfile.ZipFile(BytesIO(request.content))
        unzipped_data.extractall(temp_directory)
        unzipped_data.close()

    # https://api.github.com/repos/dpauk/rock_paper_scissors/zipball/master

    # TODO: delete zip file

    # TODO: probably better just to pass individual files into the scanner rather than the zip malarkey?  Just pass the "raw" url?


if __name__ == '__main__':
    csm = CodeScanningMonster()
    csm.get_code_to_scan('github_public', 'dpauk', 'rock_paper_scissors')
    csm.get_files_to_scan()
