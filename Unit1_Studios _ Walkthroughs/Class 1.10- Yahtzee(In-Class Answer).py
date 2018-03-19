from test import testEqual

def average_sales(daily_sales):
    #How many WEEKS (sublists) do we have
    weeks = len(daily_sales)
    result = []

    #for each week's data
    for i in range(weeks):

        #accumlator pattern for the DAYS
        weekly_sum = 0

        for day in daily_sales[i]:
            weekly_sum += day

        #divide by the number of days to get average
        weekly_avg = weekly_sum / len(daily_sales[i])

        #add the computed average to the list
        result.append(weekly_avg)
    
    return result


sales = [[1, 1, 1, 1, 1, 1, 1],
    [1, 0, 2, 0, 2, 1, 1]]

testEqual(average_sales(sales), [1, 1])
