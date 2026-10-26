"""ASCII slug normalization used by the protected acceptance suite."""

import re


def slugify(text: str) -> str:
    """Lowercase text and collapse non-ASCII-alphanumeric runs into hyphens."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
