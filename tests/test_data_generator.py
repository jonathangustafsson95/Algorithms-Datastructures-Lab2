from data import data_generator

num_elements = 10
swap_elements = 2

data1 = data_generator.generate_random_data(num_elements)
data2 = data_generator.generate_sorted_data(num_elements)
data3 = data_generator.generate_reversed_sorted_data(num_elements)
data4 = data_generator.generate_almost_sorted_data(num_elements, swap_elements)
print("random data: %s" % (data1))
print("random sorted: %s" % (data2))
print("random unsorted: %s" % (data3))
print("random almost sorted: %s" % (data4))

