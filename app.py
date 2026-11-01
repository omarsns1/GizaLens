import streamlit as st
from pathlib import Path
from docx import Document
import re

st.set_page_config(page_title="GizaLens | Arabic Manuscript Lab", page_icon="📜", layout="wide")

ROOT = Path(__file__).parent
DATA_ROOT = ROOT / "data" / "raw" / "Historical Arabic Handwritten Text Recognition Dataset"

st.title("📜 GizaLens")
st.caption("An independent research prototype for turning historical Arabic documents into searchable knowledge.")
st.info(
    "Dataset note: the starter collection contains historical Arabic handwritten material, "
    "but it is not established as Giza excavation diaries. We use it only to prototype "
    "and evaluate handwriting recognition. Giza-specific records will be added separately "
    "from appropriately accessible sources."
)

def normalise_stem(filename: str) -> str:
    stem = Path(filename).stem
    return re.sub(r"_[AB]$", "", stem)

def read_docx(path: Path) -> str:
    try:
        doc = Document(path)
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())
    except Exception:
        return ""

@st.cache_data
def collect_files():
    rows = []
    if not DATA_ROOT.exists():
        return rows
    images = sorted(DATA_ROOT.rglob("*.PNG")) + sorted(DATA_ROOT.rglob("*.png"))
    docs = sorted(DATA_ROOT.rglob("*.docx"))
    doc_index = {}
    for d in docs:
        doc_index.setdefault(normalise_stem(d.name), []).append(d)
    for image in images:
        matches = doc_index.get(normalise_stem(image.name), [])
        transcript = read_docx(matches[0]) if matches else ""
        rows.append({
            "image": image,
            "book": image.parent.name,
            "name": image.name,
            "transcript": transcript,
            "has_transcript": bool(transcript)
        })
    return rows

records = collect_files()
if not records:
    st.error("Dataset not found. Check that the supplied dataset is inside data/raw/.")
    st.stop()

st.sidebar.header("Collection")
books = ["All books"] + sorted({r["book"] for r in records})
book = st.sidebar.selectbox("Filter by folder", books)
filtered = records if book == "All books" else [r for r in records if r["book"] == book]

st.sidebar.metric("Scanned pages", len(records))
st.sidebar.metric("Pages with matched transcript", sum(r["has_transcript"] for r in records))

selected_name = st.selectbox("Choose a manuscript page", [r["name"] for r in filtered])
record = next(r for r in filtered if r["name"] == selected_name)

left, right = st.columns([1.15, 1])
with left:
    st.subheader("Original page")
    st.image(str(record["image"]), width=280)
with right:
    st.subheader("Available transcription")
    if record["has_transcript"]:
        st.text_area("Text extracted from the paired DOCX file", record["transcript"], height=420)
    else:
        st.warning("No transcription file was automatically matched to this image.")
        st.caption("Matching is based on the shared page identifier. Some images may have no separate transcription.")

st.divider()
st.subheader("Dataset overview")
matched = sum(r["has_transcript"] for r in records)
c1, c2, c3 = st.columns(3)
c1.metric("Image files", len(records))
c2.metric("Matched transcriptions", matched)
c3.metric("Without matched transcription", len(records) - matched)

st.caption(
    "This is the first data-inspection interface, not an OCR model yet. "
    "Next we will validate image-to-transcription pairs and establish a clean evaluation set."
)

