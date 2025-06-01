import json
import pymysql

db_config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "1103",
    "database": "research"
}

def get_positions_by_id(entry_id):
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            cursor.execute("SELECT data FROM tracker_data WHERE id = %s", (entry_id,))
            result = cursor.fetchone()
            if result:
                raw_json = result[0]
                data = json.loads(raw_json)
                return data.get("positions", [])
    except Exception as e:
        print(f"❌ Fout bij ophalen van data voor ID {entry_id}: {e}")
    finally:
        if 'connection' in locals():
            connection.close()
    return []
