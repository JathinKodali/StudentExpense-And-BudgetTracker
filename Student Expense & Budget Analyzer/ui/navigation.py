from __future__ import annotations

from typing import Dict, Tuple

import streamlit as st


def _icon_text(name: str) -> str:
  # Use simple, reliable unicode icons so navigation behaves like in-app buttons
  # (no links that open in a new tab).
  return {
    "home": "🏠",
    "plus": "➕",
    "pie": "📊",
    "trend": "📈",
    "bulb": "💡",
  }.get(name, "•")


def sidebar_nav(
  items: Dict[str, Tuple[str, str]],
  default_label: str,
) -> str:
  """Sidebar navigation that behaves like buttons.

  Implementation uses `st.sidebar.radio` (no hyperlinks), then CSS styles the
  options to look like a vertical button menu.

  items: label -> (icon_name, unused)
  Returns selected label.
  """

  labels = list(items.keys())
  if default_label not in items:
    default_label = labels[0] if labels else ""

  icon_map = {label: _icon_text(icon_name) for label, (icon_name, _) in items.items()}

  selected = st.sidebar.radio(
    "Navigation",
    labels,
    index=(labels.index(default_label) if default_label in labels else 0),
    format_func=lambda label: f"{icon_map.get(label, '')}  {label}",
    label_visibility="collapsed",
  )
  return selected
