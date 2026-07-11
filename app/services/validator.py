from urllib.parse import urlparse


def validate_domain(domain: str):
    """
    Normalize and validate a domain name.
    """

    domain = domain.strip().lower()

    if not domain.startswith(("http://", "https://")):
        domain = "https://" + domain

    parsed = urlparse(domain)

    if "." not in parsed.netloc:
        return None

    return parsed.netloc