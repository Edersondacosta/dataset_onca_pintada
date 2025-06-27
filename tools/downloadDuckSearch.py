# encoding: UTF-8
from duckduckgo_search import DDGS
import urllib.request
import os

filtro = "onça-pintada"
destino = "./dataset"
os.makedirs(destino, exist_ok=True)

print('Iniciando download...')
with DDGS() as ddgs:
    results = ddgs.images(filtro, max_results=10)
    for idx, result in enumerate(results):
        url = result["image"]
        try:
            urllib.request.urlretrieve(url, f"{destino}/{filtro.replace(' ', '_')}_{idx}.jpg")
            print(f"[{idx}] OK - {url}")
        except Exception as e:
            print(f"[{idx}] ERRO - {url} - {e}")
print("Downloads concluídos.")
