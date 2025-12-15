from __future__ import annotations

from dataclasses import dataclass

import streamlit as st


@dataclass(frozen=True)
class Kpi:
    title: str
    value: str
    subtitle: str = ""


def render_kpi_card(kpi: Kpi) -> None:
    st.markdown(
        f"""
        <div class="kpi-card fade-in">
          <div class="kpi-title">{kpi.title}</div>
          <div class="kpi-value">{kpi.value}</div>
          <div class="kpi-sub">{kpi.subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_title(text: str) -> None:
    st.markdown(f'<div class="section-title">{text}</div>', unsafe_allow_html=True)
