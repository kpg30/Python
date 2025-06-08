import json
import logging

# logger = logging.getLogger()
# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.INFO)


# TABLES_TO_RUN = {
#     "l1_pd_test": "l1_pc_test"
# }

TABLES_TO_RUN = {
    "l1_pd_test": "l1_pc_test",
    "l1_pd1_test": "l1_pc1_test"
}

database=["abc","bcv"]


# try:
#     table_dict = json.dumps(TABLES_TO_RUN)
#     print(f"table_dict is {table_dict}")
# except Exception as e:
#     print("there is some issue while parsing table", e)


def func_test1(table_to_validate, db):
    values = list(table_to_validate.values())
    print(f"values : {values}")
    for db_name in db:
        return db_name


    #print(f"a : {a}")
    print("-------------------------")
    for table in values:
        func_test2(table, db)


def func_test2(input_tables, db):
    print(f"input table is :  {input_tables}")
    print(f"value {db}")


func_test1(TABLES_TO_RUN, database)

# if __name__ == '__main__':
#     logging.basicConfig(level=logging.INFO)
#     func_test1(TABLES_TO_RUN)


self.name = "prasad"


