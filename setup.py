from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(name='discord_kartrider', # 패키지 명

    version='0.2',

    long_description = long_description,

    long_description_content_type='text/markdown',

    description='넥슨 API, 카트라이더 TMI, BAZZI를 이용한 크롤링(디스코드 용)',

    author='joonseo7397',

    author_email='joonseo5411@gmail.com',

    url='https://github.com/chunjoonseo541/discord-kartrider',

    license='MIT', # MIT에서 정한 표준 라이센스 따른다

    py_modules=['discord_kartrider'], # 패키지에 포함되는 모듈

    python_requires='>=3',

    install_requires=['selenium', 'nextcord', 'requests'], # 패키지 사용을 위해 필요한 추가 설치 패키지

    packages=['discord_kartrider'], # 패키지가 들어있는 폴더들

    classifiers = ['Programming Language :: Python :: 3.8', 'Programming Language :: Python :: 3.9', 'Programming Language :: Python :: 3.10'],
)