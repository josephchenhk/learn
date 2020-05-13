# -*- coding: utf-8 -*-
# @Time    : 11/1/2019 9:26 AM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: 13.8.py
# @Software: PyCharm

"""
13.8 创建和解压归档文件

"""

import shutil

# [('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"), ('tar', 'uncompressed tar file'), ('xztar', "xz'ed tar-file"), ('zip', 'ZIP file')]
print(shutil.get_archive_formats())

shutil.make_archive('13.8-test-zipfile','zip','test')

shutil.unpack_archive('13.8-test-zipfile.zip')