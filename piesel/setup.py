#!/usr/bin/env python3

from distutils.core import setup

setup(
    name="pieseł",
    version="1.0",
    description="pieseł so cute, wow",
    url="https://github.com/zyga/piesel",
    scripts=['pieseł'],
    data_files=[
        ('/usr/share/icons/hicolor/256x256/apps',
            ['icons/256x256/pieseł.png']),
        ('/usr/share/icons/hicolor/128x128/apps',
            ['icons/128x128/pieseł.png']),
        ('/usr/share/icons/hicolor/64x64/apps',
            ['icons/64x64/pieseł.png']),
        ('/usr/share/applications', ['pieseł.desktop'])
    ])
