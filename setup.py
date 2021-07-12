import os

from setuptools import setup, find_packages

version = "0.3.2"

try:
    readme = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()
except:
    readme = ""

template_dirs = []
static_dirs = []
locale_dirs = []

templates = []
static_files = []
locale_files = []

for template_dir in template_dirs:
    templates += [
        os.path.join(template_dir, f) for f in os.listdir(template_dir)
    ]

for static_dir in static_dirs:
    static_files += [
        os.path.join(static_dir, f) for f in os.listdir(static_dir)
    ]

for locale_dir in locale_dirs:
    locale_files += [
        os.path.join(locale_dir, f) for f in os.listdir(locale_dir)
    ]

dependency_links = []

# Dependencies
install_requires = [
    "Babel>=2.1.1",
]

tests_require = [
    "Faker",
    "pytest",
    "pytest-cov",
    "pytest-django",
    "pytest-ordering",
    "coverage",
]

setup(
    name="valuta",
    version=version,
    description="Currencies done right.",
    long_description=f"{readme}",
    long_description_content_type="text/x-rst",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or "
        "later (LGPLv2+)",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/barseghyanartur/valuta/issues",
        "Documentation": "https://valuta.readthedocs.io/",
        "Source Code": "https://github.com/barseghyanartur/valuta",
        "Changelog": "https://valuta.readthedocs.io/"
        "en/latest/changelog.html",
    },
    keywords="currency",
    author="Artur Barseghyan",
    author_email="artur.barseghyan@gmail.com",
    url="https://github.com/barseghyanartur/valuta/",
    package_dir={"": "src"},
    packages=find_packages(where="./src"),
    entry_points={
        "console_scripts": [
            "valuta-generate-currencies = valuta.cli:generate_currencies",
            "valuta-list-currencies = valuta.cli:list_currencies",
        ]
    },
    license="GPL-2.0-only OR LGPL-2.1-or-later",
    install_requires=install_requires,
    tests_require=tests_require,
    dependency_links=dependency_links,
    package_data={"valuta": templates + static_files + locale_files},
    include_package_data=True,
)
