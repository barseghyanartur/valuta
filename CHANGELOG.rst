Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: text

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.1.9
-----
2021-06-15

- Minor fixes in the Django app (for Django 2.2).

0.1.8
-----
2021-06-15

- Added templatetags library for Django integration app.

0.1.7
-----
2021-06-05

- Replace all imports from `valuta.registry` with imports from `valuta.base`.
- Documentation improvements.

0.1.6
-----
2021-06-04

- Move ``Registry`` class from ``valuta.registry`` to ``valuta.base``.
- Add ``valuta.shortcuts`` module as shorthand for when you have a string
  representation of the currency code and the value to convert and don't
  want to handle possible exceptions.

0.1.5
-----
2021-05-23

- Add more tests.
- Add an argument ``--sort-by-value`` for ``valuta-list-ccurrencies`` command.

0.1.4
-----
2021-05-20

- Add more tests.

0.1.3
-----
2021-05-19

- Minor fixes.

0.1.2
-----
2021-05-19

- Change of the default display format in the Django integration app.
- Allow customization of the display format in the Django integration app.

0.1.1
-----
2021-05-19

- Improve docs.
- Clean up.
- Minor fixes.

0.1
---
2021-05-17

- Initial beta release.
