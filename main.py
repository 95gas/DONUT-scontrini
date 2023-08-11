from donut import DonutModel
from PIL import Image
import torch
import pandas as pd
import glob


def load_images_from_folder(folder):
    image_list = []
    for filename in glob.glob(folder+"/*"):
        image_list.append(filename)
    return image_list


# Function for finding municipality
def check_municipality(CAP, address):
    
    if CAP is None:
        return -1
    
    # read the file
    file = pd.read_csv('assets/listacomuni.csv',sep=';', encoding = "ISO-8859-1")
    ListMun = file['Comune']
    ListCAP = file['CAP']
    index = -1

    # get all municipalites with same CAP
    candidates = []
    
    for entry in ListCAP:
        index = index + 1
        # condition to match
        if entry in CAP:
            candidates.append(ListMun[index])
                
    tokens = address.split()
    
    # find out the municipality
    for entry in candidates:
        for item in tokens:
            if item.lower() in entry.lower():
                return entry
    
    return -1


def main():
    
    # call model
    model = DonutModel.from_pretrained("assets/model")
    if torch.cuda.is_available():
        model.half()
        device = torch.device("cuda")
        model.to(device)
    else:
        model.encoder.to(torch.bfloat16)
        
    # run prediction 
    model.eval()
    images = load_images_from_folder("test")
        
    for item in images:
        
        print("\nProcessing image: ", item)
        
        image = Image.open(item).convert("RGB")
        output = model.inference(image=image, prompt="<s_sroie-donut>")
        
        # LOOF FOR TOTAL
        try:
            print('\tTotale:', output['predictions'][0]['total'])
        except:
            print('\tTotale: NOT FOUND')
            
            
        # LOOF FOR MUNICIPALITY
        try:
            address = output['predictions'][0]['address']
            
            import re
            CAP = re.findall(r"\D(\d{5})\D", address)
            
            mun = check_municipality(CAP, address)
            
            if mun == -1:
                
                file = pd.read_csv('assets/listacomuni.csv',sep=';', encoding = "ISO-8859-1")
                ListMun = file['Comune']
                
                tokens = address.split()
    
                # find out the municipality
                found = False
                for entry in tokens:
                    for item in ListMun:
                        if found==False:
                            if item.lower() in entry.lower():
                                print('\tCOMUNE: ', item)
                                found = True
                if found==False:   
                    print('\tComune: NOT FOUND')
            
            else:
                print('\tComune: ', mun)
            
        except:
            print('\tComune: NOT FOUND')
            
        # loof for date
        try:
            print('\tData:', output['predictions'][0]['date'])
        except:
            print('\tData: NOT FOUND')
        

if __name__ == "__main__":
    main()