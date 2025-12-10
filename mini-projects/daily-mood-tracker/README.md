# Daily Mood Tracker

A simple Python console app where I can log my mood each day and view basic stats.  
This project helps me practice file handling, parsing data, and building a small menu-driven program.

## Features
- Log your daily mood (with an optional 1–5 mood rating)
- Saves all entries to `mood_log.txt`
- View stats:
  - Total days logged
  - Most common mood
  - Last 5 logged moods
- Works entirely in the terminal

## How It Works
Each mood entry is stored on a new line in:

YYYY-MM-DD, mood, rating

When viewing stats, the app reads and analyzes these entries to show simple insights.

## How to Run

```bash
python daily_mood_tracker.py

