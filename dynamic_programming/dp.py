def gridTraveler(rows, columns):
    if rows == 0 or columns  == 0:
        return 0
    
    if rows == 1 and columns == 1:
        return 1
    
    return gridTraveler(rows - 1, columns) + gridTraveler(rows, columns - 1)
    
    
print(gridTraveler(4,5))