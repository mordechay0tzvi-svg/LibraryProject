from  database.db_connection import connectionDB
connector = connectionDB()


class MembersDB:
    def  __init__(self):
        connector.create_tables()
    
    def create_member(self, data:dict):
        conn = connector.get_connection()
        cursor = conn.cursor()
        sql = ("insert into members (name, email, is_active, total_borrows) values (%s,%s,%s,%s)")
        values = (data['name'], data['email'], True, 0)
        cursor.execute(sql, values)
        added = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return added
    
    def get_all_members(self):
        conn = connector.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('select * from members')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    
    def get_member_by_id(self, id:int):
        conn = connector.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('select * from members where id = %s',(id,))
        member = cursor.fetchone()
        cursor.close()
        conn.close()
        return member
    
    def update_member(self, id:int, data:dict):
        conn = connector.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('update members set name = %s, email = %s where id = %s',(data['name'], data['email'], id))
        updated = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return updated
    
    def deactivate_member(self, id:int):
        if not self.get_member_by_id(id)['is_active']:
            return {"message":"memeber is already deactive"}
        conn = connector.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('update members set is_active = %s where id = %s',(False , id))
        updated = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return updated
    
    def activate_member(self, id:int):
        if self.get_member_by_id(id)['is_active']:
            return {"message":"memeber is already active"}
        conn = connector.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('update members set is_active = %s where id = %s',(True , id))
        updated = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return updated
    
    def increment_borrows(self, id:int):
        conn = connector.get_connection()
        cursor = conn.cursor()
        cursor.execute('select total_borrows from members where id = %s', (id,))
        total = cursor.fetchone()
        if not total:
            return 0
        total = total[0] + 1
        cursor.execute('update members set total_borrows = %s where id = %s', (total,  id))
        increased = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return increased
    
    def count_active_members(self):
        conn = connector.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('select count(*) as active from members where is_active')
        active = cursor.fetchone()['active']
        cursor.close()
        conn.close()
        return active
    
    def get_top_member(self):
        conn = connector.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('select * from members order by total_borrows desc limit 1')
        top = cursor.fetchone()
        cursor.close()
        conn.close()
        return top
    
     


     












