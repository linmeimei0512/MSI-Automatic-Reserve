#   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#    Copyright (C) 2024 MSI-FUNTORO
#  #
#    Licensed under the MSI-FUNTORO License, Version 1.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#  #
#        https://www.funtoro.com/global/
#  #
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#   ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
library_version = '1.0.1.1811'

from datetime import datetime

def set_library_version(major, minor, patch):
    start_day = datetime(2020, 1, 1)
    print('start day: {}'.format(start_day))

    now_day = datetime.now()
    print('now day: {}'.format(now_day))

    version = '{}.{}.{}.{}'.format(major, minor, patch, (now_day - start_day).days)
    print('version: {}'.format(version))

    file_data = ''
    with open('version.py', 'r') as f:
        for line, line_str in enumerate(f.readlines()):
            if line + 1 == 16:
                line_str = 'library_version = \'{}\'\n'.format(version)
            file_data += line_str

    with open('version.py', 'w') as f:
        f.write(file_data)


def have_new_version():
    import requests
    response = requests.get('https://api.github.com/repos/linmeimei0512/MSI-Snap-Up/releases/latest')
    print(response)


if __name__ == '__main__':
    set_library_version(major=1, minor=0, patch=1)
