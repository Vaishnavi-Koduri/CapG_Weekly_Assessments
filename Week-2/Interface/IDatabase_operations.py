# 17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`.
#  Implement this in `SQLDatabase` and `NoSQLDatabase`.

from abc import ABC, abstractmethod

class iDatabase_op(ABC):
    @abstractmethod
    def enter(self,number):
        pass
    @abstractmethod
    def insert(self):
        pass
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    def delete(self):
        pass
class SQLDatabase(iDatabase_op):
    def enter(self,number):
        self.number= number
    def insert(self):
        return f"{self.number} is inserted into the SQL DataBase"
    def update(self):
        return f"{self.number} is updated into the SQL DataBase"
    def delete(self):
        return f"{self.number} is updated into the SQL DataBase"

class NoSQLDatabase(iDatabase_op):
    def enter(self,number):
        self.number= number
    def insert(self):
        return f"{self.number} is inserted into the NoSQl DataBase"
    def update(self):
        return f"{self.number} is updated into the NoSQL DataBase"
    def delete(self):
        return f"{self.number} is updated into the NoSQL DataBase"
    
sql1= SQLDatabase()
print(sql1.enter(4))
print(sql1.insert())
print(sql1.update())
print(sql1.delete())

sql2= NoSQLDatabase()
print(sql2.enter(9))
print(sql2.insert())
print(sql2.update())
print(sql2.delete())