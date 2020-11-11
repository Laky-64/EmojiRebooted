import re
import sys

import unicode_codes_custom

PY2 = sys.version_info[0] == 2

_EMOJI_REGEXP = None
_DEFAULT_DELIMITER = ":"


def emojize(string, use_aliases=False, delimiters=(_DEFAULT_DELIMITER, _DEFAULT_DELIMITER), variant=None,
            language='en'):
    emoji_unicode = unicode_codes_custom.EMOJI_UNICODE[language]
    pattern = re.compile(u'(%s[a-zA-Z0-9+\\-_&.ô’Åéãíç()!#*]+%s)' % delimiters)

    def replace(match):
        mg = match.group(1).replace(delimiters[0], _DEFAULT_DELIMITER).replace(delimiters[1], _DEFAULT_DELIMITER)
        if use_aliases:
            emj = unicode_codes_custom.UNICODE_EMOJI_ALIAS_ENGLISH.get(mg, mg)
        else:
            emj = emoji_unicode.get(mg, mg)
        if variant is None:
            return emj
        elif variant == "text_type":
            return emj + u'\uFE0E'
        elif variant == "emoji_type":
            return emj + u'\uFE0F'

    return pattern.sub(replace, string)


def demojize(string, use_aliases=False, delimiters=(_DEFAULT_DELIMITER, _DEFAULT_DELIMITER), language='en'):
    emoji_unicode = unicode_codes_custom.UNICODE_EMOJI[language]

    def replace(match):
        codes_dict = unicode_codes_custom.UNICODE_EMOJI_ALIAS_ENGLISH if use_aliases else emoji_unicode
        val = codes_dict.get(match.group(0), match.group(0))
        return delimiters[0] + val[1:-1] + delimiters[1]

    return re.sub(u'\ufe0f', '', (get_emoji_regexp(language).sub(replace, string)))


def get_emoji_regexp(language='en'):
    global _EMOJI_REGEXP
    emoji_unicode = unicode_codes_custom.EMOJI_UNICODE[language]
    if _EMOJI_REGEXP is None:
        emojis = sorted(emoji_unicode.values(), key=len,
                        reverse=True)
        pattern = u'(' + u'|'.join(re.escape(u) for u in emojis) + u')'
        _EMOJI_REGEXP = re.compile(pattern)
    return _EMOJI_REGEXP


def emoji_lis(string, language='en'):
    _entities = []
    for match in get_emoji_regexp(language).finditer(string):
        _entities.append({
            "location": match.start(),
            "emoji": match.group()
        })
    return _entities


def distinct_emoji_lis(string):
    distinct_list = list({c for c in string if c in unicode_codes_custom.UNICODE_EMOJI})
    return distinct_list


def emoji_count(string):
    return len(emoji_lis(string))
