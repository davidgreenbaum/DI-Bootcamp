from executor import Executor

class MenuManager:
    """This class is responsible for managing the menu items in the database"""

    def __init__(self) -> None:
        self.table_name = 'Menu_Items'

    def all(self):
        """Returns all the items in the menu"""
        query = f"select * from {self.table_name}"
        out = Executor.run_fetch(query)
        return out
    
    def get_by_name(self, name: str):
        """Returns the item with the given name, or None if not found"""
        query = f"SELECT * FROM {self.table_name} WHERE item_name = %s"
        out = Executor.run_fetch(query, params=(name,), many=False)
    
        if out:
            item_id, item_name, item_price = out
            return MenuItem(item_name, item_price)
        else:
            return None # if item isnt found

    

if __name__ == '__main__':
    manage = MenuManager()
    # print(manage.all())
    # print(manage.get_by_name('BurgerXL'))
    
    
    @classmethod
    def all_items(cls):
        """Returns a list of all items in the menu"""
        query = f"SELECT * FROM {cls.table_name}"
        out = Executor.run_fetch(query)
        return out