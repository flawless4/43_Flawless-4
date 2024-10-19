# Medicine Reminder
---
## Overview

Medicine Reminder is a comprehensive application designed to help users manage their medication schedules effectively. It utilizes advanced technologies such as natural language processing, text-to-speech, and speech recognition to provide a user-friendly experience for setting up and managing medicine reminders.

---

## Features

- User Authentication: Secure registration and login system
- Medicine Schedule Management: Add, update, and delete medicine schedules
- Reminder System: Set and manage reminders for taking medications
- Voice Interaction: Speech recognition for hands-free operation
- PDF Processing: Extract information from PDF documents
- Data Visualization: Display medicine schedules and reminders using interactive charts

---

## Technologies Used

- Python
- Streamlit: For the web application interface
- LangChain: For natural language processing tasks
- Google Generative AI: Powering the chatbot and language understanding features
- PyTTSx3: For text-to-speech functionality
- Speech Recognition: For voice command processing
- Pandas: For data manipulation and analysis
- Plotly Express: For creating interactive visualizations
- FAISS: For efficient similarity search and clustering of dense vectors
- SQLite: For local database management

---

## Setup and Installation

1. Clone the repository
2. Go to the working directory
  ```bash
   cd medicine-reminder
   ```
3. Create and activate a Python Virtual Environment
   ```bash
   python -m venv .venv
   ```
   For Windows:
   ```bash
   .venv\Scripts\activate
   ```
   For Linux:
   ```bash
   source .venv\bin\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up your environment variables:
6. Create a .env file in the project root
7. Add your Google API key in te `.env` file:
   ```python
   GOOGLE_API_KEY=<your_api_key_here>
   ```

---

## To run the application:
```bash
streamlit run app.py
```

---

## Navigate through the application using the sidebar menu to access different features such as medicine schedule management, reminders, and voice interactions.

---

## Project Demo

[Watch the project demo](project-demo.webm)

<video controls src="https://github.com/yashpotdar-py/medicine-reminder/raw/refs/heads/main/project-demo.mp4" title="Project Demo"></video>
---

## Future Scopes and Experimental Features

1. IoT Integration:
   - Smart pill dispensers connected to the app
   - Wearable devices for real-time health monitoring

2. Emergency Calling System:
   - One-touch emergency call button
   - Automatic alerts to designated emergency contacts

3. Cloud Connection to Family Members:
   - Real-time medication adherence updates for family members
   - Shared calendar for appointments and medication schedules

4. Priority Users:
   - Caregiver accounts with enhanced permissions and monitoring capabilities
   - VIP support for users with complex medical needs

5. Medication Interaction Checker:
   - AI-powered system to detect potential drug interactions

6. Telemedicine Integration:
   - Direct connection to healthcare providers for virtual consultations

7. Augmented Reality (AR) Pill Identification:
   - Use smartphone camera to identify pills and provide information

8. Voice-Activated Smart Home Integration:
   - Control lights, thermostats, etc., via voice commands within the app

9. Personalized Health Insights:
    - AI analysis of medication patterns and health data for customized recommendations

10. Multi-language Support:
    - Voice recognition and interface in multiple languages for diverse elderly populations

11. Simplified User Interface Modes:
    - Extra large buttons and high contrast modes for users with visual impairments

These future scopes and experimental features are designed to enhance the Medicine Reminder application, making it more comprehensive and tailored for elderly users' needs.

---

## Contributing
Contributions to improve Medicine Reminder are welcome. Please feel free to submit pull requests or open issues to discuss potential enhancements.

---

## License
[MIT LICENSE]
