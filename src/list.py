int_list = [1,2,3,4,5,6,7,8,9,10]

# lc = [FORMATTING  COLLECTION   CONDITION]
# lc = [MAP         COLLECTION   FILTER]

# Add 3 to each number
add_3 = [(i+3)         for i in int_list]

add_3_to_odds_list = [(i+3)     for i in int_list     if i % 2 == 1]

make_even_string_list = [str(i)     for i in int_list     if i % 2 == 1]