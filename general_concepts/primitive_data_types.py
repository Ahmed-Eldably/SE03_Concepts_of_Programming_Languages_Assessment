"""
Prrimitive data types: they arer te building blocks forr data manipulation and contain puurer, simple values of data. 
Python has four primitive variable types:

1. Integers
2. Float
3. String
4. Boolean
"""
# 1. Integers: whole nuumbers from negative to infinity.
total_number_of_pink_floyd_albums = 15
print(type(total_number_of_pink_floyd_albums))

# 2. Floats: floating number points ending with a decimal figure.
led_zeppelin_records_sold = 111.5
print(type(led_zeppelin_records_sold))

# you can apply all sort of mathematical formulas on ints and floats

# 3. Strings: collection of alphapets, words or other characters.
best_band = "Pink Floyd"
second_best_band = "Led Zeppelin"

# concatenation
print("Best rock bands ever are " + best_band + " and " + second_best_band + ".")

# Repeats
print(4 * best_band)

# sclicing
print("A new band called: " + best_band[:4] + " " +  second_best_band[4:])

#. 4. Boolean
print("Pink Floyd" == best_band)
print("Led Zeppelin" == best_band)

# Explicit data type conversion
best_band = "Pink Floyd"
total_number_of_pink_floyd_albums = 15
print(best_band + " has made " + str(total_number_of_pink_floyd_albums) + " Albums")

# References
# 1. https://www.datacamp.com/community/tutorials/data-structures-python#primitive

