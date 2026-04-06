import langcodes


def _find_language_tag(lang: str) -> str:
    """Search `langcodes` for a language."""
    try:
        return langcodes.find(lang).language
    except Exception as e:
        raise ValueError(f"Could not find any language matching '{lang}'") from e

def standardize_language_input(lang: str) -> str:
    """Standardize user-provided language input into a two-letter IETF language code.
    
    Args:
        lang: User-provided language input.
    
    Returns:
        Two-letter IETF language code, e.g. 'en', 'ko', 'bg'.
    
    Examples:
        >>> standardize_language_input("Canadian english")
        'en'
        >>> standardize_language_input("en-CA")
        'en'
        >>> standardize_language_input("english")
        'en'
    """
    if langcodes.tag_is_valid(lang):
        tag = langcodes.get(lang).language
    else:
        tag = _find_language_tag(lang)
    
    display_name = langcodes.get(tag).display_name()
    print(f"Encoded language input='{lang}' as code='{tag}' ({display_name})")
    return tag
