import re


def is_project_title(line: str) -> bool:
    """
    Returns True if the line is likely a project title.
    """

    line = line.strip()

    if not line:
        return False

    # Ignore bullet points
    if line.startswith(("•", "-", "*")):
        return False

    # Ignore continuation lines
    if line[0].islower():
        return False

    # Ignore percentages or numeric continuations
    if re.match(r"^[0-9]", line):
        return False
    # Ignore short continuation lines ending with a period
    words = line.split()

    if (
        len(words) <= 3
        and line.endswith(".")
    ):
        return False

    # Ignore common continuation words
    continuation_words = (
        "evaluation",
        "implemented",
        "executed",
        "performed",
        "developed",
        "built",
        "designed",
        "applied",
        "using",
        "through",
        "covered"
    )

    if line.lower().startswith(continuation_words):
        return False

    return True


def extract_projects(project_text: str):

    projects = []

    current_project = None

    description = []

    lines = [
        line.strip()
        for line in project_text.splitlines()
        if line.strip()
    ]

    for line in lines:

        if is_project_title(line):

            if current_project:

                projects.append({
                    "project_name": current_project,
                    "description": " ".join(description)
                })

            current_project = line
            description = []

        else:

            clean_line = line.replace("•", "").strip()

            if clean_line:

                description.append(clean_line)

    if current_project:

        projects.append({
            "project_name": current_project,
            "description": " ".join(description)
        })

    return projects