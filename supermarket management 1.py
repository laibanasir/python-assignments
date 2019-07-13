#-----------------SUPERMARKET MANAGEMENT SYSTEM--------------------
items = []
while True:
    display = input('Press enter to continue.')
    print('------------------Welcome to the supermarket------------------')
    print('1. View items\n2. Add items for sale\n3. Purchase items\n4. Search items \n5. Edit items\n6. Exit')
    choice = input('Enter the number of your choice : ')

    if choice == '1' :
        print('------------------View Items------------------')
        print('The number of items in the inventory are : ',len(items))
        while len(items) != 0:
            print('Here are all the items available in the supermarket.')
            for item in items:
                for key, value in item.items():
                    print(key, ':', value)
            break

    elif choice == '2' :
        print('------------------Add items------------------')
        print('To add an item fill in the form')
        # while True:
        #     try:
        #         number_items = int(input('Enter the number of items you want to add in the inventory : '))
        #         break
        #     except ValueError:
        #         print('Number of items should only be in digits')
        # for num in range(number_items):
        item = {}
        item['name'] = input('Item name : ')
        while True:
            try:
                item['quantity'] = int(input('Item quantity : '))
                break
            except ValueError:
                print('Quantity should only be in digits')
        while True:
            try:
                item['price'] = int(input('Price $ : '))
                break
            except ValueError:
                print('Price should only be in digits')
        print('Item has been successfully added.')
        items.append(item)

    elif choice == '3' :
        print('------------------purchase items------------------')
        print(items)
        purchase_item = input('which item do you want to purchase? Enter name : ')
        for item in items:
            if purchase_item.lower() == item['name'].lower() :
                if item['quantity'] != 0 :
                    print('Pay ', item['price'] , 'at checkout counter.')
                    item['quantity'] -= 1
                else: 
                    print('item out of stock.')

    elif choice == '4' :
        print('------------------search items------------------')
        find_item = input('Enter the item\'s name to search in inventory : ')
        for item in items:
            if item['name'].lower() == find_item.lower():
                print('The item named ' + find_item + ' is displayed below with its details')
                print(item)
            else:
                print('item not found.')

    elif choice == '5' :
        print('------------------edit items------------------')
        item_name = input('Enter the name of the item that you want to edit : ')
        for item in items:
            if item_name.lower() == item['name'].lower():
                print('Here are the current details of ' + item_name)
                print(item)
                item['name'] = input('Item name : ')
                while True:
                    try:
                        item['quantity'] = int(input('Item quantity : '))
                        break
                    except ValueError:
                        print('Quantity should only be in digits')
                while True:
                    try:
                        item['price'] = int(input('Price $ : '))
                        break
                    except ValueError:
                        print('Price should only be in digits')
                print('Item has been successfully updated.')
                print(item)
            else:
                print('Item not found')
                
    elif choice == '6' :
        print('------------------exited------------------')
        break

    else: 
         print('You entered an invalid option')
