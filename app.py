"""
Legal Limitation Calculator
Based on the First Schedule of the Limitation Act 1908 (Pakistan)

DISCLAIMER: This tool is for reference purposes only and does not constitute
legal advice. Always consult a qualified legal practitioner for professional
guidance. Deadlines may vary based on court orders, condonation, and other
legal factors not captured here.
"""

import streamlit as st
from datetime import datetime, timedelta
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class LimitationEntry:
    days: int
    source: str          # Section / Schedule reference
    notes: str = ""      # Optional clarifying note


# Data based on First Schedule of the Limitation Act, 1908 (Pakistan)
LIMITATION_DATA: dict[str, LimitationEntry] = {
    "Civil Suit (General)": LimitationEntry(
        days=1095,
        source="First Schedule, Article 120",
        notes="3-year residual period applies where no specific article governs.",
    ),
    "First Appeal (Civil)": LimitationEntry(
        days=30,
        source="First Schedule, Article 156",
        notes="Period runs from the date of the decree or order appealed against.",
    ),
    "Civil Revision": LimitationEntry(
        days=90,
        source="First Schedule, Article 163",
        notes="Period runs from the date of the order sought to be revised.",
    ),
    "Criminal Appeal (High Court)": LimitationEntry(
        days=60,
        source="Cr.P.C Section 417 / High Court Rules",
        notes="Period runs from the date of the judgment or order.",
    ),
    "Death Sentence Appeal": LimitationEntry(
        days=7,
        source="Cr.P.C Section 410",
        notes="Extremely short period — certified copy should be obtained immediately.",
    ),
}

MAX_CERTIFIED_COPY_DAYS = 365  # Reasonable upper bound for Sec. 12 exclusion


# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Legal Limitation Calculator",
    page_icon="⚖️",
    layout="centered",
)

st.title("⚖️ Legal Limitation Calculator")
st.write("A reference tool for Pakistani legal practitioners.")

st.warning(
    "**Disclaimer:** This tool is for informational purposes only and does not "
    "constitute legal advice. Consult a qualified lawyer for professional guidance.",
    icon="⚠️",
)

st.divider()


# ---------------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------------

case_type = st.selectbox(
    "Select Case Type",
    options=list(LIMITATION_DATA.keys()),
    help="Case types are drawn from the First Schedule of the Limitation Act, 1908.",
)

entry = LIMITATION_DATA[case_type]

# Show statutory source and notes inline
st.caption(f"📖 Statutory basis: {entry.source}")
if entry.notes:
    st.caption(f"ℹ️ {entry.notes}")

today = datetime.now().date()

start_date = st.date_input(
    "Date of Order / Decree",
    value=today,
    max_value=today,
    help="The date from which the limitation period begins to run.",
)

# Validate: start date should not be in the future (belt-and-suspenders guard)
if start_date > today:
    st.error("The order/decree date cannot be in the future. Please check the date.")
    st.stop()

certified_copy_days = st.number_input(
    "Days taken to obtain certified copies (Section 12 exclusion)",
    min_value=0,
    max_value=MAX_CERTIFIED_COPY_DAYS,
    value=0,
    step=1,
    help=(
        "Under Section 12 of the Limitation Act, time spent obtaining certified "
        "copies of the judgment/decree is excluded from the limitation period."
    ),
)


# ---------------------------------------------------------------------------
# Calculation
# ---------------------------------------------------------------------------

statutory_days = entry.days
total_days = statutory_days + int(certified_copy_days)
final_deadline = start_date + timedelta(days=total_days)
days_left = (final_deadline - today).days


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

st.divider()
st.subheader("Result")

col1, col2, col3 = st.columns(3)
col1.metric("Statutory Period", f"{statutory_days} days")
col2.metric("Certified Copy Exclusion", f"{int(certified_copy_days)} days")
col3.metric("Total Period", f"{total_days} days")

st.subheader(f"📅 Deadline: {final_deadline.strftime('%d %B, %Y')}")

if days_left > 0:
    st.success(f"✅ **{days_left} days remaining.** Action required before the deadline.")
elif days_left == 0:
    st.warning(
        "⚠️ **Today is the deadline.** File immediately — do not delay.",
    )
else:
    st.error(
        f"🚫 **Time-barred.** The deadline passed {abs(days_left)} day(s) ago. "
        "Condonation of delay may be required under Section 5 of the Limitation Act."
    )

st.divider()
st.caption(
    "Based on the Limitation Act, 1908 (Pakistan) — First Schedule. "
    "This tool does not account for court holidays, condonation orders, or "
    "jurisdiction-specific rules. Always verify with the relevant court registry."
)