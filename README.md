
Este script obtiene la lista de items publicados por vendedor/es en MercadoLibre,
usa la api de ML para el site_id = "MLA" y genera un ​ archivo de LOG​ que contiene los siguientes datos de cada ítem: "​ id​ " del ítem, "​ title​ " del item, "​ category_id​ " donde está publicado, "​ name​ " de la categoría.
El output del archivo se verá asi:

Item_ID = MLA912271216
Title =  Apc Smart-ups Rc Src1ki-ar 1000va Con Entrada Y Salida De 230v  Negro
Category_ID = MLA1720
Category_name = UPS
****************************-
Item_ID = MLA912269991
Title =  Apc Back-ups Pro 900 Br900g-ar 900va Con Entrada Y Salida De 230v  Negro
Category_ID = MLA1720
Category_name = UPS
****************************-
Item_ID = MLA863267784
Title = Monitor Dell Professional P2018h Led 20  Negro 100v/240v
Category_ID = MLA14407
Category_name = Monitores
****************************-

REQUISITOS:
Tener instalado el modulo "requests", para instalarlo ejecutar
  pip install requests

Para ejecutar el script siga los siguientes pasos:
1. ejecutar por consola el script junto a los id de los vendedores deseados separados por un espacio:
./items_seller.py $SELLER_ID $SELLER_ID
ó
python3 items_seller.py SELLER1_ID SELLER2_ID
2. Se creara si no existiera el archivo items.log en el mismo directorio, cuidado si ya existe lo va a sobreescribir.

