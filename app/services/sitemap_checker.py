import requests


def check_sitemap(domain):

    try:

        response = requests.get(
            f"https://{domain}/sitemap.xml",
            timeout=5
        )

        return response.status_code == 200

    except Exception:

        return False