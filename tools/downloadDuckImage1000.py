# encoding: UTF-8
from duckduckgo_search import DDGS
import urllib.request
import os
import time

filtro = "reborn"
destino = "./datasetreborn"
limite = 1000

os.makedirs(destino, exist_ok=True)

baixadas = 0
urls_baixadas = set()

print(f"Iniciando download de até {limite} imagens de '{filtro}'...")

with DDGS() as ddgs:
    results = ddgs.images(filtro, max_results=limite)
    for idx, result in enumerate(results):
        url = result.get("image")
        if not url or url in urls_baixadas:
            continue
        try:
            nome_arquivo = f"{filtro.replace(' ', '_')}_{baixadas}.jpg"
            caminho_arquivo = os.path.join(destino, nome_arquivo)
            urllib.request.urlretrieve(url, caminho_arquivo)
            print(f"[{baixadas}] OK - {url}")
            urls_baixadas.add(url)
            baixadas += 1
            if baixadas >= limite:
                break
            time.sleep(0.2)  # respeita o servidor
        except Exception as e:
            print(f"[{idx}] ERRO - {url} - {e}")

print(f"Downloads concluídos: {baixadas} imagens.")
