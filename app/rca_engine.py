import re


def parse_model_output(text):

    sections = {

        "probable_root_cause": "",

        "evidence": [],

        "immediate_actions": [],

        "validation_steps": [],

        "preventive_actions": []
    }

    mapping = {

        "probable root cause":
            "probable_root_cause",

        "evidence":
            "evidence",

        "immediate actions":
            "immediate_actions",

        "validation steps":
            "validation_steps",

        "preventive actions":
            "preventive_actions"
    }

    current_section = None

    for line in text.splitlines():

        clean = line.strip()

        if not clean:
            continue

        normalized = (
            clean
            .strip("#: ")
            .lower()
        )

        matched = None

        for key in mapping:

            if normalized.startswith(key):

                matched = key
                break

        if matched:

            current_section = mapping[matched]
            continue

        if current_section:

            if current_section == "probable_root_cause":

                sections[current_section] += (
                    (" " if sections[current_section] else "")
                    + clean
                )

            else:

                item = re.sub(
                    r"^[\-\*\d\.\s]+",
                    "",
                    clean
                )

                if item:
                    sections[current_section].append(item)

    return sections
