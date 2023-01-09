import json
repetidos = [1,2,3,"1","2","3",3,4,5]
r = [1,"5",2,"3"]
d_str = '{"valor":125.3,"codigo":123}'

no_repetidos = list(set(repetidos))
vals_en_comun = list(set(repetidos) & set(r))
d_dic = json.loads(d_str)

print("no repetidos:", no_repetidos)
print("valores en comun:", vals_en_comun)
print("diccionario:", d_dic)