
"""
Type inference: the system generates consistent type 
                declrations from information implicit in
                the program.
"""
def sum(led_zeppelin_records_sold: int, pink_floyd_records_sold: int) -> int:
    return led_zeppelin_records_sold + pink_floyd_records_sold  # treat as a.__add__(b)

led_zeppelin_records_sold = 111.5
pink_floyd_records_sold = 250

print(sum(led_zeppelin_records_sold, pink_floyd_records_sold))