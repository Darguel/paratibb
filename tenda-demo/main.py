from typing import Union
from fastapi import FastAPI, File, UploadFile

from model import Product
from db import clientPS
from db import productDB
from db import categoryDB
from db import subCategoryDB
from db import productDB

import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/product/")
def consulta():
    return productDB.consulta()

@app.get("/product/{id}")
def consultaById(id):
    return productDB.consultaById(id)


@app.post("/product/")
def createProduct(prod: Product.Product):
    return productDB.insertProduct(prod)
    

@app.put("/product/{id}")
def updateById(prod: Product.Product):
    return productDB.update(prod)

@app.delete("/product/{id}")
def deleteById(id):
    return productDB.delete(id)

@app.post("/loadProducts")
async def create_upload_file(file: UploadFile):
    dadesCSV = pd.read_csv(file.file, header=0)
    for index, row in dadesCSV.iterrows():
        fila = row.to_dict()
        getCategory(fila["id_categoria"], fila["nom_categoria"])
        getSubCategory(fila["id_categoria"], fila["id_subcategoria"], fila["nom_subcategoria"])
        getProduct(fila["id_producto"], fila["nom_producto"], fila["descripcion_producto"], fila["companyia"], fila["precio"], fila["unidades"], fila["id_subcategoria"])
    return {"message": "introducidos los datos de forma correcta"}

def getCategory(id, name):
    return categoryDB.adminCategory(id,name)

def getSubCategory(idCAt, id, name):
    return subCategoryDB.adminSubCategory(idCAt,id,name)


def getProduct(id, name, desc, company, price, unit, idSubcate):
    return productDB.adminProduct(id, name, desc, company, price, unit, idSubcate)


# @app.get("/product/{id}")
# def getproductById(id:int):
#     productDB.consulta(id)
#     return {"masseage": f"consulta producte: {id}"}
