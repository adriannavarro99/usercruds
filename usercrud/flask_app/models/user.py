from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.updated_at = data['update_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usercr;"
        results = connectToMySQL('practice').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO usercr (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

        result = connectToMySQL('practice').query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM usercr WHERE id = %(id)s;"
        result = connectToMySQL('practice').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE usercr SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,update_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('practice').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM usercr WHERE id = %(id)s;"
        return connectToMySQL('practice').query_db(query,data)