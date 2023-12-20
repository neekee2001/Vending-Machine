item = [
    {
        'itemId': 0,
        'itemName': 'Chocolate',
        'itemPrice': 10,
    },
    {
        'itemId': 1,
        'itemName': 'Dairy Milk',
        'itemPrice': 3,
    },
    {
        'itemId': 2,
        'itemName': 'Milo',
        'itemPrice': 2,
    },
    {
        'itemId': 3,
        'itemName': '100 Plus',
        'itemPrice': 3,        
    },
    {
        'itemId': 4,
        'itemName': 'Mineral Water',
        'itemPrice': 1,        
    }, 
    {
        'itemId': 5,
        'itemName': 'Super Ring',
        'itemPrice': 3,        
    }, 
    {
        'itemId': 6,
        'itemName': 'Potato Chip',
        'itemPrice': 4,        
    }, 
    {
        'itemId': 7,
        'itemName': 'Lays',
        'itemPrice': 7,        
    }, 
    {
        'itemId': 8,
        'itemName': 'Oat Krunch',
        'itemPrice': 3,        
    },  
    {
        'itemId': 9,
        'itemName': 'Haribo',
        'itemPrice': 4,        
    },
]

availableNotes = {100: 10, 50: 10, 20: 20, 10: 20, 5: 30, 1: 50}
returnNote = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0}

itemToBuy = []
run = True

def main(item, itemToBuy, run):
    while(run):        
        buyItem = int(input("\nEnter the code of the item you wish to buy: "))
        if(0 <= buyItem < len(item)):
            itemToBuy.append(item[buyItem])
        else:
            print("Your item code is invalid.")
        
        needContinue = str(input("Do you want to continue buying? Please type Y if yes, N if no: "))
        if needContinue =='N' or needContinue =='n':
            run = False
            
    totalAmount = calculateSum(itemToBuy)
    print("\nThe total amount you have to pay is RM", totalAmount)
    
    totalAmountPaid = pay(totalAmount)
    totalNeedReturn = totalAmountPaid - totalAmount
    if(totalNeedReturn == 0):
        print("Transaction success! Thank you!")
    else:
        print("\nThe total amount of change needed to return to you is RM",totalNeedReturn)
        
        if(checkHasEnoughNote(totalNeedReturn, availableNotes) == True):
            result = calculateReturn(totalNeedReturn)
            print("\nReturning change: ")
            for note, count in result.items():
                print(f"RM{note} notes: {count}")
        else:
            print("Sorry, not enough notes in the vending machine to return.")
        
        
def calculateSum(itemToBuy):
    sum = 0
    for i in itemToBuy:
        sum += i['itemPrice']
    return sum

def pay(totalAmount):
    totalAmountPaid = 0
    for note in availableNotes:
        count = int(input(f"The amount of note RM{note} you paid: "))
        availableNotes[note] += count
        totalAmountPaid += note * count
    
    while(totalAmountPaid < totalAmount):
        remainingAmount = totalAmount - totalAmountPaid
        print("\nYou still have to pay RM", remainingAmount)
        for note in availableNotes:
            count = int(input(f"The amount of note RM{note} you paid: "))
            availableNotes[note] += count
            totalAmountPaid += note * count
    return totalAmountPaid
    

def checkHasEnoughNote(totalNeedReturn, availableNotes):
    totalAvailable = sum(note * count for note, count in availableNotes.items())
    return totalAvailable >= totalNeedReturn


def calculateReturn(totalNeedReturn):    
    for note in returnNote:
        if(totalNeedReturn >= note):
            count = min(totalNeedReturn // note, availableNotes[note])
            totalNeedReturn -= (count*note)
            returnNote[note] = count
            availableNotes[note] -= count  
    return returnNote
            
print("-------------Vending Machine-------------")
for i in item:
    print(f"Item: {i['itemId']} - {i['itemName']} --- Price: RM{i['itemPrice']} ")
                
main(item, itemToBuy, run)