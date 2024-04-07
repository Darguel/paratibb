from db import clientPS

def adminSubCategory(idCAt,id,name):
    try:
        if (not(consultaCatById(id) is None)):
            try:
                conn = clientPS.client()

                cur = conn.cursor()

                cur.execute(f"UPDATE public.subcategory SET subcategory_id={id}, name='{name}', category_id={idCAt}, created_at=CURRENT_TIMESTAMP, updated_at=CURRENT_TIMESTAMP WHERE subcategory_id={id};")

                conn.commit()

            except Exception as e:
                return f'Error conexión {e}'
            
            finally:
                conn.close()
        else:
            try:
                conn = clientPS.client()

                cur = conn.cursor()

                sql = f"INSERT INTO public.subcategory(subcategory_id, name, category_id, created_at, updated_at) VALUES ({id}, '{name}', {idCAt}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"

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

        cur.execute(f"select * from public.subcategory where subcategory_id = {id}")

        data = cur.fetchone()

    except Exception as e:
        return f'Error conexión {e}'
    
    finally:
        conn.close()
        return data