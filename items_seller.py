#!/usr/bin/env python3

import requests
import sys

def items_log():    
    #url para el sitio MLA
    url_seller = "https://api.mercadolibre.com/sites/MLA/search?seller_id="
    url_categories = "https://api.mercadolibre.com/categories/"
    log = open("items.log","w+")
    #recorre las lista de IDs pasados por consola
    for seller in sys.argv[1:]:  
        
        offset = 0
        cont = 0
        res = requests.get(url_seller+ str(seller))        
        data_seller = res.json()       
        
        items = data_seller["results"]           
        total_items = data_seller["paging"]["total"]
        limit = data_seller["paging"]["limit"]
        print("cargando items del vededor {}".format(seller))
        #La url limita el numero de items que muestra, para cambiar de pagina usa el parametro offset       
        while(offset<total_items):
            
            res = requests.get(url_seller + str(seller)+"&offset="+ str(offset))
            data_seller = res.json()
            items = data_seller.get("results")

            # itera los items encontrados en la lista "results"
            for item in items:
                #busqueda de la categoria
                category_id = item.get("category_id")
                res_categories = requests.get(url_categories+ category_id)
                category = res_categories.json()     
                #guarda datos en el log
                log.write("Item_ID = " + item.get("id")+ "\n")
                log.write("Title = " + item.get("title")+ "\n")
                log.write("Category_ID = " + category_id + "\n")
                log.write("Category_name = "+ category.get("name") + "\n")
                log.write("-\n".rjust(30,'*')) 
                cont = cont + 1
            offset = offset + limit  
        #imprime la cantidad de items por vendedor
        print("cantidad de items: {}".format(cont)) 
    log.close()         
      
       
if __name__ == "__main__":

    if (len(sys.argv)==1):
        print("Ingrese al menos un ID")
    else:
        items_log()