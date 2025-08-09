"""Setup configuration for anvil-core library."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="anvil-core",
    version="0.1.0",
    author="Anvil Team",
    author_email="adrian.belmans@gmail.com",
    description="Core library for the Anvil Suite - shared pattern analysis and fingerprinting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/code-periodic-table",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "libcst>=0.4.0",
        "GitPython>=3.1.0",
        "click>=8.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "mypy>=0.950",
            "flake8>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "anvil-core=anvil_core.cli:main",
        ],
    },
)