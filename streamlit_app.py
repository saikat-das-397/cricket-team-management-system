import streamlit as st

from app.application import Application
from services.analytics import Analytics


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Cricket Team Management System",
    page_icon="🏏",
    layout="wide"
)


# ==========================================
# Application
# ==========================================

if "app" not in st.session_state:

    application = Application(
        "Bangladesh"
    )

    loaded = application.load()

    if not loaded:
        st.error(
            "Unable to load data/scorecard.txt"
        )
        st.stop()

    st.session_state.app = application

app = st.session_state.app

analytics = Analytics(
    app.get_team()
)

# ==========================================
# Header
# ==========================================

st.title(
    "🏏 Cricket Team Management System"
)

st.caption(
    "Cricket team management, analytics and reporting"
)


# ==========================================
# Get Players
# ==========================================

players = app.get_players()


# ==========================================
# Search
# ==========================================

st.sidebar.header("🔎 Search Players")

search_keyword = st.sidebar.text_input(
    "Player name",
    key="search_player",
)

search_keyword = search_keyword.strip().lower()

if search_keyword:

    filtered_players = [
        player
        for player in players
        if search_keyword in player.get_name().lower()
    ]

else:

    filtered_players = players


# ==========================================
# Team Information
# ==========================================

team = app.get_team()

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Team",
        team.get_team_name()
    )

with col2:

    st.metric(
        "Players",
        len(players)
    )

with col3:

    total_runs = sum(
        player.get_runs()
        for player in players
    )

    st.metric(
        "Total Runs",
        total_runs
    )


# ==========================================
# Add Player
# ==========================================

st.sidebar.header("➕ Add Player")

with st.sidebar.form("add_player_form"):

    name = st.text_input(
        "Player Name"
    )

    runs = st.number_input(
        "Runs",
        min_value=0,
        step=1
    )

    balls = st.number_input(
        "Balls",
        min_value=0,
        step=1
    )

    submitted = st.form_submit_button(
        "Add Player"
    )

    if submitted:

        success, message = app.add_player(
            name,
            runs,
            balls
        )

        if success:

            st.success(message)

            st.rerun()

        else:

            st.error(message)


# ==========================================
# Update Player
# ==========================================

st.sidebar.header("✏️ Update Player")

player_names = [
    player.get_name()
    for player in app.get_players()
]

if player_names:

    selected_name = st.sidebar.selectbox(
        "Select Player",
        player_names,
        key="update_player_select"
    )

    selected_player = app.get_team().search_player(
        selected_name
    )

    if selected_player:

        new_name = st.sidebar.text_input(
            "New Name",
            value=selected_player.get_name(),
            key=f"update_name_{selected_name}"
        )

        new_runs = st.sidebar.number_input(
            "New Runs",
            min_value=0,
            value=selected_player.get_runs(),
            step=1,
            key=f"update_runs_{selected_name}"
        )

        new_balls = st.sidebar.number_input(
            "New Balls",
            min_value=0,
            value=selected_player.get_balls(),
            step=1,
            key=f"update_balls_{selected_name}"
        )

        if st.sidebar.button(
            "Update Player",
            key="update_player_button"
        ):

            success, message = app.update_player(
                selected_name,
                new_name,
                new_runs,
                new_balls
            )

            if success:

                st.success(message)

                st.rerun()

            else:

                st.error(message)


# ==========================================
# Delete Player
# ==========================================

st.sidebar.header("🗑️ Delete Player")

delete_player_names = [
    player.get_name()
    for player in app.get_players()
]

if delete_player_names:

    delete_name = st.sidebar.selectbox(
        "Select Player to Delete",
        delete_player_names,
        key="delete_player_select"
    )

    confirm_delete = st.sidebar.checkbox(
        "I want to delete this player",
        key="confirm_delete"
    )

    if st.sidebar.button(
        "🗑️ Delete Player",
        key="delete_player_button"
    ):

        if not confirm_delete:

            st.warning(
                "Please confirm deletion first."
            )

        else:

            success, message = app.delete_player(
                delete_name
            )

            if success:

                st.success(message)

                st.rerun()

            else:

                st.error(message)

# ==========================================
# Player Table
# ==========================================

st.subheader("Players")

st.caption(
    f"Showing {len(filtered_players)} of {len(players)} players"
)

if filtered_players:

    table_data = [
        player.to_dict()
        for player in filtered_players
    ]

    st.dataframe(
        table_data,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No players found."
    )


# ==========================================
# Analytics Dashboard
# ==========================================

st.header("📊 Team Analytics")

total_players = len(app.get_players())

total_runs = analytics.get_total_runs()

average_runs = analytics.get_average_runs()

average_strike_rate = analytics.get_average_strike_rate()


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Players",
        total_players
    )


with col2:

    st.metric(
        "Total Runs",
        total_runs
    )


with col3:

    st.metric(
        "Average Runs",
        f"{average_runs:.2f}"
    )


with col4:

    st.metric(
        "Average Strike Rate",
        f"{average_strike_rate:.2f}"
    )



# ==========================================
# Performance Charts
# ==========================================

st.header("📊 Performance Analysis")

if len(app.get_players()) > 0:

    if st.button(
        "📊 Generate Performance Charts",
        key="generate_charts"
    ):

        chart_files = app.generate_charts()

        st.session_state.chart_files = chart_files

        st.success(
            "Performance charts generated successfully."
        )

else:

    st.info(
        "No player data available for chart generation."
    )

# ==========================================
# Display Charts
# ==========================================

if "chart_files" in st.session_state:

    chart_files = st.session_state.chart_files

    col1, col2 = st.columns(2)

    with col1:

        if chart_files.get("Runs"):

            st.image(
                chart_files["Runs"],
                caption="Runs Scored",
                use_container_width=True
            )

    with col2:

        if chart_files.get("Strike Rate"):

            st.image(
                chart_files["Strike Rate"],
                caption="Strike Rate",
                use_container_width=True
            )

    col1, col2 = st.columns(2)

    with col1:

        if chart_files.get("Contribution"):

            st.image(
                chart_files["Contribution"],
                caption="Team Run Contribution",
                use_container_width=True
            )

    with col2:

        if chart_files.get("Ranking"):

            st.image(
                chart_files["Ranking"],
                caption="Player Ranking",
                use_container_width=True
            )





# ==========================================
# Player Highlights
# ==========================================

st.subheader("🏆 Player Highlights")

highest_scorer = analytics.get_highest_scorer()

best_strike_rate = analytics.get_best_strike_rate_player()

col1, col2 = st.columns(2)


with col1:

    if highest_scorer:

        st.success(
            f"🏆 Highest Scorer: "
            f"{highest_scorer.get_name()} "
            f"— {highest_scorer.get_runs()} runs"
        )

    else:

        st.info(
            "No player data available."
        )


with col2:

    if best_strike_rate:

        st.success(
            f"⚡ Best Strike Rate: "
            f"{best_strike_rate.get_name()} "
            f"— {best_strike_rate.strike_rate():.2f}"
        )

    else:

        st.info(
            "No player data available."
        )

# ==========================================
# Data Management
# ==========================================

st.sidebar.header("💾 Data Management")

if st.sidebar.button(
    "🔄 Reload Scorecard",
    key="reload_scorecard"
):

    if app.load():

        st.success(
            "Scorecard loaded successfully."
        )

        st.rerun()

    else:

        st.error(
            "Unable to load scorecard."
        )

if st.sidebar.button(
    "💾 Save Changes",
    key="save_changes"
):

    if app.save():

        st.success(
            "Changes saved successfully."
        )

    else:

        st.error(
            "Unable to save scorecard."
        )

# ==========================================
# PDF Report
# ==========================================

st.header("📄 Team Report")

if st.button(
    "📄 Generate PDF Report",
    key="generate_pdf"
):

    try:

        # Generate latest charts
        app.generate_charts()

        # Generate PDF
        pdf_filename = app.generate_pdf()

        st.session_state.pdf_filename = pdf_filename

        st.success(
            "PDF report generated successfully."
        )

    except Exception as e:

        st.error(
            str(e)
        )
        
# ==========================================
# Download PDF
# ==========================================

if "pdf_filename" in st.session_state:

    pdf_filename = st.session_state.pdf_filename

    with open(
        pdf_filename,
        "rb"
    ) as pdf_file:

        st.download_button(
            label="⬇️ Download PDF Report",
            data=pdf_file,
            file_name="Cricket_Team_Report.pdf",
            mime="application/pdf",
            key="download_pdf"
        )
#