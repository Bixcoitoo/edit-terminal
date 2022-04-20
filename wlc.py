import os,sys,time,random
print("")
print("")
color = ["\033[1;31m","\033[1;32m"]
m = random.choice(color)+"Bem vindo THBD \nAtualizando pacote de dados...\n\n\n\n\n\n\n\n\n\n\nConcluido mãos a obra!!\n"
for msg in m:
    sys.stdout.write(msg)
    sys.stdout.flush()
    time.sleep(0.25)
print("")
