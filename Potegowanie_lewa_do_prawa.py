def change2binar(the_number) -> int:
    num_of_need = the_number
    binar_code = []
    while(num_of_need != 0):
        binar_code.append(num_of_need%2)
        num_of_need = int(num_of_need/2)
    return binar_code[::-1]

base_num = int(input('Write the the base note: '))

index_num = int(input('Write the number powering: '))
bin_num_index = change2binar(index_num)[::-1]

#powering function
end_num = 1
base = base_num

for i in range(len(bin_num_index)):
    if(bin_num_index[i] == 1):
        end_num *= base
    base *= base

#changing list of ints to list of strings
for i in range(len(bin_num_index)):
    bin_num_index[i] = str(bin_num_index[i])
#end note
print(base_num, '^',''.join(bin_num_index), '=', end_num)
