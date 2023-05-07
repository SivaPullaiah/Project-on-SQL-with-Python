import mysql.connector
conn = mysql.connector.connect(host='localhost',
                               user='root',
                               password='Msiva5717@',
                               )
print("Connection Made Successfully!")

class Inventory:
    def __init___(self):
        pass
        
    def createDatabase():
        sql= f"create database Inventory_Management"
        crsr = conn.cursor()
        crsr.execute(sql)
        conn.commit()
        crsr.close()
        print("Databse is created successfully!")
    
    def useDatabase():
        sql = "use Inventory_Management"
        crsr = conn.cursor()
        crsr.execute(sql)
        crsr.close()
        conn.commit()
        print("Database selected")
        
    def ManufacturerTable():
        sql=f"""create table manufacture(manufacturer_id int primary key,
                manufacturer_name varchar(30) not null,
                email varchar(50),
                phone bigint,
                products_to_manufacture INT DEFAULT 0,
                defective_items INT DEFAULT 0);"""
        crsr = conn.cursor()
        crsr.execute(sql)
        conn.commit()
        crsr.close()
        print("Manufacture Table is created.")
        
    def GoodsTable():
        sql = f"""create table goods(goods_id int primary key,
                good_name varchar(50) not null ,
                manufacturer_id int not null,
                category varchar(20),
                unit_price float not null,
                quantity int not null default 0,
                manufactured_date date,
                color varchar(20),
                foreign key(manufacturer_id) references manufacture(manufacturer_id));
                """
        crsr = conn.cursor()
        crsr.execute(sql)
        conn.commit()
        crsr.close()
        print("Goods Table is created.")
    
    def PurchaseTable():
        sql = f"""create table purchase(purchase_id int primary key,
					goods_id int not null,
                    purchase_date date,
                    purchase_qty int default 0,
                    purchase_price float default 0.0,
                    store_name varchar(50),
                    store_type varchar(50),
                    foreign key(goods_id) references goods(goods_id));
                    """
        crsr = conn.cursor()
        crsr.execute(sql)
        conn.commit()
        crsr.close()
        print("Purchase table is created.")
    
    def SalesTable():
        sql = """create table sales(sale_id int primary key,
					goods_id int not null,
                    sale_price float,
                    sale_date date ,
                    sale_qty int default 0,
                    store_name varchar(50),
                    foreign key(goods_id) references goods(goods_id));
                    """
        crsr = conn.cursor()
        crsr.execute(sql)
        conn.commit()
        crsr.close()
        print("Sales table is created.")
    
    def defectiveItems():
        sql = """create table defectiveItems(def_id int primary key,
					goods_id int not null,
                    manufacturer_id int not null,
                    defect_description varchar(256),
                    foreign key(goods_id) references goods(goods_id),
                    foreign key(manufacturer_id) references manufacture(manufacturer_id));
                    """
        crsr = conn.cursor()
        crsr.execute(sql)
        conn.commit()
        crsr.close()
        print("defectiveItems table is created")
        
    def insertManufactureData():
        # Inserting values into Manufacture table
        msql = f"""INSERT INTO manufacture(manufacturer_id, manufacturer_name, email, phone)
                    VALUES (%s, %s, %s, %s)"""
        values = [
            (1, "SS Export", "john@example.com", 1234567890),
            (2, "ABC Manufacturing", "javid@example.com", 9876543210),
            (3, "XYZ Industries", "anees@example.com", 4567890123)
        ]
        crsr = conn.cursor()
        crsr.executemany(msql,values)
        crsr.close()
        conn.commit()
        
        # Inserting values into good table
    def insertGoodData():
        gsql = f"""INSERT INTO goods (goods_id, good_name, manufacturer_id, category, unit_price, quantity, manufactured_date , color)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        
        values = [
            (1, "Wooden Chair", 1, "Furniture", 50.0, 10, "2023-01-15", "red"),
            (2, "Steel Table", 2, "Furniture", 100.0, 5, "2023-02-10", "blue"),
            (3, "Plastic Shelf", 3, "Storage", 20.0, 8, "2023-03-20", "Green"),
            (4, "shirt", 2, "Clothes", 250.99, 2, "2023-02-16", "black")
        ]
        crsr = conn.cursor()
        crsr.executemany(gsql,values)
        crsr.close()
        conn.commit()
        
        # Inserting values into Purchase table
    def insertPurchaseData():
        psql = f"""INSERT INTO purchase (purchase_id, goods_id, purchase_date, purchase_qty, purchase_price, store_name, store_type)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
        values = [
            (1, 1, "2023-04-05", 5, 200.0, "Store A", "Online"),
            (2, 2, "2023-04-07", 3, 500.0, "Store B", "Offline"),
            (3, 3, "2023-04-10", 2, 150.0, "Store C", "Online")
        ]
        crsr = conn.cursor()
        crsr.executemany(psql,values)
        crsr.close()
        conn.commit()

        # Inserting values into Sales table
    def insertSalesData():
        ssql = f"""INSERT INTO sales (sale_id, goods_id, sale_date, sale_qty, store_name)
                    VALUES (%s, %s, %s, %s, %s);
                    """
        values = [
            (1, 1, "2023-04-15", 3, "Store A"),
            (2, 2, "2023-04-18", 2, "Store B"),
            (3, 3, "2023-04-20", 4, "Store C")
        ]
        crsr = conn.cursor()
        crsr.executemany(ssql,values)
        crsr.close()
        conn.commit()
        
        # Inserting values into defectiveItmes table
    def insertDefectiveData():
        dsql = f"""INSERT INTO defectiveItems (def_id, goods_id, manufacturer_id, defect_description)
                    VALUES (%s, %s, %s, %s);
                    """
        values = [
            (1, 1, 1, "Cracked leg"),
            (2, 2, 2, "Faulty welding"),
            (3, 3, 3, "Scratched surface")
        ]
        crsr = conn.cursor()
        crsr.executemany(dsql,values)
        crsr.close()
        conn.commit()
        
        print("Data has been inserted into all tables successfully!")
    
    def query3():
        """In the “manufacture” table, one should be able to see all the products that need to be manufactured, 
        and defective items during the manufacture with different entries like manufacture id, number of items required, etc."""
        
        sql = f"""SELECT manufacturer_id, manufacturer_name, products_to_manufacture, defective_items
                    FROM manufacture;"""
        crsr = conn.cursor()
        crsr.execute(sql)
        values = crsr.fetchall()
        print("Manufacturer_id | manufacture_name | products_to_mnufacture | defective_itmes ")
        for value in values:
            print(*value)
        crsr.close()
        conn.commit()
    
    def deleteDefectiveItems():
        sql = f"""DELETE FROM purchase p WHERE p.goods_id in (
            select d.goods_id from defectiveItems d)
            AND p.store_name = 'ORay'
            AND p.purchase_date = '2023-04-01'
        """
        crsr = conn.cursor()
        crsr.execute(sql)
        conn.commit()
        crsr.close()
        print("Defective items has been deleted successfully!")
        
    def updateRedColorToys():
        sql = """UPDATE manufacture m
                JOIN goods g ON m.manufacturer_id = g.manufacturer_id
                JOIN purchase p ON g.goods_id = p.goods_id
                SET m.manufacturer_id = 10,
                 m.manufacturer_name = 'Javid',
                 m.email = 'javid@gmail.com',
                 m.phone = 1233211231,
                 m.products_to_manufacture = 4,
                 m.defective_items = 2
             WHERE g.category = 'toy' AND g.color = 'red';
                """
        crsr = conn.cursor()
        crsr.execute(sql)
        conn.commit()
        crsr.close()
        print("Manufacture table has been updated basd on the criteria")
    
    def woodenChair():
        sql = """select g.quantity from goods g
                where g.manufacturer_id in (
                select m.manufacturer_id from manufacture m where g.manufactured_date<'2023-05-01'
                )"""
        crsr = conn.cursor()
        crsr.execute(sql)
        values = crsr.fetchall()
        for value in values:
            print(*value)
        crsr.close()
        
        
    def profitOfWoodenTable():
        sql = """select (s.sale_price - p.purchase_price) as profit from sales s
                join goods on s.goods_id = goods.goods_id
                join purchase p on goods.goods_id = p.goods_id
                join manufacture m on goods.manufacturer_id = m.manufacturer_id
                where goods.good_name = 'wooden table'
                and s.store_name = 'Mycare'
                and m.manufacturer_name = 'SS Export';
        """
        crsr = conn.cursor()
        crsr.execute(sql)
        value = crsr.fetchone()
        profit = value[0] if value else None
        print("Profit margin is : ",profit)
        crsr.close()

if __name__ == '__main__':
    print("----\tMENU\t----\n")
    print("""
          1. Create Database\t \t\t 
          3. Create Manufacture Table \t\t 4. Create Good Table\t
          5. Create Purchase Table\t\t 6. Create Sales Table
          7. Create defectiveItmes Table \t 8. Insert data into Goods Table
          9. Insert data into Purchase Table \t 10. Insert data into Sales Table
          11. Insert data in defective Table\t 12. query3() 
          13. Delete Defective Items\t\t 14. Update red colored toys
          15. Query for wooden chair\t\t 16. Profit of Wooden Table Products
          17. Exit\n""")
    i = Inventory
    ch = 0
    # i.createDatabase()
    i.useDatabase()
    while ch!=17:
        ch = int(input("Enter your choice : "))
        if ch==1:
            i.createDatabase() 
        elif ch==3:
            i.ManufacturerTable()
        elif ch==4:
            i.GoodsTable()
        elif ch==5:
            i.PurchaseTable()
        elif ch==6:
            i.SalesTable() 
        elif ch==7:
            i.defectiveItems()
        elif ch==8:
            i.insertGoodData()
        elif ch==9:
            i.insertPurchaseData()
        elif ch==10:
            i.insertSalesData()
        elif ch==11:
            i.insertDefectiveData()
        elif ch==12:
            i.query3()
        elif ch==13:
            i.deleteDefectiveItems()
        elif ch==14:
            i.updateRedColorToys()
        elif ch==15:
            i.woodenChair()
        elif ch==16:
            i.profitOfWoodenTable()
        elif ch==17:
            break