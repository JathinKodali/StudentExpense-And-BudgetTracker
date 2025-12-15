import streamlit as st


APP_CSS = """
<style>
  .block-container { padding-top: 1.2rem; padding-bottom: 2rem; }

  /* Sidebar nav (button-like rows) */
  section[data-testid="stSidebar"] div[role="radiogroup"] label {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 12px 12px;
    border-radius: 12px;
    margin: 4px 0;
    border: 1px solid rgba(0,0,0,0.06);
    background: rgba(0,0,0,0.02);
    transition: background 120ms ease, transform 120ms ease;
  }
  section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: rgba(0,0,0,0.06);
    transform: translateY(-1px);
  }

  /* Hide the default radio circle */
  section[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-child {
    display: none !important;
  }

  /* Selected option highlight (modern browsers) */
  section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
    background: rgba(0,0,0,0.10);
  }

  .kpi-card {
    border-radius: 16px;
    padding: 18px 18px;
    background: rgba(255, 255, 255, 0.7);
    border: 1px solid rgba(0,0,0,0.06);
    box-shadow: 0 10px 24px rgba(0,0,0,0.06);
    backdrop-filter: blur(6px);
  }
  .kpi-title { font-size: 0.85rem; opacity: 0.75; margin-bottom: 6px; }
  .kpi-value { font-size: 1.75rem; font-weight: 750; line-height: 1.2; }
  .kpi-sub { font-size: 0.85rem; opacity: 0.75; margin-top: 6px; }

  .fade-in { animation: fadeInUp 420ms ease-out both; }
  @keyframes fadeInUp {
    from { opacity: 0; transform: translate3d(0, 8px, 0); }
    to   { opacity: 1; transform: translate3d(0, 0, 0); }
  }

  .section-title { font-size: 1.05rem; font-weight: 700; margin: 6px 0 10px; }
</style>
"""


def apply_styles() -> None:
    st.markdown(APP_CSS, unsafe_allow_html=True)
