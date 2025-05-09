from setuptools import setup
import mistletoe

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mistletoe',
    version=mistletoe.__version__,
    description='A fast, extensible Markdown parser in pure Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/miyuchina/mistletoe',
    author='Mi Yu',
    author_email='hello@afteryu.me',
    license='MIT',
    packages=['mistletoe', 'mistletoe.contrib'],
    package_data={'mistletoe': ['py.typed']},
    entry_points={'console_scripts': ['mistletoe = mistletoe.__main__:main']},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: Markdown',
    ],
    keywords='markdown lexer parser development',
    python_requires='~=3.5',
    zip_safe=False,
)
