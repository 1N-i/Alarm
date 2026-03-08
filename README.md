# ⏰ Python Alarm Clock

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)
![Library](https://img.shields.io/badge/Library-playsound3-green?style=for-the-badge)

A countdown timer and alarm that uses ANSI escape codes for dynamic screen updates and plays an audio alert when time is up.

## 📋 Summary
- [Technologies](#-technologies)
- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [What I Learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)
- [How to Run](#-how-to-run)

---

## 🛠 Technologies
- **Python 3.x**: Core logic and timing.
- **Playsound3**: For audio playback functionality.
- **Time Module**: Handles the countdown intervals and delays.

## ✨ Features
- **Dynamic UI:** Uses ANSI escape codes (`\035[2J` and `\035[H`) to clear the terminal and refresh the timer in place, providing a clean interface.
- **Precise Calculation:** Converts raw seconds into a formatted `MM:SS` display using integer division and modulo operators.
- **Audio Notification:** Triggers an external `.mp3` file once the countdown reaches zero.

## 📂 Project Architecture
* `alarm.py`: The main script containing the timing loop, screen clearing logic, and audio trigger.
* `alarm.mp3`: The audio file used for the alarm sound.

## 📚 What I Learned
* **Terminal Control:** How to use ANSI codes to manipulate the console cursor and clear the screen without spamming new lines.
* **Time Formatting:** Using floor division (`//`) and modulo (`%`) to transform total seconds into readable time units.
* **External Libraries:** Integrating `playsound3` to handle cross-platform audio execution.

## 🔮 Future Improvements
- [X] User input for custom alarm durations.
- [ ] Support for multiple alarm sounds/choices.
- [ ] A graphical progress bar.

## 🚀 How to Run

1. **Install dependencies:**
   This project requires the `playsound3` library:
   ```bash
   pip install playsound3
