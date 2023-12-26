class VendingMachine:
    def __init__(self):
        # MENU ITEMS WITH CODES, PRICES ADN AND CATEGORIES.
        self.menu = {
            'A1': {'name': 'DORITOS', 'price': 3.00, 'category': 'Snacks'},
            'B2': {'name': 'GALAXY', 'price': 3.50, 'category': 'Chocolate'},
            'C3': {'name': 'OMAN CHIPS', 'price': 1.50, 'category': 'Snacks'},
            'D4': {'name': 'REDBULL', 'price': 22.25, 'category': 'Drinks'},
            'E5': {'name': 'BISCUITS', 'price': 2.00, 'category': 'Snacks'},
            'F1': {'name': 'COCA COLA', 'price': 3.00, 'category': 'Drinks'},
            'G2': {'name': 'ICED COFFEE', 'price': 3.50, 'category': 'Drinks'},
            'H3': {'name': 'PRIME', 'price': 20.00, 'category': 'Premium'},
            'I4': {'name': 'WATER', 'price': 1.25, 'category': 'Drinks'},
            'J5': {'name': 'FRESH JUICE', 'price': 2.00, 'category': 'Drinks'},
        }

    def display_menu(self):
        print("""\n █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▄░█ ▄▀█ ░░█ █░█░█ ▄▀█ █▄░█ ▀ █▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀
 ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   █░▀█ █▀█ █▄█ ▀▄▀▄▀ █▀█ █░▀█ ░ ▄█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█
              
█▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀ █
█░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄ ▄""")
        





        for code, item in self.menu.items():
            print(f"{code}: {item['name']} - ${item['price']} ({item['category']})")

# INITIALIZING MONEY IN THE  VENDING MACHINE           

vm = VendingMachine()
vm.display_menu()

count = 1
totalCredit = 0

coinNum = int(input("How many coins would you like to enter: "))

while count <= coinNum:
    coin = float(input("Enter coin: $ "))
    totalCredit += coin
    count += 1

print("You have ${:.2f} in your bank.".format(round(totalCredit, 2)))

finalCredit = round(totalCredit, 2)

item_code = input("𝐷𝑜 𝑦𝑜𝑢 𝑘𝑛𝑜𝑤 𝑜𝑢𝑟 𝑝𝑟𝑖𝑚𝑒 𝑖𝑠 𝑎 𝑐𝑢𝑠𝑡𝑜𝑚𝑒𝑟 𝑓𝑎𝑣𝑜𝑢𝑟𝑖𝑡𝑒? 𝐺𝑖𝑣𝑒 𝑖𝑡 𝑎 𝑡𝑟𝑦....Enter the code for your item:")

while item_code not in vm.menu:
    print("Invalid item code. Please enter a valid code.")
    item_code = input("Enter the code for your item: ")

selected_item = vm.menu[item_code]
finalCredit -= selected_item['price']

#Invalidating the vending machine due to certain circumstances.
if totalCredit < selected_item['price']:
    print("INVALID AMOUNT.THE AMOUNT YOU HAVE INSERTED IS NOT ENOUGH FOR THIS ITEM, PLEASE SELECT ANOTHER ITEM OR INSERT MORE MONEY.YOUR CHANGE WILL BE DISPENSED. PLEASE RUN THE VENDING MACHINE AGAIN. THANK YOU ")
else:
    print(f"{selected_item['name']} DISPENSING, costing ${selected_item['price']:.2f}. ENJOY YOUR {selected_item['name']}.")
    print("Your change of ${:.2f} will be dispensed.".format(finalCredit))
    print("""\n█░█░█ █▀▀   █░█ █▀█ █▀█ █▀▀   █▄█ █▀█ █░█   █▀▀ █▄░█ ░░█ █▀█ █▄█ █▀▀ █▀▄   █▄█ █▀█ █░█ █▀█
▀▄▀▄▀ ██▄   █▀█ █▄█ █▀▀ ██▄   ░█░ █▄█ █▄█   ██▄ █░▀█ █▄█ █▄█ ░█░ ██▄ █▄▀   ░█░ █▄█ █▄█ █▀▄

█▀█ █░█ █▀█ █▀▀ █░█ ▄▀█ █▀ █▀▀ ░   █░█░█ █▀▀   █░░ █▀█ █▀█ █▄▀   █▀▀ █▀█ █▀█ █░█░█ ▄▀█ █▀█ █▀▄   ▀█▀ █▀█
█▀▀ █▄█ █▀▄ █▄▄ █▀█ █▀█ ▄█ ██▄ ▄   ▀▄▀▄▀ ██▄   █▄▄ █▄█ █▄█ █░█   █▀░ █▄█ █▀▄ ▀▄▀▄▀ █▀█ █▀▄ █▄▀   ░█░ █▄█

█▀ █▀▀ █▀█ █░█ █ █▄░█ █▀▀   █▄█ █▀█ █░█   ▄▀█ █▀▀ ▄▀█ █ █▄░█ █
▄█ ██▄ █▀▄ ▀▄▀ █ █░▀█ █▄█   ░█░ █▄█ █▄█   █▀█ █▄█ █▀█ █ █░▀█ ▄""")