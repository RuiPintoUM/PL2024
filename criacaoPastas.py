import os

for i in range(5):
    nome = f"TPC{i+1}"
    os.mkdir(nome)
    open(f"{nome}/.gitkeep", "w")