import sqlite3

from globals import DATABASE_URL, QUERY_FILE


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def str_to_list(s_to_cast):
    s_casted = s_to_cast.strip('][').replace("'", "").split(', ')

    return s_casted


class FreshFlowOutput:

    def __init__(self):
        self.sqlite_connection = sqlite3.connect(DATABASE_URL)
        self.sqlite_connection.row_factory = dict_factory
        print("SQLite Connection opened")

    def execute_sql(self):
        result = None

        try:
            cursor = self.sqlite_connection.cursor()
            print("Connected to SQLite successfully")

            with open(QUERY_FILE, 'r') as sqlite_file:
                sql_script = sqlite_file.read()

            cursor.execute(sql_script)
            result = cursor.fetchmany() # debug
            # result = cursor.fetchall()

            cursor.close()

        except sqlite3.Error as error:
            print("Connection error to sqlite", error)

        return result

    def get_output(self):

        result = self.execute_sql()

        # CASTS
        for item in result:
            item['item_categories'] = str_to_list(item['item_categories'])
            item['labels'] = str_to_list(item.pop('tags')) + str_to_list(item.pop('extra_categories'))

            item['case'] = {
                'quantity': item.pop('case_quantity'),
                'unit': item.pop('case_unit')
            }
            item['order'] = {
                'quantity': item.pop('order_quantity'),
                'unit': item.pop('order_unit')
            }
            item['inventory'] = {
                'quantity': item.pop('inventory_quantity'),
                'unit': item.pop('inventory_unit')
            }

        return result

    def __del__(self):
        if self.sqlite_connection:
            self.sqlite_connection.close()
            print("SQLite Connection closed")
