import socket
import ssl
from datetime import datetime


def check_ssl(domain: str):
    """
    Check SSL certificate information.
    """

    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as secure_sock:

                cert = secure_sock.getpeercert()

        expiry = datetime.strptime(
            cert["notAfter"],
            "%b %d %H:%M:%S %Y %Z"
        )

        remaining = (expiry - datetime.utcnow()).days

        issuer = dict(x[0] for x in cert["issuer"])

        return {
            "valid": True,
            "issuer": issuer.get("organizationName", "Unknown"),
            "expiry": expiry.strftime("%d %b %Y"),
            "days_remaining": remaining
        }

    except Exception:

        return {
            "valid": False,
            "issuer": "-",
            "expiry": "-",
            "days_remaining": 0
        }