import openai

def generate_followup_email(lead_info):
    prompt = (
        f"Write a warm follow-up email to this lead:\n\n"
        f"Name: {lead_info.get('name')}\n"
        f"Industry: {lead_info.get('industry')}\n"
        f"Location: {lead_info.get('location')}\n"
        f"Email: {lead_info.get('email')}"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()

def generate_report(focus):
    prompt = f"Generate a {focus} report for a plumbing business."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You generate strategic business summaries and reports."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()

def generate_onboarding_quiz(industry):
    prompt = f"Create a list of 5 onboarding questions for a {industry} business looking to improve operations using AI."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip().split("\n")

def simulate_lead_scrape(industry, location):
    return [
        {"name": f"{industry.title()} Co {i+1}", "location": location, "email": f"contact{i+1}@{industry}.com"}
        for i in range(5)
    ]