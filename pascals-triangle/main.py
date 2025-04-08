def pascals_triangle(level):
    if level == 0:
        return []
    elif level == 1:
        return [[1]]
    else:
        new_row = [1]
        result = triangle(n - 1)
        last_row = result[-1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row += [1]
        result.append(new_row)
    return result


triangle = []
pascals_triangle(3)




# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1

