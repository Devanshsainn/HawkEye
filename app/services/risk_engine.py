def calculate_score(ssl_info, headers):

    score = 100

    recommendations = []

    # SSL

    if not ssl_info["valid"]:
        score -= 30
        recommendations.append(
            "Install a valid SSL certificate."
        )

    # Security Headers

    for header, enabled in headers.items():

        if not enabled:
            score -= 8
            recommendations.append(
                f"Enable {header}."
            )

    if score < 0:
        score = 0

    if score >= 90:
        grade = "Excellent"

    elif score >= 75:
        grade = "Good"

    elif score >= 60:
        grade = "Fair"

    else:
        grade = "Poor"

    return {
        "score": score,
        "grade": grade,
        "recommendations": recommendations,
    }