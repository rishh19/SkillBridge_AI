import re


ROLE_KEYWORDS = [
    "intern",
    "engineer",
    "developer",
    "analyst",
    "scientist",
    "consultant",
    "associate",
    "specialist",
    "research",
    "manager",
    "lead",
    "architect",
    "administrator",
    "designer",
    "tester",
    "sde",
]


DATE_PATTERN = re.compile(
    r"(20\d{2}|19\d{2}|present|current|remote|jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)",
    re.IGNORECASE,
)


def is_role(line: str):

    lower = line.lower()

    return any(keyword in lower for keyword in ROLE_KEYWORDS)


def extract_experience(experience_text: str):

    experiences = []

    if not experience_text.strip():
        return experiences

    lines = [

        line.strip()

        for line in experience_text.splitlines()

        if line.strip()

    ]

    current = None

    for line in lines:

        if is_role(line):

            if current:
                experiences.append(current)

            current = {

                "position": line,

                "duration": "",

                "description": []

            }

            continue

        if current and DATE_PATTERN.search(line):

            if current["duration"] == "":
                current["duration"] = line
            else:
                current["description"].append(line)

            continue

        if current:

            current["description"].append(line)

    if current:

        experiences.append(current)

    return experiences