domain = ["wheat", "rice", "barley"]
variables = []
constraints = []

# dataset la vandhu key crop and value is a list containing the requirements for the crop to grow
# the list contains [minimum temp,max temp,min water level, min ph, max ph,[types of soil it can grow in]]

dataset = {
    "rice": [35, 36, 14, 4, 6, ["clay", "alluvial"]],
    "barley": [31, 37, 17, 8, 10, ["sandy", "saline"]],
    "wheat": [37, 40, 20, 5, 7, ["alluvial", "black"]],
}

i = 0


def calculate_best_crop(soil_type, water, temperature, ph, i, variables):
    c = 0
    if i < 3:
        crop = domain[i]
        if soil_type in dataset[crop][5]:
            c += 1
            if water >= dataset[crop][2]:
                c += 1
                if ph >= dataset[crop][3] and ph <= dataset[crop][4]:
                    c += 1
                    if (
                        temperature >= dataset[crop][0]
                        and temperature <= dataset[crop][1]
                    ):
                        c += 1
                        variables.append([c, crop])
                        # print(variables,"1")
                        calculate_best_crop(
                            soil_type, water, temperature, ph, i + 1, variables
                        )
                        return variables
                    else:
                        variables.append([c, crop])
                        # print(variables,'2')
                        calculate_best_crop(
                            soil_type, water, temperature, ph, i + 1, variables
                        )
                        return variables
                else:
                    variables.append([c, crop])
                    # print(variables,'3')
                    calculate_best_crop(
                        soil_type, water, temperature, ph, i + 1, variables
                    )
                    return variables
            else:
                variables.append([c, crop])
                # print(variables,'4')
                calculate_best_crop(soil_type, water, temperature, ph, i + 1, variables)
                return variables
        else:
            variables.append([c, crop])
            calculate_best_crop(soil_type, water, temperature, ph, i + 1, variables)
            return variables
    else:
        return variables


soil_type = input("enter the type of soil:")
water = int(input("enter the amount of water:"))
temperature = int(input("enter the surrounding temperature:"))
ph = int(input("enter the level of ph of the soil:"))

crop_rank = calculate_best_crop(soil_type, water, temperature, ph, i, variables)
crop_rank.sort(reverse=True)
print("The crops which are best suitable for growing in the land is in the order of:")

for i in crop_rank:
    print(i[1])
