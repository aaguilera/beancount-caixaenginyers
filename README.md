# beancount-caixaenginyers

Un _importer_ per tal de generar transaccions en el format [_Beancount_](https://github.com/beancount/beancount/) a partir d'un fitxer de moviments de Caixa d'Enginyers.

## Instal·lació

Copieu el fitxer `caixaenginyers.py` al directori on es troben la resta
d'importers de Beancount, per exemple, a `~/.local/lib/python3.9/site-packages/beancount/ingest/importers/` o similar.

## Preparació del fitxer de moviments

Baixeu el fitxer de moviments de Caixa d'Enginyers _en format XLS_, i convertiu-lo
a CSV, mirant de conservar la codificació UTF-8.

Si teniu el _LibreOffice_ instal·lat, podeu fer la conversió automàticament des de la línia de comandes:

```bash
libreoffice --headless --convert-to "csv:Text - txt - csv (StarCalc):44,34,76,1,1/1:" MovimientosCuenta.xls
```

Això us generarà un fitxer CSV anomenat `MovimientosCuenta.csv`.

## Configuració de l'importer

Editeu el fitxer `importconfig.py` i modifiqueu el nom simbòlic del vostre compte _Beancount_ de Caixa d'Enginyers:

```python
ACCOUNT_NAME = "Assets:CaixaEnginyers:CompteCorrent"
```

## Utilització

Suposant que teniu els fitxers `importconfig.py` i `MovimientosCuenta.csv` al directori actual, podeu fer la importació amb la següent comanda:

```bash
bean-extract importconfig.py MovimientosCuenta.csv
```

Les transaccions es mostraran a la sortida estandard.
