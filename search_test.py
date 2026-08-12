import streamlit as st

from streamlit_searchbox import st_searchbox


st.set_page_config(
    page_title="Search Test",
    page_icon="🔎"
)

st.title("🔎 Search Test")


def search_players(keyword):

    players = [
        "Shanto",
        "Rahim",
        "Karim",
        "Tamim",
        "Litton"
    ]

    if not keyword:
        return players

    return [
        player
        for player in players
        if keyword.lower() in player.lower()
    ]


selected = st_searchbox(
    search_function=search_players,
    key="player_search"
)

st.write("Selected:", selected)