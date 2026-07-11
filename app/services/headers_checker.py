import requests


HEADERS_TO_CHECK = {
    "Strict-Transport-Security": "HSTS",
    "Content-Security-Policy": "Content Security Policy",
    "X-Frame-Options": "Clickjacking Protection",
    "X-Content-Type-Options": "MIME Type Protection",
    "Referrer-Policy": "Referrer Policy",
    "Permissions-Policy": "Permissions Policy",
}


def check_security_headers(domain: str):

    try:
        response = requests.get(
            f"https://{domain}",
            timeout=5,
            allow_redirects=True
        )

        results = {}

        for header, description in HEADERS_TO_CHECK.items():

            results[description] = header in response.headers

        return results

    except Exception:

        return {
            description: False
            for description in HEADERS_TO_CHECK.values()
        }