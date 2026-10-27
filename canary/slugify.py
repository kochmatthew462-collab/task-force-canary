"""ASCII slug for the protected canary acceptance tests."""

import re


def slugify(text: str) -> str:
    """Keep lowercase ASCII letters and digits. Other runs become one hyphen."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
