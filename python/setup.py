from setuptools import setup, find_packages
import pathlib
import os

_repo_dir = os.environ.get("GITHUB_WORKSPACE")
assert _repo_dir
setup(
    name="rmmbr",
    version="0.0.3",
    description="Simple persistent caching.",
    long_description=(pathlib.Path(_repo_dir) / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/uriva/rmmbr",
    packages=find_packages(),
    install_requires=[
        "redis>=3.5.3",
        "python-dotenv>=0.17.1",
        "pytest",
        "httpx",
        "aiofiles",
        "pytest-asyncio",
    ],
    entry_points={"console_scripts": ["cache=cache.cli:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
