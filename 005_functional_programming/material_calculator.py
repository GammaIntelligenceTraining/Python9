def area(width, height):
    result = width * height
    return result

def perimeter(width, height):
    result = width * 2 + height * 2
    return result

def material_amount(data):
    result_dict = {}
    for key, value in data.items():
        product_area = area(value[0], value[1])
        carpet_material = product_area * value[2] / 100
        product_perimeter = perimeter(value[0], value[1])
        edge_material = product_perimeter * value[2] / 100

        result_dict[key] = [carpet_material, edge_material]
    return result_dict

def print_result(result):
    total_carpet_material = 0
    total_edge_material = 0
    for key, value in result.items():
        print(f'Carpet material for {key}: {value[0]} square meters')
        print(f'Edge material for {key}: {value[1]} meters')
        total_carpet_material += value[0]
        total_edge_material += value[1]
    print()
    print(f'Total carpet material: {total_carpet_material} square meters')
    print(f'Total edge material: {total_edge_material} meters')



product_dict = {'small': [20, 20, 40], 'medium': [40, 60, 35], 'large': [50, 90, 22]}

print_result(material_amount(product_dict))