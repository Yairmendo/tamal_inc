# Tamal_inc

##Plateamiento

Tortas De Tamal Inc. necesita integrar fuentes de datos que describan sus ventas en el mercado. La información vive en su Data Lake y usted deberá homologarlas para exponerlas en un cubo de datos en formato estrella que permita a sus empleados generar reportes. El data lake está dividido en 2 zonas que almacenan los datos con base en su madurez. Las zonas del data lake son:
●Crudo:
Los datos se guardan en los archivos de entrada de una forma ordenada y que
permite tener trazabilidad respetando formatos y estructuras de datos originales.

●Procesado:
En esta zona se guardan los datos refinados que se toman de la zona de datos
crudos y están listos para ser consumibles por las interfaces que llevan los datos al
usuario final.

#### Fuentes de datos a integrar
Las dos fuentes de datos que se necesitan integrar son:

- Ventas reportadas por ERP​ : Datos internos generados por Tamal Inc y
almacenados en su sistema ERP donde registran las ventas de sus productos
realizadas por los revendedores. Los datos se actualizarán en el data lake de forma semanal y contienen información del último mes en cada una de las actualizaciones.
No existe una conexión directa con el ERP y la información que se ingresa al data lake se comparte en formato csv.

- Ventas y precios de campo​ : Datos generados por la empresa TeInvento.inc
dedicada a levantar datos de campo sobre los productos de sus clientes y la
competencia. En el dataset se registran las ventas en el punto de venta de los
productos de Tamal Inc y además los precios de sus productos y la competencia.
Estos datos se actualizan de forma semanal y contienen información del último mes en cada actualización. TeInvento.inc comparte la información para ingestar al data lake en formato xlsx.

###Requirements

Python 3.x, cualquier versión de  pip, y virtualenv (o venv)

### Ejecución

Usa ya sea $ python main.py o $ python3 main.py  deacuerdo a tu sistema operativo.



### Aclaraciones
Dentro de este proyecto se mostrará una parte del proceso de extract, ya que a como se encuentra la informacón segamentada y no clasificada tendríamos que "asumir" muchas cosas para poder "interpretarla", lo cuál sería incorrecto por que al asumir origenes de los datos o valores podríamos incurrir en errores en el análisis de los datos y provocar daños a nuestro cliente "tamales inc".

Lo que podemos realizar de forma más acertada es darle recomendaciones para que al trabajar con empresas terceras como "teinvento inc"; para la recopilación de datos, tenga un formato y estructura más adecuado para los datos.
 ### Imagen del modelo 
![Modelo de base de pipe line "images/tamales_inc_model.png"](images/tamales_inc_model.png?raw=true "Title")

### Observaciones
Dentro de los puntos que se pueden mejorar son:

1.  En el modelo de "Ventas y precios de campo", ya que se está trabajando en Excel es más fácil para un usuario agregar datos a las columnas de los archivos.
 
2. Dentro de este mismo modelo, realizar la estandarización para el nombrado de archivos para que sea más accesible para el manejo de la información y puedan aprovecharlos en las demás áreas como marketing,etc.

3. Al tener un path  como "./teinvento_inc/ventas_reportadas_mercado_tamales/mx/20200801/" podemos reducirlo másy evitar tantos niveles de carpetas inecesarias, como el caso de MX ya que en los archivos se encuentra el campo "País" podríamos omitir ese nivel de carpetas.
      
4. Para el path de tamal inc "./tamales_inc/ventas_mensuales_tamales_inc/mx/20200801/csv", también podemos omitir varias carpetas ya que sería redundante, como la carpeta "MX", "csv", "Norte", "Sur", "E._Privados" al tener estandarizado que el almacenamiento de datos en formato csv únicamente y también los nombres de los archivos podemos evitar varios niveles de carpetas innecesarias.
       
5. Dentro de los archivos de datos en "Ventas reportadas por ERP", hay varios campos que se pueden optimizar, principalmente donde se colocan las "ventas de sus productos"; dentro del análisis lo nombre "Sales" pero no nos da una idea certera de a que valor se refiere, ya que tiene mucha dispersión, no sabemos que unidades son, es muy fuctuante y de intentarlo aterrizar a "unidades vendidas", "monto mensual", "ganancias", etc no sería un dato que se pueda adaptar ya que su comportamiento en toda la tabla no lo permite.
       
6. Realizar una optimización para reducir la captura de errores por eeror humano al momento de llenar los formularios, que revise estadísticamente (en campos donde sea posible) los datos para buscar outliers.

### Plabras finales

Dentro de la ciencia de datos debemos estar concientes de la responsabilidad que tenemos, los peligros y beneficios de los análisis que hacemos día a día, una frase muy conocida "garbage in, garbage out", no importa que tan bueno sea tu modelo, con la tecnología más avanzada o con la infrestuctura que siempre soñaste, si alimentas a tu modelo o sistema con datos que son "basura" a la salida obtendras "basura".