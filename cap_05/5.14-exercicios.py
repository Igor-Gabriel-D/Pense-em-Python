#O módulo time fornece uma função, também chamada time, que devolve a Hora Média de
#Greenwich, que é um momento arbitrário usado como ponto de referência.
#sistemas UNIX, a época é primeiro de janeiro de 1970.

#Escreva um script que leia a hora atual e a converta em um tempo em horas, minutos e
#segundos, mais o número de dias desde a época.

import time

print(int(time.time()))

hora = (int(time.time()) % 86400)

print( (hora // 60 ) // 60)
print( (hora // 60)  % 60  )
print( hora % 60 )


dias = (int(time.time()) // 86400)
print(dias)

