from setuptools import setup, find_packages
import os

setup(
    name='mtkclient',
    version='1.4',
    packages=find_packages(),
    install_requires=[
        "attrs",
    ],
    long_description=open("README.md").read(),
    scripts=['mtk','stage2','mtkclient/Tools/brom_to_offs','mtkclient/Tools/da_parser'],
    data_files = ['LICENSE','README.md'],
    long_description_content_type="text/markdown",
    url='https://github.com/bkerler/mtkclient',
    project_urls={
        "Bug Tracker": "https://github.com/bkerler/mtkclient/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT License',
    author='B. Kerler',
    author_email='info@revskills.de',
    description='Mediatek reverse engineering and flashing tools',
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False
)
