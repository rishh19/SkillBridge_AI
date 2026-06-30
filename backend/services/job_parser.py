def clean_job_description(job_description: str):

    """
    Cleans the raw Job Description.
    """

    job_description = job_description.replace("\r", "\n")

    job_description = "\n".join(
        line.strip()
        for line in job_description.splitlines()
        if line.strip()
    )

    return job_description