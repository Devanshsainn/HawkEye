import requests


def check_robots(domain):

    try:

        response = requests.get(
            f"https://{domain}/robots.txt",
            timeout=5
        )

        return response.status_code == 200

    except Exception:

        return False