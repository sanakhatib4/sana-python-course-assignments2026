# Zodiac Profile Calculator

This application generates a user's zodiac profile, including their Sun Sign, Moon Sign, and Rising Sign, based on their birth date, time, and location. The application features a graphical user interface (GUI) for user interaction.

## Installation Instructions

To run this project, you need to install the required dependencies. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sanakhatib4/sana-python-course-assignments2026.git
   cd sana-python-course-assignments2026/day03
   ```

2. **Set Up a Python Environment**:
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   source venv/bin/activate   # On macOS/Linux
   ```

3. **Install Dependencies**:
   Install the required Python packages using:
   ```bash
   pip install -r requirements.txt
   ```
  
5. **Run the Application**:
   ```bash
   python zodiac_generator.py
   ```

## How AI Helped in This Project

I used ChatGPT-4o to do the following:

1. **Separate Business Logic from GUI Code**:
   - The original `zodiac_generator.py` file contained both the business logic and the GUI code.
   - AI suggested and implemented the separation of concerns by moving the business logic into a new file, `zodiac_logic.py`, and updating `zodiac_generator.py` to import and use these functions.

2. **Summarize the Process**:
   - AI helped me summarize the process that led to the final result in this README.




