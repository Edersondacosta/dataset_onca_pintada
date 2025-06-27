# dataset_onca_pintada

🐆 Dataset de Onças-Pintadas – Formato YOLO
Este repositório disponibiliza um dataset de imagens de onças-pintadas (Panthera onca) com anotações manuais no formato YOLO, organizado para facilitar o treinamento de modelos de detecção de objetos.

As imagens foram coletadas em sites públicos da internet e cuidadosamente anotadas manualmente com bounding boxes representando a presença da onça-pintada.

📁 Estrutura do Repositório
Copiar
Editar
├── dataset/
│   ├── imagem1.jpg
│   ├── imagem1.txt
│   ├── imagem2.jpg
│   ├── imagem2.txt
│   └── ...
└── README.md
Os arquivos .jpg são as imagens originais.

Cada arquivo .txt contém as anotações da imagem correspondente, no formato YOLO.

🧾 Formato das Anotações (YOLO)
Cada linha dos arquivos .txt segue o padrão:

php-template
Copiar
Editar
<class_id> <x_center> <y_center> <width> <height>
Todos os valores são normalizados entre 0 e 1.

Neste dataset: class_id = 0 representa onça-pintada.

🧠 Aplicações
Treinamento de modelos como YOLOv4, YOLOv5, YOLOv8

Testes em projetos de visão computacional

Estudos sobre monitoramento automatizado da fauna

📄 Licença e Uso
As imagens foram obtidas de fontes públicas na internet, e as anotações foram feitas manualmente para fins educacionais e de pesquisa. Este dataset está disponível sob a Licença MIT.
