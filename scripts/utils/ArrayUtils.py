def try_removing_value_in_array(array, value):
    try:
        array.remove(value)
    except ValueError:
        pass