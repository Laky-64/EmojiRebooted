# Emoji(Rebooted)

Emoji for Python.  This project was inspired by [Taehoon Kim](https://github.com/carpedm20/emoji/).


## Example

The entire set of Emoji codes as defined by the [unicode consortium](http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html)
is supported in addition to a bunch of [aliases](http://www.emoji-cheat-sheet.com/).  By
default, only the official list is enabled but doing ``emoji.emojize(use_aliases=True)`` enables
both the full list and aliases.

``` python

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

```

[More Info](https://github.com/carpedm20/emoji/blob/master/README.rst)