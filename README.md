# Video-Classification

## instrucciones

Instale las dependencias con

```
pip install -r requirements.txt  
```

Para descargar el dataset desde azure ejecute los siguientes comandos

```
$ dvc remote add -d myremote azure://cenia
$ dvc remote modify --local myremote account_name 'jrojash1'
$ dvc remote modify --local myremote sas_token 'sp=racwdli&st=2022-03-03T19:02:43Z&se=2022-06-10T04:02:43Z&spr=https&sv=2020-08-04&sr=c&sig=2G4z24TxrfbvAedKrKZU3hRRubaKjaA4%2Fww5U1dK4k4%3D'
$ dvc pull
```
Por ultimo ejecute 

```
python Main.py
```
