from executor import Executor

class MenuItem:
    """This class is responsible for managing single menu items in the database"""

    def __init__(self, name: str, price: int) -> None:       
        self.item_name = name
        self.item_price = price
        self.table_name = 'Menu_Items'

    def save(self):
        """Saves the item to the database"""

        query = f"insert into {self.table_name}(item_name, item_price) values ('{self.item_name}', {self.item_price})"
   
        Executor.run_commit(query)
        return query
    
    def delete(self):
        """Deletes the item from the database"""

        query = f"delete from {self.table_name} where item_name='{self.item_name}' and item_price={self.item_price}"
 
        Executor.run_commit(query)
        return query
    
    def update(self, new_name: str = "", new_price: str = "None"):
        """Updates the item in the database"""

        n_name = new_name if new_name != "" else self.item_name
        n_price = new_price if new_price != "" else self.item_price

        query = f"update {self.table_name} set item_name='{n_name}', item_price={n_price} where "
        query += f"item_name='{self.item_name}' and item_price={self.item_price}"

        Executor.run_commit(query)
        return query
    

if __name__ == '__main__':
    item = MenuItem('Falafel', 5)
    item.save()
    # item.update(new_name='BurgerXL')
    # print(item.update(new_price=15))
    # item.delete()