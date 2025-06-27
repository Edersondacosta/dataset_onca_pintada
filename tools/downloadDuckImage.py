# encoding: UTF-8
import DuckDuckGoImages as ddg # pip install DuckDuckGoImages

filtro = "onça-pintada"
destino = './dataset'

print('iniciando downlaod')
try:
    ddg.download(filtro, folder=destino, remove_folder=False, parallel=True)
except Exception as e:
    print("type error: ", e)
print("downloads concluídos")
        
    