参考：
1. [Python3及应用7-打包发布自己的库](https://github.com/ecmadao/Coding-Guide/blob/master/Notes/Python/Python%E5%8F%8A%E5%BA%94%E7%94%A8/Python3%E5%8F%8A%E5%BA%94%E7%94%A87-%E6%89%93%E5%8C%85%E5%8F%91%E5%B8%83%E8%87%AA%E5%B7%B1%E7%9A%84%E5%BA%93.md)
2. [twine](https://pypi.org/project/twine/)
3. [Using TestPyPI](https://packaging.python.org/guides/using-testpypi/)

打包到test.pypi:

```
>>> python setup.py sdist bdist_wheel
>>> twine upload --repository-url https://test.pypi.org/legacy/ dist/*
>>> pip install --index-url https://test.pypi.org/simple/ your-package
```

打包到pypi

```
>>> python setup.py sdist bdist_wheel
>>> twine upload dist/*
>>> pip install your-package
```

