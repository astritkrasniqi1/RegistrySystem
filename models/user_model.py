import bcrypt
from database import get_connection


class UserModel:
    @staticmethod
    def create_user(username, password, email, emri, mbiemri, personal_id):
        conn = get_connection()
        cursor = conn.cursor()

        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        sql = """
            INSERT INTO users (username, emri, mbiemri, password, email, nrpersonal)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (username, emri, mbiemri, hashed_password.decode("utf-8"), email, personal_id))
        conn.commit()
        cursor.close()
        conn.close()


    @staticmethod
    def validate_user(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result:
            stored_password = result[0].encode("utf-8")
            return bcrypt.checkpw(password.encode("utf-8"), stored_password)
        return False
    

    @staticmethod
    def personal_id_exists(nrpersonal):
        conn = get_connection()
        if not conn:
            return False
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users WHERE nrpersonal = %s", (nrpersonal,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result[0] > 0


