# voolkia-challenge

Este script obtiene la lista de items publicados por vendedor/es en MercadoLibre,usa la api de ML para el site_id = "MLA" 
y genera un archivo de LOG que contiene los siguientes datos de cada ítem: "id" del ítem, "title" del item, "category_id" 
donde está publicado, "name" de la categoría.
***
El output del archivo se verá asi:
```
Item_ID = MLA822918508
Title = Juego De Playa Balde Y Pala
Category_ID = MLA432255
Category_name = Sets de Juguetes Playeros
****************************-

Item_ID = MLA859259405
Title = Kit De Limpieza Cartier Para Metal
Category_ID = MLA3938
Category_name = Otros
****************************-

Item_ID = MLA850734878
Title = Botellón  De Farmacia
Category_ID = MLA1383
Category_name = Otros
****************************-
```
***


### REQUISITOS:

Tener instalado el modulo "requests", para instalarlo ejecutar:
```
pip install requests
```

### Para ejecutar el script siga los siguientes pasos:
* Ejecutar por consola el script junto a los id de los vendedores deseados separados por un espacio:
```
./items_seller.py $SELLER_ID $SELLER_ID 
```
	ó
```
python3 items_seller.py SELLER1_ID SELLER2_ID
```
* Se creara si no existiera el archivo items.log en el mismo directorio, cuidado si ya existe lo va a sobreescribir.


