
import streamlit as st

st.set_page_config(
    page_title="GizaLens",
    page_icon="🏺",
    layout="wide"
)

st.title("🏺 GizaLens")
st.subheader(
    "Turning historical Arabic documents "
    "into searchable knowledge"
)

st.write(
    "An independent digital humanities project "
    "exploring machine learning for historical "
    "Arabic handwriting and archaeological archives."
)

st.sidebar.title("GizaLens")
page = st.sidebar.radio(
    "Navigate",
    [
        "Document Explorer",
        "Add a Document",
        "Research Roadmap",
        "About"
    ]
)

if page == "Document Explorer":
    st.header("Document Explorer")
    st.info(
        "Your manuscript collection will appear here. "
        "Upload a page to begin."
    )

    st.markdown("### Our research goals")
    col1, col2, col3 = st.columns(3)

    col1.metric("Original evidence", "Images")
    col2.metric("Verified text", "Transcriptions")
    col3.metric("Historical links", "Knowledge graph")

elif page == "Add a Document":
    st.header("Upload a manuscript page")

    image = st.file_uploader(
        "Upload an Arabic handwritten page",
        type=["png", "jpg", "jpeg", "tif"]
    )

    if image:
        st.image(image, caption="Original manuscript",
                 use_container_width=True)

        source = st.text_input("Archive / dataset")
        reference = st.text_input("Volume or page reference")
        transcription = st.text_area(
            "Verified Arabic transcription"
        )

        st.caption(
            "This is currently a preview. "
            "Permanent storage and AI recognition "
            "will be implemented in later versions."
        )

elif page == "Research Roadmap":
    st.header("Research Roadmap")

    stages = [
        "Arabic manuscript dataset preparation",
        "Handwriting recognition (HTR)",
        "Historical entity extraction",
        "Relationship extraction",
        "Historical knowledge graph",
        "Evidence-grounded natural-language search"
    ]

    for i, stage in enumerate(stages, 1):
        st.write(f"**{i}.** {stage}")

elif page == "About":
    st.header("About GizaLens")

    st.write(
        "GizaLens investigates how machine learning "
        "can transform handwritten historical records "
        "into searchable, interconnected knowledge."
    )

    st.markdown("### Research question")

    st.write(
        "Can AI digitise historical Arabic documents "
        "while preserving a verifiable connection "
        "to the original archival evidence?"
    )

    st.markdown("### Inspiration")

    st.markdown(
        "- [Harvard Digital Giza](https://giza.fas.harvard.edu/)"
    )
    st.markdown(
        "- [Harvard Quft Archive](https://quft.fas.harvard.edu/)"
    )

    st.caption(
        "Independent student project. Not affiliated "
        "with Harvard University or the MFA."
    )
