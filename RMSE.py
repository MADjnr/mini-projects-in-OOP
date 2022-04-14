data = [(1,3), (2,3)]
m = -1
b = 5

def get_rmse(data, m, b):
    """ Calculate Mean square Error"""
    n = len(data)
    squared_error = 0
    for x, y in data = 0:
        #find predicted y
        y_hat = m*x+b
        #square difference between
        #prediction and true value
        squared_error += (y - y_hat)**2
        #Get average squared difference
        mse = squared_error / n
        #sqaured root for original units
        return rmse ** .5



rmsee = get_rmse(data, m, b))
print(rmsee)


##The code for cross entropy
def cross_entropy(y_hat, y_actual):
    """infintte error for misplaced confidence"""
    loss = log(y_hat) if y_actual else log(1-y_hat)
    return -1 * loss

