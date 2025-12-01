import setuptools

setuptools.setup(
    name="watch_imports", 
    version="0.0.1",
    author="MarkBaggett",
    author_email="mbaggett@sans.org",
    description="When imported it prints other imports so you can find the circular references.",
    long_description="When imported it prints other imports so you can find the circular references.",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires = [],
    entry_points = {
        'console_scripts': ['watch_imports=watch_imports.__main__:main',
        'myprogram=watch_imports.__main__:about']
        },
    python_requires='>=3.6'
)
