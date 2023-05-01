# HIDS_Python
A simple HIDS using Pyhon, n-grams and Tries

O objetivo deste PP Parte I  ́e programar um algoritmo simples de HIDS (Host Intrusion Detection
System) e testá-lo offline em conjuntos de dados (data sets) publicamente disponíveis. Qualquer 
uso de recursos do computador por uma aplicação  ́e feito através de chamadas
ao SO via system calls. Como programas de computador são processos sequenciais, se uma máquina
(um servidor, p.e.) tem uma cesta relativamente pequena e estável de aplicações em execução,
nossa hipótese  ́e que os padrões de sequências de system calls configuram como que ”assinaturas” do
comportamento dinâmico normal das aplicações. Assim sendo, monitorar o surgimento de padrões
de sequências de systems calls anômalas ao conjunto do funcionamento normal  ́e uma forma de
detectar aplicações intrusas no host. Dessa forma o algoritmo consiste em coletar uma longa corrida
de system calls do funcionamento normal (n ̃ao infectado) da m ́aquina e percorrer esta sequência
armazenando todas as subsequências  ́unicas de tamanho n (n-grams) cuja frequência de ocorrência
 ́e maior que f. Os melhores valores de n e f devem ser determinados atrav ́es de teste, mas n =
2 a 12 e f = 5 s ̃ao valores típicos. Esta foi a ”fase de treinamento” do algoritmo. Na ”fase de
teste”, sendo dada uma corrida de system calls na qual deseja-se verificar a presença ou n ̃ao de
intruso, procede-se percorrendo a sequência de teste procurando por subsequˆencias de tamanho n
que n ao estejam presentes nas subsequências normais armazenadas. Quando uma ou mais de tais
sequências ”anômalas” forem encontradas com frequência maior ou igual a f, declara-se que um
intruso foi detectado. Para efiência de armazenamento e consulta das subsequˆencias normais utilize
a estrutura de dados trie, um tipo de  ́arvore de prefixos.
