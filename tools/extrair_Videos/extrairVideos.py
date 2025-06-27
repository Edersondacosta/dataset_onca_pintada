import cv2
import os

# Caminho do vídeo
video_path = 'onca.mp4'

# Pasta onde os frames serão salvos
output_folder = 'frames_1fps_meio'
os.makedirs(output_folder, exist_ok=True)

# Abre o vídeo
cap = cv2.VideoCapture(video_path)

# FPS e duração do vídeo
fps = cap.get(cv2.CAP_PROP_FPS)
duracao = cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps
print(f"FPS: {fps}")
print(f"Duração (s): {duracao}")

# Extrair 1 frame por segundo (no meio do segundo)
segundo = 0
frame_salvo = 0

while segundo < duracao:
    tempo_ms = (segundo + 0.5) * 1000  # meio do segundo em milissegundos
    cap.set(cv2.CAP_PROP_POS_MSEC, tempo_ms)
    ret, frame = cap.read()

    if not ret:
        break

    frame_filename = os.path.join(output_folder, f'frame__onca01_{frame_salvo:04d}.jpg')
    cv2.imwrite(frame_filename, frame)
    print(f'Salvou {frame_filename} no tempo {tempo_ms/1000:.2f}s')
    frame_salvo += 1
    segundo += 1

cap.release()
print(f'Total de frames salvos: {frame_salvo}')
