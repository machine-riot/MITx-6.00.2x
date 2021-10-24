"""
Solving a Knapsack Problem with a Decision Tree
"""
def maxVal(toConsider, avail):
    """
    Assumes toConsider a list of items, avail a weight
    Returns a tuple of the total value of a solution to 0/1 knapsack
    problem and the items of that solution
    """
    if toConsider == [] or avail = 0:
        result = (0, ())
    elif toConsider[0].getUnits() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                avail - nextItem.getUnits())
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Explore better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)

    return result
