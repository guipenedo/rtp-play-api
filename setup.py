from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='rtpplayapi',
    version='1.0.0',
    description='An unofficial python api to fetch media from RTPPlay, based on their mobile API.',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Guilherme Penedo',
    author_email='nostrumg@gmail.com',
    keywords=['rtp', 'rtpplay', 'rtp-play', 'api', 'mobile', 'rtp-play-api'],
    url='https://github.com/guipenedo/rtp-play-api',
    download_url='https://pypi.org/project/rtp-play-api/'
)

install_requires = [
    'requests'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
