from __future__ import annotations

from typing import Optional


def try_load_lottie(url: str) -> Optional[dict]:
    """Optional Lottie JSON fetcher.

    The app works without Lottie. If requests/streamlit-lottie isn't available,
    or the URL fails, return None.
    """

    try:
        import requests

        response = requests.get(url, timeout=4)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


def render_lottie(animation_json: Optional[dict], height: int = 180) -> None:
    if not animation_json:
        return

    try:
        from streamlit_lottie import st_lottie

        st_lottie(animation_json, height=height, key=f"lottie-{height}")
    except Exception:
        return
