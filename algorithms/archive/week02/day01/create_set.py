def create_set(base_sets, item) :
    result_set = []

    for s in base_sets :
        print(f"set is {s}")
        new_set = s.copy()
        new_set.append(item)
        print(f"after set is {s}")
        result_set.append(new_set)

    return result_set

def find_all_subsets(v):
    result_set = [[]]   
    for item in v :
        new_set = create_set(result_set, item)
        print(f"new_set is {new_set} , result_set is {result_set} ")
        result_set.extend(new_set)
        print(f"after result_set is {result_set} ")

    return result_set

print(find_all_subsets([1,2]))
print(find_all_subsets([-1,-10,-3,1,2,4]))
