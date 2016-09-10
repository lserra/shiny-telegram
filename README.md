# zinzane
Calculating Aging of the Products (Analisys and Report)

# Objective: 
Extrair os dados da base do Cliente que estão em um servidor remoto e movê-los para uma stage area que também fica em em outro servidor remoto. Ou seja, podemos dizer que tanto o data source quanto o data target estão nas nuvens. Em seguida, validar e tratar estes dados antes de movê-los para o repositório de data mart. E por fim efetuar o processamento de cálculo do aging, com base nos seguintes critérios: por Loja e por Cia.

# Description: 
O cálculo do aging consiste em determinar para cada peça armazenada no estoque, há quanto tempo ela está armazenada. Para isso precisamos para cada sku do estoque em cada loja da empresa varrer todos as entradas, da mais recente para a mais antiga, e identificar a data da entrada. Armazenamos a data da entrada e a quantidade de peças, pois desta forma conseguimos mostrar a informação do Aging em diversos níveis e formas distintas de agregação.

# Requirements:
  * Sistema Operacional = Windows/Linux
  * SSH (Linux) ou OpenSSH (Windows)
  * MySQL 5.5 ou superior
  * Pycharm 3 ou superior
  * Python 2.7.x ou superior
  * Bibliotecas Python: pymssql, MySQLdb

# Architecture:
![arq-func](/images/architecture-functional.png)
