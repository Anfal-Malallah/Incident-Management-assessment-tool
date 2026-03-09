##Test
def assess_incident_management(score):
    if score >= 80:
        return "High maturity"
    elif score >= 50:
        return "Moderate maturity"
    else:
        return "Low maturity"


organization_score = 65
result = assess_incident_management(organization_score)

print("Assessment Result:", result)
