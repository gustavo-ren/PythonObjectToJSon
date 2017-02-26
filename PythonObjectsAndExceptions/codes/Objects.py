'''
Created on 25 de fev de 2017

@author: Gustavo
'''

from codes.FirstClass import FirstClass
import json
from pprint import pprint



def main():
    x=FirstClass("555-555", "Oliver Queen", "25")
    
    with open ("perfil.json") as dataJson :
         dataJson=json.dumps(x.__dict__)
         
    pprint(dataJson)

         
    
main()