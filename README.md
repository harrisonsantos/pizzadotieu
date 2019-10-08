# Desafio 4
## hola que tal git
Tieu é dono de uma pizzaria e a administra à sua maneira. Enquanto em um restaurante normal, um cliente é atendido seguindo a regra de primeiro a chegar, primeiro a ser atendido, Tieu simplesmente minimiza o tempo médio de espera de seus clientes. Então, ele decide quem é servido primeiro, independentemente de quanto mais cedo ou mais tarde uma pessoa vier.

Diferentes tipos de pizzas levam diferentes quantidades de tempo para cozinhar. Além disso, quando ele começa a cozinhar uma pizza, ele não pode cozinhar outra pizza até que a primeira pizza esteja completamente cozida. Digamos que temos três clientes que chegam no momento t = 0, t = 1, & t = 2, respectivamente, e o tempo necessário para cozinhar suas pizzas é 3, 9 e 6, respectivamente. Se o Tieu aplicar a regra de primeiro a chegar, primeiro a ser servido, o tempo de espera de três clientes será 3, 11 e 16, respectivamente. O tempo médio de espera neste caso é (3 + 11 + 16) / 3 = 10. Esta não é uma solução otimizada. Depois de atender o primeiro cliente no momento t = 3, Tieu pode optar por atender o terceiro cliente. Nesse caso, o tempo de espera será 3, 7 e 17, respectivamente. Portanto, o tempo médio de espera é (3 + 7 + 17) / 3 = 9.

Ajude Tieu a alcançar o tempo médio médio de espera.

Formato de Entrada

A primeira linha contém um número inteiro N, que é o número de clientes. Nas próximas N linhas, a i-ésima linha contém dois números separados por espaço Ti e Li. Ti é o momento em que o cliente pede uma pizza, e Li é o tempo necessário para cozinhar essa pizza.
