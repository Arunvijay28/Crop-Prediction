import csv


with open('front_end_project\crop_dataset.csv',mode ='r') as file:        
    dataset = list(csv.reader(file))
    domain = ['wheat', 'rice', 'barley', 'maize', 'tomato', 'potato', 'onion', 'groundnut', 'millets', 'coffee']
    variables = []
    constraints = []
    def calculate_best_crop(constraints,j,variables):
        c = 0
        if j<len(dataset):
            for i in range(len(constraints)):
                if i==0:
                    if constraints[i]==dataset[j][4]:
                        c+=1
                    else:
                        variables.append([c,dataset[j][10],dataset[j][16],dataset[j][17],dataset[j][18],dataset[j][19]])
                        calculate_best_crop(constraints,j+1,variables)
                        return variables
                elif i==5:
                    if constraints[i]==dataset[j][13]:
                        c+=1
                    else:
                        variables.append([c,dataset[j][10],dataset[j][16],dataset[j][17],dataset[j][18],dataset[j][19]])
                        calculate_best_crop(constraints,j+1,variables)
                        return variables
                elif i==7:
                    if constraints[i]==dataset[j][15]:
                        c+=1
                        variables.append([c,dataset[j][10],dataset[j][16],dataset[j][17],dataset[j][18],dataset[j][19]])
                        calculate_best_crop(constraints,j+1,variables)
                        return variables
                    else:
                        variables.append([c,dataset[j][10],dataset[j][16],dataset[j][17],dataset[j][18],dataset[j][19]])
                        calculate_best_crop(constraints,j+1,variables)
                        return variables
                
                elif i==4:
                    if abs(constraints[i]-float(dataset[j][5]))<=2:
                        c+=1
                    else:
                        variables.append([c,dataset[j][10],dataset[j][16],dataset[j][17],dataset[j][18],dataset[j][19]])
                        calculate_best_crop(constraints,j+1,variables)
                        return variables
                elif i==6:
                    if abs(constraints[i]-float(dataset[j][14]))<=2:
                        c+=1
                    else:
                        variables.append([c,dataset[j][10],dataset[j][16],dataset[j][17],dataset[j][18],dataset[j][19]])
                        calculate_best_crop(constraints,j+1,variables)
                        return variables
                elif i==1:
                    if abs(constraints[i]-float(dataset[j][1]))<=2:
                        c+=1
                    else:
                        variables.append([c,dataset[j][10],dataset[j][16],dataset[j][17],dataset[j][18],dataset[j][19]])
                        calculate_best_crop(constraints,j+1,variables)
                        return variables
                elif i==2:
                    if abs(constraints[i]-float(dataset[j][0]))<=2:
                        c+=1
                    else:
                        variables.append([c,dataset[j][10],dataset[j][16],dataset[j][17],dataset[j][18],dataset[j][19]])
                        calculate_best_crop(constraints,j+1,variables)
                        return variables
                else:
                    if abs(constraints[i]-float(dataset[j][2]))<=2:
                        c+=1
                    else:
                        variables.append([c,dataset[j][10],dataset[j][16],dataset[j][17],dataset[j][18],dataset[j][19]])
                        calculate_best_crop(constraints,j+1,variables)
                        return variables
        else:
            return variables
         
    # Average_Temperature = float(input('enter the average temperature:'))
    # Precipitation = float(input('enter the precipitation amount:'))
    # Humidity = float(input('enter the humidity level:'))
    # Wind_Speed= float(input('enter the wind speed:'))
    # Soil_Type= input('enter the soil type:')
    # Soil_pH= float(input('enter the soil ph:'))
    # Soil_Nitrogen= float(input('enter the nitrogen content in the soil:'))
    # Soil_Potassium= float(input('enter the potassium content in the soil:'))
    # Soil_Calcium= float(input('enter the calcium amount in the soil:'))
    # Soil_Moisture= float(input('enter the soil moisture level:'))
    # Variety= input('enter the crop type:')
    # Fertilizer_Type= input('enter the fertilizer type:')
    # Fertilizer_Quantity= float(input('enter the fertilizer quantity:'))
    # Irrigation_Type= input('enter the irrigation type:')
    # Irrigation_Frequency= float(input('enter the irrigation frequency:'))
    # Location= input('enter the location:')

    # Average_Temperature=34.0
    # Precipitation=97.0
    # Humidity=76.0
    # Soil_Type='Clay'
    # Soil_pH=6.0
    # Irrigation_Type='Sprinkler'
    # Irrigation_Frequency=4.0
    # Location='Rajasthan'

    # constraints.extend([Soil_Type,Precipitation,Average_Temperature,Humidity,Soil_pH,Irrigation_Type,Irrigation_Frequency,Location])
    # crop_rank = calculate_best_crop(constraints,1,variables)
    # crop_rank.sort(reverse=True)

    # print(crop_rank)
    # print("The crops which are best suitable for growing in the land is in the order of:")
    # s='                      '
    # print("RANK"+(" "*(len(s)-4))+'CROP'+' '*(len(s)-4)+'YIELD'+' '*(len(s)-5)+'QUANTITY'+' '*(len(s)-8)+'COST OF PRODUCTION'+' '*(len(s)-18)+"MARKET PRICE")
    # for i in range(3):
    #     print(str(i+1)+' '*(len(s)-1)+crop_rank[i][1]+' '*(len(s)-len(crop_rank[i][1]))+crop_rank[i][2]+' '*(len(s)-len(crop_rank[i][2]))+crop_rank[i][3]+' '*(len(s)-len(crop_rank[i][3]))+crop_rank[i][4]+' '*(len(s)-len(crop_rank[i][4]))+crop_rank[i][5]+' '*(len(s)-len(crop_rank[i][5])))
