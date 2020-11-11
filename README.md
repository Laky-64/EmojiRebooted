Emoji(Rebooted)
=====

Emoji for Python.  This project was inspired by `kyokomi <https://github.com/carpedm20/emoji/>`__.


Example
-------

The entire set of Emoji codes as defined by the `unicode consortium <http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html>`__
is supported in addition to a bunch of `aliases <http://www.emoji-cheat-sheet.com/>`__.  By
default, only the official list is enabled but doing ``emoji.emojize(use_aliases=True)`` enables
both the full list and aliases.

.. code-block:: python

    >> import emoji_decoder
    >> print(emoji_decoder.emojize('Python is :thumbs_up:'))
    Python is 👍
    >> print(emoji_decoder.emojize('Python is :thumbsup:', use_aliases=True))
    Python is 👍
    >> print(emoji_decoder.demojize('Python is 👍'))
    Python is :thumbs_up:
    >>> print(emoji_decoder.emojize("Python is fun :red_heart:"))
    Python is fun ❤
    >>> print(emoji_decoder.emojize("Python is fun :red_heart:",variant="emoji_type"))
    Python is fun ❤️ #red heart, not black heart

..

More Info At https://github.com/carpedm20/emoji/blob/master/README.rst