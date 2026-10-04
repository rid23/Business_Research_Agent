

def clean_text(text:str) -> str:
    """
    Cleans the input text by removing extra whitespace and newlines.

    Args:
        text (str): The text to be cleaned.
        """
    lines = []
    for line in text.splitlines():
        stripped_line = line.strip()
        if not stripped_line:
            continue
        if len(stripped_line) < 2:
            continue
        lines.append(stripped_line)
    # Remove extra whitespace and newlines
    cleaned_text = '\n'.join(lines)
    return cleaned_text