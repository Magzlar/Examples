import csv
from os import remove
import string 
from quantulum3 import parser

def open_file(filename: str)->list:  
    new_list = []
    with open(filename, errors="ignore") as my_file:
        new_file = csv.reader(my_file,delimiter=",")
        for i in new_file:
            new_list.append(i)
    return new_list # Return the new list as a file 

def basic_info(new_list:list)->list:
    awaiting_total = 0
    removed_total = 0 
    approved_total = 0 
    not_cat = 0
    
    new_dict = {}
            
    for i in new_list:
        if i[0] == "id":
            continue
        new_dict[i[3].lower()] = {}
        if i[7].lower() == "awaiting evidence":
            awaiting_total += 1
        elif i[7].lower() == "removed":
            removed_total +=1
        elif i[7].lower() == "validated":
            approved_total +=1
        else:
            not_cat += 1 
            
    total = approved_total +awaiting_total
            
        
    no_companies = len(new_dict.keys())
    calculation = "{: .2f}".format(total/no_companies)
    print()
    print("Basic overiew:")
    print(f"{no_companies} companies are applying for a novel food license")        
    print(f"{removed_total} products have been removed")
    print(f"excluding the {removed_total} removed products, {total} products are appealing to be licensed as a novel food")
    print(f"{awaiting_total} products are awaiting review")
    print(f"{approved_total} prodcuts have been approved")
    print(f"{not_cat} are not able to be catergorised")
    
    
    return new_list


def product_conc(new_list:list)->dict:
    frmt_conc_list = []
    useable_dict = {}
    counter = 0 
    
    
    conc_list = [x[5] for x in new_list] # list comprhension instead of using for loop 
    
    for i in conc_list:
        i.lower()
        if "mg" in i and "ml" in i:
            frmt_conc_list.append(parser.parse(i)) 
        elif "ml" in i and "%" in i:
            frmt_conc_list.append(parser.parse(i))    
        else:
            continue 
    
    for i in frmt_conc_list:
        counter += 1 
        useable_dict[counter] = [] 
        within = useable_dict[counter]
        for e in range(len(i)):
            within.append(i[e].surface)
    
    success_rate_calc = (len(useable_dict)/11765)*100
    success_rate = "{: .2f}".format(success_rate_calc)
            
    print(f"{len(useable_dict)} products have enough information in the 'productSizeVolumeQuantity' and  field to make accurate conclusion on the concentration of the product")
    print(
        f"This could be used as a predictor of succesful applications, which would mean of the 11,765 products the {len(useable_dict)} with accurate 'productSizeVolumeQuantity' are more likley to be successful")
    print(f"Therefore {success_rate}'%' would be the product success rate of applications")
    print("***ALSO COULD USE COMPANY HOUSE DATA TO ASSESS LIKLEHOOD OF SUCCESSFUL APLPICATION BY THE AMOUNT OF FUNDING COMPANIES HAVE***")
    print("*** WEIGHTING USING CAPTIAL, QUALITY OF WEBSITE, PRESENCE OF SCIENTIFIC ADVSIOR")
    print()
    print("Types of cannabinoids:")
    print("9 products contain CBDA alongside CBD")
    print("1 product contains soley CBDA")
    print()
    print("4 products contain CBG alongside CBD")
    print("5 products contain soley CBG")
    print()
    print("2 products contain CBC alongside CBD")
    print("0 products contain soley CBC")
    print()
    print("2 products contain CBN alongside CBD")
    print("1 product contain soley CBN")
    print("Of note CBN is classified as a controlled substance in the UK",flush=True)
    print()
    print("No other phytocannabinoids were used in any products in a novel food application")

            
    return useable_dict

def products_by_company(new_list):
    new_dict1 = {}
    new_dict2 = {}

    
    for i in new_list:
        i[3].lower()
        if i[3] not in new_dict1.keys():
            new_dict1[i[3]] = []
        elif i[3] in new_dict1:
            dict_local = new_dict1[i[3]]
            dict_local.append(1)
        else:
            continue 
        
    for key, value in new_dict1.items():
        new_dict2[key] = len(value)+1
         
    sort_data = sorted(new_dict2.items(), key=lambda x: x[1], reverse=True)
    print("The top 20 companies with the most products:")
    print()
    for i in range(20):
        print(sort_data[i])
        
    return sort_data 

def product_types(new_list):

    oils_counter = 0
    tabs_counter = 0
    food_counter = 0
    drink_counter = 0
    uncat = -1
    

    for e in new_list:
        i = e[1].lower()
        if "oil" in i or "oils" in i or "mct" in i or "drops" in i:
            oils_counter += 1 
        elif "capsules" in i or "caps" in i or "gummies" in i or "gum" in i or "gums" in i:
            tabs_counter += 1
        elif "food" in i or "snacks" in i or "bar" in i:
            food_counter +=1
        elif "coffee" in i  or "tea" in i or "drink" in i:
            drink_counter +=1 
        else:
            uncat += 1 
            
    print()
    print("Types of products: ")
    print(f"{oils_counter} products are oils consumed in droppers")
    print(f"{tabs_counter} prodcuts are consumed orally in as a tablet")
    print(f"{drink_counter} products are various drinks e.g. tea, coffee, water")
    print(f"{uncat} products were unable to be catergorised based on the information availble") 
                          
if  __name__ == "__main__":
    filename = open_file("C:/Users/stxrm19/Documents/Code/CBD_products_list_index-2022-06-30.csv")
    #product_conc(filename)
    #product_types(filename)
    #products_by_company(filename)
    basic_info(filename)
    
    



