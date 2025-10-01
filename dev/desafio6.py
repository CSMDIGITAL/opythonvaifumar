area_do_campo = 6000
m2_m2 = 1000000
area_desmatada = float(input("digite a área de desmatada"))
area_desmatada = area_desmatada * m2_m2
campos_exatos = area_desmatada/area_do_campo
print(area_desmatada)
print(area_do_campo)
print(f'{campos_exatos:,.2f}')
import math
print(math.sqrt(2))

# UPPER_SNAKE_CASE e SNAKE_CASE
# PASCAL_CASING - Caculadora
# constante  UPPER_SNAKE_CASE
# PEP-08 - regras
KM2_PARA_M2 = 1_000_000
# CONSTANTE
AREA_CAMPO_M2 = 100 * 60 

# VARIÂVEL - snake_case
area_devastada_km2 = float(input("digite a área de desmatada em KM²"))

#Calculo
area_desmatada_km2 =  area_devastada_km2 * (1000**2)
area_do_campo_futebol = area_desmatada_km2 /AREA_CAMPO_M2
print("A ârea desmatada", area_devastada_km2, "KM²")
