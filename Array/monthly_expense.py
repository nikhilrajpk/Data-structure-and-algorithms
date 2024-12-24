def compare(expense,month,from_which):
    extra = expense[month] - expense[from_which]
    return extra

def total_quarter(expense):
    total = 0
    for i in range(3):
        total += expense[i]
    return total

def finding(expense,price):
    start = 0
    end = len(expense)-1
    while start<=end:
        mid = start + ((end-start)//2)
        if expense[mid] == price:
            return mid
        elif price < expense[mid]:
            end = mid-1
        else:
            start = mid +1 
    return 'No month found'

def adding_new(expense,price):
    expense.append(price)
    return expense

def corrections(expense,month,refund):
    expense[month] = expense[month] + refund
    return expense

expense = [2200,2350,2600,2130,2190]
print('extra:',compare(expense,1,0))
print('total in quarter:',total_quarter(expense))
print('month with expense 2000 : ',finding(expense,2000))
print(adding_new(expense,1980))
print(corrections(expense,3,200))