# -*- coding: utf-8 -*-
# @Time    : 29/4/2020 12:23 PM
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: setup.py
# @Software: PyCharm

from setuptools import setup, find_packages

setup(
    name='quantkits', # 包名称，之后如果上传到了pypi，则需要通过该名称下载
    version='0.0.2',  # version只能是数字，还有其他字符则会报错
    keywords=('setup', 'quantkits'),
    description='setup quantkits',
    long_description='',
    license='MIT',    # 遵循的协议
    install_requires=['sqlalchemy', 'pandas', 'numpy', 'pytz',
                      'selenium', 'requests', 'bs4'], # 这里面填写项目用到的第三方依赖
    author='josephchen',
    author_email='josephchenhk@gmail.com',
    packages=find_packages(), # 项目内所有自己编写的库
    platforms='any',
    url='', # 项目链接,
    include_package_data=True,
    entry_points={
        'console_scripts':[
            'example=example.test:main'
        ]
    },
)
