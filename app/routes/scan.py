from flask import Blueprint, render_template, request

from app.services.validator import validate_domain

from app.services.ssl_checker import check_ssl

from app.services.headers_checker import check_security_headers

from app.services.risk_engine import calculate_score

from app.services.robots_checker import check_robots

from app.services.sitemap_checker import check_sitemap

from datetime import datetime

import time

scan_bp = Blueprint("scan", __name__)


@scan_bp.route("/scan", methods=["POST"])
def scan():

    start = time.time()
    domain = request.form.get("domain", "").strip()

    domain = validate_domain(domain)

    if domain is None:
        return render_template(
            "results.html",
            error="Invalid domain."
        )

    ssl_info = check_ssl(domain)
    headers = check_security_headers(domain)
    risk = calculate_score(
    ssl_info,
    headers
)
    robots = check_robots(domain)
    sitemap = check_sitemap(domain)
    scan_time = datetime.now().strftime("%d %b %Y %I:%M %p")
    duration = round(time.time() - start, 2)
    return render_template(
    "results.html",
    domain=domain,
    ssl=ssl_info,
    headers=headers,
    risk=risk,
    robots=robots,
    sitemap=sitemap,
    scan_time=scan_time,
    duration=duration
)