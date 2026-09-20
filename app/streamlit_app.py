import streamlit as st
import requests


st.set_page_config(

    page_title=
        "Azure OpenAI RCA Assistant",

    layout="wide"
)


st.title(
    "Azure OpenAI GenAI RCA & "
    "Application Support Assistant"
)

st.caption(
    "Enterprise application-support "
    "RCA portfolio simulation"
)


api_url = st.sidebar.text_input(

    "FastAPI URL",

    "http://127.0.0.1:8000"
)


incident_id = st.text_input(

    "Incident ID",

    "INC-1001"
)


service = st.text_input(

    "Service",

    "genai-support-assistant"
)


error_code = st.selectbox(

    "Error Code",

    [
        "401",
        "403",
        "404",
        "408",
        "429",
        "500",
        "502",
        "503"
    ]
)


description = st.text_area(

    "Incident Description",

    "Users report intermittent "
    "Azure OpenAI failures during peak traffic."
)


logs = st.text_area(

    "Logs",

    "10:30:01 200\n"
    "10:30:02 200\n"
    "10:30:03 429\n"
    "10:30:04 429\n"
    "10:30:05 429"
)


if st.button("Analyze Incident"):

    payload = {

        "incident_id":
            incident_id,

        "service":
            service,

        "error_code":
            error_code,

        "description":
            description,

        "logs":
            logs.splitlines()
    }

    try:

        response = requests.post(

            f"{api_url}/analyze",

            json=payload,

            timeout=90
        )

        response.raise_for_status()

        result = response.json()

        st.subheader(
            "Incident Classification"
        )

        st.success(
            result["classification"]
        )

        st.subheader(
            "Evidence"
        )

        for evidence in result["evidence"]:

            st.write(
                f"- {evidence}"
            )

        st.subheader(
            "Retrieved Knowledge"
        )

        for document in result[
            "retrieved_knowledge"
        ]:

            st.write(
                f"- {document}"
            )

        st.subheader(
            "RCA"
        )

        st.json(
            result["model_rca"]
        )

    except Exception as error:

        st.error(
            f"Request failed: {error}"
        )
