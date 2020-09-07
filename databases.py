import mysql.connector

mydb = mysql.connector.connect(host="aws-simplified.cfsozqviv5g2.ap-south-1.rds.amazonaws.com",
                               user="debangshudb",
                               passwd="debangshu1994",
                               database="business")

c = mydb.cursor()

def insert_element(emp):
    sqlformula = "INSERT INTO employee (username,password) VALUES (%s,%s)"
    c.execute(sqlformula, emp)
    mydb.commit()


def delete_element(emp):
    sqlformula = "DELETE FROM employee WHERE username=%s"
    c.execute(sqlformula, (emp,))
    mydb.commit()