from app.database.connection import get_connection

def save_click(click_id, offer_id, ip_address, user_agent, referer):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO clicks (click_id, offer_id, ip_address, user_agent, referer)
            VALUES (?, ?, ?, ?, ?)
        ''', (click_id, offer_id, ip_address, user_agent, referer))
        conn.commit()
    finally:
        if conn is not None:
            conn.close()