import os
import sqlite3	

db_path = "CalorieTracker_DB2.sqlite"


def clear_terminal():
    os.system("cls")


def weight_progress_chart():
    os.system("termgraph user_progress.txt --color [green]")


def calorie_graph(too_many_cals):
    if too_many_cals:
        os.system("termgraph calorie_consumption.txt --color {red,cyan} --stacked --no-values")
    else:
        os.system("termgraph calorie_consumption.txt --color {green,cyan} --stacked --no-values")


def is_new_day(most_recent_row, current_date):
    if most_recent_row < current_date:
        return True
    else:
        return False


def get_calorie_info(food_item):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT Cals_per100grams FROM CalorieDB  WHERE FoodItem = ?", (food_item,))
        calorie_info = int(cursor.fetchall()[0][0].split(" ")[0])
    except:
        calorie_info = "not found"
    connection.close()
    return calorie_info


#print(get_calorie_info("Applesauce"))