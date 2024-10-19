import sqlite3


# Initialize the authentication database
def init_auth_db():
    """
    Initialize the authentication database by creating necessary tables if they don't exist.
    Tables created:
    1. users: Stores user information (id, username, password)
    2. medicine_schedule: Stores medicine schedules for users
    3. reminders: Stores reminders for users' medicine schedules
    """
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS medicine_schedule (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            medicine_name TEXT,
            morning BOOLEAN,
            afternoon BOOLEAN,
            night BOOLEAN,
            dosage INTEGER,  -- New dosage column
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            medicine_name TEXT,
            reminder_time TEXT,
            dosage INTEGER,  -- New dosage column
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    conn.commit()
    conn.close()


# User registration
def register_user(username, password):
    """
    Register a new user in the database.
    
    Args:
    username (str): The username for the new user
    password (str): The password for the new user
    
    Returns:
    bool: True if registration is successful, False if the username already exists
    """
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                  (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


# User login
def login_user(username, password):
    """
    Authenticate a user's login credentials.
    
    Args:
    username (str): The username of the user trying to log in
    password (str): The password of the user trying to log in
    
    Returns:
    tuple: User data if authentication is successful, None otherwise
    """
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?',
              (username, password))
    user = c.fetchone()
    conn.close()
    return user


# Store medicine schedule
def store_medicine_schedule(user, medicine_schedule):
    """
    Store a new medicine schedule for a user.
    
    Args:
    user (tuple): User data tuple containing user ID at index 0
    medicine_schedule (dict): Dictionary containing medicine schedule details
    """
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('INSERT INTO medicine_schedule (user_id, medicine_name, morning, afternoon, night, dosage) VALUES (?, ?, ?, ?, ?, ?)',
              (user[0], medicine_schedule['medicine_name'], medicine_schedule['morning'], medicine_schedule['afternoon'], medicine_schedule['night'], medicine_schedule['dosage']))
    conn.commit()
    conn.close()


# Retrieve medicine schedule
def get_medicine_schedule(user):
    """
    Retrieve all medicine schedules for a user.
    
    Args:
    user (tuple): User data tuple containing user ID at index 0
    
    Returns:
    list: List of dictionaries containing medicine schedule details
    """
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('SELECT * FROM medicine_schedule WHERE user_id = ?', (user[0],))
    schedules = c.fetchall()
    conn.close()
    return [{'medicine_name': item[2], 'morning': item[3], 'afternoon': item[4], 'night': item[5], 'dosage': item[6]} for item in schedules]


# Store reminder
def store_reminder(user, medicine_name, reminder_time, dosage):
    """
    Store a new reminder for a user's medicine schedule.
    
    Args:
    user (tuple): User data tuple containing user ID at index 0
    medicine_name (str): Name of the medicine
    reminder_time (str): Time for the reminder
    dosage (int): Dosage of the medicine
    """
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('INSERT INTO reminders (user_id, medicine_name, reminder_time, dosage) VALUES (?, ?, ?, ?)',
              (user[0], medicine_name, reminder_time, dosage))
    conn.commit()
    conn.close()


# Retrieve reminders
def get_reminders(user):
    """
    Retrieve all reminders for a user.
    
    Args:
    user (tuple): User data tuple containing user ID at index 0
    
    Returns:
    list: List of tuples containing reminder details
    """
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('SELECT * FROM reminders WHERE user_id = ?', (user[0],))
    reminders = c.fetchall()
    conn.close()
    return reminders


# Delete medicine schedule
def delete_medicine_schedule(user, medicine_name):
    """
    Delete a medicine schedule for a user.
    
    Args:
    user (tuple): User data tuple containing user ID at index 0
    medicine_name (str): Name of the medicine to be deleted
    """
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('DELETE FROM medicine_schedule WHERE user_id = ? AND medicine_name = ?',
              (user[0], medicine_name))
    conn.commit()
    conn.close()


# Delete reminder
def delete_reminder(user, medicine_name):
    """
    Delete a reminder for a user.
    
    Args:
    user (tuple): User data tuple containing user ID at index 0
    medicine_name (str): Name of the medicine for which the reminder is to be deleted
    """
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('DELETE FROM reminders WHERE user_id = ? AND medicine_name = ?',
              (user[0], medicine_name))
    conn.commit()
    conn.close()


# Update medicine schedule
def update_medicine_schedule(user, old_name, new_schedule):
    """
    Update an existing medicine schedule for a user.
    
    Args:
    user (tuple): User data tuple containing user ID at index 0
    old_name (str): Current name of the medicine
    new_schedule (dict): Dictionary containing updated medicine schedule details
    """
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('UPDATE medicine_schedule SET medicine_name = ?, morning = ?, afternoon = ?, night = ?, dosage = ? WHERE user_id = ? AND medicine_name = ?',
              (new_schedule['medicine_name'], new_schedule['morning'], new_schedule['afternoon'], new_schedule['night'], new_schedule['dosage'], user[0], old_name))
    conn.commit()
    conn.close()


# Update reminder
def update_reminder(user, medicine_name, new_time):
    """
    Update the reminder time for a specific medicine and user.
    
    Args:
    user (tuple): User data tuple containing user ID at index 0
    medicine_name (str): Name of the medicine
    new_time (str): Updated reminder time
    """
    conn = sqlite3.connect('auth.db')
    c = conn.cursor()
    c.execute('UPDATE reminders SET reminder_time = ? WHERE user_id = ? AND medicine_name = ?',
              (new_time, user[0], medicine_name))
    conn.commit()
    conn.close()
