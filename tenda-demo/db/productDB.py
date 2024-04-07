from db import clientPS
from schema import producte

def consulta():

    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute("select * from public.product")

        data = cur.fetchone()

        data = producte.product_schema(data)

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
        return f"consulta de {data}"

def consultaById(id:int):

    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute(f"select * from public.product where product_id = {id}")

        data = cur.fetchone()

        data = producte.product_schema(data)

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
        return f"consulta de {data}"



def insertProduct(product):
    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute(f"INSERT INTO public.product(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES ({product.id}, '{product.name}', '{product.description}', '{product.company}', '{product.price}', '{product.unit}', '{product.subcategory_id}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);")

        conn.commit()
           

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
    
    return f"Producto añadido"



def update(product):
    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute(f"UPDATE public.product	SET product_id={product.id}, name='{product.name}', description='{product.description}', company='{product.company}', price={product.price}, units={product.unit}, subcategory_id={product.subcategory_id}, created_at=CURRENT_TIMESTAMP, updated_at=CURRENT_TIMESTAMP	WHERE product_id={product.id};")

        conn.commit()

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
    
    return f"Producto actualizado"

def delete(id:int):
    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute(f"DELETE FROM public.product WHERE product_id = {id}")

        conn.commit()

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
        return f"Producto eliminado de base de datos"
    
def adminProduct(id, name, desc, company, price, unit, idSubcate):
    try:
        if (not(consultaCatById(id) is None)):
            try:
                conn = clientPS.client()

                cur = conn.cursor()

                cur.execute(f"UPDATE public.product	SET product_id={id}, name='{name}', description='{desc}', company='{company}', price={price}, units={unit}, subcategory_id={idSubcate}, created_at=CURRENT_TIMESTAMP, updated_at=CURRENT_TIMESTAMP	WHERE product_id={id};")

                conn.commit()

            except Exception as e:
                return f'Error conexión {e}'
            
            finally:
                conn.close()
        else:
            try:
                conn = clientPS.client()

                cur = conn.cursor()

                sql = f"INSERT INTO public.product(product_id, name, description, company, price, units, subcategory_id, created_at, updated_at) VALUES ({id}, '{name}', '{desc}', '{company}', '{price}', '{unit}', '{idSubcate}', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
                
                cur.execute(sql)

                conn.commit()

            except Exception as e:
                return f'Error conexión {e}'
            
            finally:
                conn.close()
                
    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        return f"Producto añadido o actualizado"
    
def consultaCatById(id:int):

    try:
        conn = clientPS.client()

        cur = conn.cursor()

        cur.execute(f"select * from public.product where product_id = {id}")

        data = cur.fetchone()

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
        return data