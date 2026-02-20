# 📝 Python Command-Line To-Do App

A simple yet powerful command-line interface (CLI) based to-do application built with Python. This tool helps users manage their daily tasks efficiently by allowing them to add, view, and delete tasks using real-time timestamps.

## ✨ Features
- **Task Creation:** Add tasks with specific duration.
- **Real-time Timestamp:** Automatically records the exact time (`HH:MM AM/PM`) when a task is updated.
- **Persistent Storage:** Saves all tasks to a `task.txt` file, so that your data is not lost when you close the program.
- **Smart Deletion:** View all tasks with index number and easily delete any specific task.
- **Error Handling:**
- Prevents crashes from empty input.
- Handles `FileNotFoundError` if the task file does not exist.
- Validates numeric input for menu selection and deletion.
- **Encoding Support:** Uses `utf-8` to ensure compatibility with different languages ​​and symbols.

## 🛠️ Technologies Used
- **Python 3.x**
- **Modules:**
- `datetime`: To generate accurate timestamps.
- `time`: To improve user experience (UX) with delays.

## 🚀 How to Run
1. **Clone the repository:**
``bash
git clone https://github.com
