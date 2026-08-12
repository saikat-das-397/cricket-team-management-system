# cricket-team-management-system# 🏏 Cricket Team Management System

A Python-based Cricket Team Management System built using Object-Oriented Programming, file handling, data parsing, analytics, visualization, PDF reporting, and both desktop and web interfaces.

## 🚀 Features

### Player Management
- Add player
- Update player
- Delete player
- Search player
- Duplicate player validation
- Input validation

### Data Management
- Load player data from `scorecard.txt`
- Save changes to `scorecard.txt`
- Reload scorecard
- Regex-based scorecard parsing

### Analytics
- Total players
- Total runs
- Total balls
- Average runs
- Average strike rate
- Highest scorer
- Best strike rate
- Top 3 players

### Data Visualization
- Runs scored chart
- Strike-rate chart
- Team contribution chart
- Player ranking chart

### Reporting
- PDF team report
- Team summary
- Top performers
- Top 3 players
- Complete player scorecard
- Performance charts

### Interfaces
- Tkinter desktop GUI
- Streamlit web interface

## 🏗️ Architecture

The project follows a layered Object-Oriented architecture.

```text
                    User
                     │
             ┌───────┴────────┐
             │                │
        Tkinter GUI       Streamlit
             │                │
             └───────┬────────┘
                     │
               Application
                     │
       ┌─────────────┼─────────────┐
       │             │             │
     Models       Services      Commands
       │             │             │
       └─────────────┼─────────────┘
                     │
                scorecard.txt




cricket-team-management-system/
│
├── app/
│   └── application.py
│
├── models/
│   ├── player.py
│   ├── batsman.py
│   ├── team.py
│   └── team_report.py
│
├── services/
│   ├── parser.py
│   ├── analytics.py
│   ├── charts.py
│   ├── report.py
│   └── validator.py
│
├── commands/
│   ├── add_player_command.py
│   └── update_player_command.py
│
├── gui/
│   └── main_window.py
│
├── data/
│   └── scorecard.txt
│
├── charts/
│
├── reports/
│
├── streamlit_app.py
├── requirements.txt
└── README.md