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
