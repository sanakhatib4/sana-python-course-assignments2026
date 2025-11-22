# Zodiac Profile Calculator

This project is a Python-based application that calculates a user's zodiac profile, including their Sun Sign, Moon Sign, and Rising Sign, based on their birth date, time, and location. The application features a graphical user interface (GUI) for user interaction.

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
   Install the required Python packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

   If a `requirements.txt` file is not present, manually install the following dependencies:
   ```bash
   pip install tkinter pillow ephem
   ```

4. **Run the Application**:
   ```bash
   python zodiac_generator.py
   ```

## How AI Helped in This Project

AI assistance was used to:

1. **Separate Business Logic from GUI Code**:
   - The original `zodiac_generator.py` file contained both the business logic (e.g., zodiac calculations) and the GUI code.
   - AI suggested and implemented the separation of concerns by moving the business logic into a new file, `zodiac_logic.py`, and updating `zodiac_generator.py` to import and use these functions.

2. **Summarize the Process**:
   - The AI identified the business logic functions (`get_zodiac_sign_from_angle`, `get_moon_sign`, `get_rising_sign`, `get_sun_sign`, `get_sign_description`) and moved them to `zodiac_logic.py`.
   - The GUI code in `zodiac_generator.py` was updated to use the imported functions, ensuring modularity and maintainability.


## Summary of Prompts and Solutions

- **Prompt**: Identify and separate the business logic from the GUI code.
  - **Solution**: Moved all zodiac-related calculations to `zodiac_logic.py` and updated `zodiac_generator.py` to import these functions.

- **Prompt**: Explain how to install dependencies and document the process.
  - **Solution**: Created this README file with detailed installation instructions and a summary of AI's contributions.

