import csv
#6,7,8,9,10
with open('front_end_project\crop_dataset.csv',mode ='r') as file:        
    dataset = list(csv.reader(file))
    domain = ['Organic','Chemical']
    variables = []
    constraints = []
    def calculate_fertilizer(constraints,j,variables):
        c=0
        if j<len(dataset):
            for i in range(len(constraints)):
                if i==4:
                    if dataset[j][10]==constraints[i]:
                        c+=1
                        variables.append([c,dataset[j][11],dataset[j][12]])
                        calculate_fertilizer(constraints,j+1,variables)
                        return variables
                    else:
                        variables.append([c,dataset[j][11],dataset[j][12]])
                        calculate_fertilizer(constraints,j+1,variables)
                        return variables
                else:
                    if abs(float(dataset[j][i+6])-constraints[i])<=1:
                        c+=1
                    else:
                        variables.append([c,dataset[j][11],dataset[j][12]])
                        calculate_fertilizer(constraints,j+1,variables)
                        return variables
        else:
            return variables
    
    # Soil_Nitrogen=35.0
    # Soil_Potassium=27.0
    # Soil_Calcium=15.0
    # Soil_Moisture=64.0
    # Crop='rice'
    # constraints.extend([Soil_Nitrogen,Soil_Potassium,Soil_Calcium,Soil_Moisture,Crop])
    # fertilizer_suggestion=calculate_fertilizer(constraints,1,variables)
    # #print(fertilizer_suggestion)
    # fertilizer_suggestion.sort(reverse=True)
    # print('The suggested fertilizers and its quantities are:')
    # for i in range(3):
    #     print(fertilizer_suggestion[i][1],fertilizer_suggestion[i][2])