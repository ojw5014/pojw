from setuptools import setup, find_packages
 
setup(
    name                = 'pojw',
    # Package version
    version             = '0.0.5',
    license             = 'MIT',
    author              = 'Jinwook.On',
    author_email        = 'ojw5014@hanmail.net',
    description         = 'OpenJigWare 원격 제어 소스',
    url                 = 'https://github.com/ojw5014/pojw',
    packages            = find_packages(),
    # 해당 패키지를 사용하기 위해 필요한 파이썬 버전을 적습니다.
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
