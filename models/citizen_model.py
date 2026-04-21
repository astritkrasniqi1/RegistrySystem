from database import get_connection



class Citizen:
    def __init__(self, id, personal_id,  emri, mbiemri, email, city):
        self.id = id
        self.personal_id = personal_id
        self.emri = emri
        self.mbiemri = mbiemri
        self.email = email
        self.city = city


class CitizenModel:
    @staticmethod
    def AddCitizen(personal_id, emri, mbiemri, email, city):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO citizens (personal_id, emri, mbiemri, email, city) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (personal_id, emri, mbiemri, email, city))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_citizens(personal_id_filter=None, name_filter=None, city_filter=None):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT id, personal_id, emri, mbiemri, email, city FROM citizens WHERE 1=1"
        params = []

        if personal_id_filter:
            sql += " AND personal_id = %s"
            params.append(personal_id_filter)

        if name_filter:
            sql += " AND emri LIKE %s"
            params.append(f"%{name_filter}%")
        if city_filter:
            sql += " AND city LIKE %s"
            params.append(f"%{city_filter}%")

        cursor.execute(sql, tuple(params))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_citizen_by_id(citizen_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM citizens WHERE id=%s", (citizen_id,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def update_citizen(citizen_id, data):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            UPDATE citizens 
            SET personal_id=%s, emri=%s, mbiemri=%s, email=%s, city=%s 
            WHERE id=%s
        """
        cursor.execute(sql, (
            data['personal_id'],
            data['emri'],
            data['mbiemri'],
            data['email'],
            data['city'],
            citizen_id
        ))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def delete_citizen(citizen_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM citizens WHERE id=%s", (citizen_id,))
        conn.commit()
        cursor.close()
        conn.close()