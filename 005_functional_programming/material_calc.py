def perimeter(width, height):
    return (width + height) * 2


def area(width, height):
    return width * height


def count_materials(order):
    result = {}
    for key in order:
        result[key] = [perimeter(order[key][0], order[key][1]) * order[key][2],
                       area(order[key][0], order[key][1]) * order[key][2]]
    return result


def count_all_materials(result_dict):
    total_p = 0
    total_a = 0
    for key in result_dict:
        total_p += result_dict[key][0] / 100
        total_a += result_dict[key][1] / 10000
    return [total_p, total_a]


def print_by_type(result_dict):
    for key in result_dict:
        print(f'{key}\nCarpet edge: {result_dict[key][0] / 100} meters\n'
              f'Carpet material: {result_dict[key][1] / 10000} square meters')


def count_cost(edge_price, carpet_price, total_materials):
    total_edge = total_materials[0] *  edge_price
    total_carpet = total_materials[1] * carpet_price
    return [total_edge, total_carpet]


def main():
    while True:
        user_menu = input('Please choose:\n1. Count all materials\n2. Count by product type\n3. Count cost\n0. Exit\n--> ')
        if user_menu == '1':
            materials = count_all_materials(count_materials(carpets))
            print(f'Total edge: {materials[0]}\nTotal carpet: {materials[1]}')
        elif user_menu == '2':
            print_by_type(count_materials(carpets))
        elif user_menu == '3':
            materials = count_cost(3.5, 5, count_all_materials(count_materials(carpets)))
            print(f'Total edge cost: {materials[0]}')
            print(f'Total carpet cost: {materials[1]}')
            print(f'Total cost: {materials[0] + materials[1]} EUR')
        elif user_menu == '0':
            break
        else:
            print('Choice out of range')



carpets = {'small': [60, 60, 15], 'medium': [60, 90, 47], 'large': [90, 90, 20], 'xlarge': [125, 125, 5]}
main()
