#!/usr/bin/env python3

from distutils.core import setup


setup(
    name="pieseł",
    version="1.0",
    description="pieseł so cute, wow",
    url="https://github.com/zyga/piesel",
    scripts=['pieseł'],
    data_files=[
        ('/usr/share/icons/hicolor/128x128/apps', ['pieseł.png']),
        ('/usr/share/applications', ['pieseł.desktop'])
    ])
