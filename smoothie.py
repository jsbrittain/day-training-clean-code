def smoothie(apples=0, bananas=0, oranges=0):
    """Makes a smoothie with the given ingredients.

    Params:
        apples:  The number of apples.
        bananas: The number of bananas.
        oranges: The number of oranges.

    Returns:
        A list representing the total number of fruits used, and the name of each
        fruit in descending order of quantity.
    """
    fruits = [('apples', apples), ('bananas', bananas), ('oranges', oranges)]
    fruits.sort(key=lambda x: x[1], reverse=True)
    return [sum(x[1] for x in fruits), *[x[0] for x in fruits if x[1] > 0]]
