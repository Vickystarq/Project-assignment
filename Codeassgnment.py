# This is a code for shopping list
shopping_list = ["Apple"]
shopping_list.append("Banana")
shopping_list.append("Bread")
shopping_list.append("Milk")
shopping_list.append("Egg")
print(shopping_list)
#accessing specific item
print(shopping_list[0])
# Using negative index
print(shopping_list[-1])
#Lets change the order to Almond milk
shopping_list[3]= "Almond Milk"
print("My Updated list", shopping_list)
# remove bread
shopping_list.remove("Bread")
print("My new grocery list is",shopping_list)
if "Banana" in shopping_list:
    print("yes i have Banana on my list")
else:
    print("Banana is not on my list")

#End of code
#Rep
