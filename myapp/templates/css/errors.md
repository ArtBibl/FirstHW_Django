Есть пара мелких опечаток, которые Вы в последствии будете видеть с помощью валидатора

Вот тут опечатка

<h2><img src="./Logo2.png" width="20" alt="My logo" a>   Home Work.</h2>
(зачем-то дорисовали атрибут "а" картинке)
P.S. Ну и походу где-то один раз сделали, а потом копировали) 
Потому что такой прикол ещё встречается на других страницах

и вот тут опечатка:
<b><u>a</b></u></b>

(зачем-то закрыли тег "b" раньше времени)

Но особого внимания они не стоят, поэтому это не считается)

! Теперь то, что стоит внимания:

1.  <a href="./Best_tags.html"><button>Best tags</button></a>

Вот так делать ни в коем случае нельзя
интерактивные элементы вкладывать один в один нельзя

Нужно было либо ссылку использовать либо кнопку. Они не могут быть наследниками (child'ами) друг друга.

P.S. Возможно, я Вам это провтыкал рассказать. Тогда за ошибку не считается, но запомнить такой факт стоит.

2. Наследниками списков могут быть только <li></li>

То есть у Вас есть вот такой код

  <ul>
      <li>#myid:focus</li>
      <b>0, 1, 1, 0</b>    
      <li>.menu > li > a:hover</li>
      <b>0, 0, 2, 1</b>    
      <li>#myid > ul > li a:hover</li>
      <b>0, 1, 1, 2</b>     
  </ul>

и исходя из него у списка ul наследников 6, 3 из которых - теги <b>
Вот так нельзя)
Лучше делайте, как у Вас в другом задании:

<ol>
  <li><b>Lorem ipsum, dolor sit amet consectetur adipisicing elit.</b><br> Voluptates praesentium, et iusto aspernatur itaque rerum minus officia repudiandae enim quis dolor dolorum numquam saepe similique incidunt consequuntur impedit? Numquam, deserunt?</li>
  <li><b>Lorem ipsum, dolor sit amet consectetur adipisicing elit.</b><br> Voluptates praesentium, et iusto aspernatur itaque rerum minus officia repudiandae enim quis dolor dolorum numquam saepe similique incidunt consequuntur impedit? Numquam, deserunt?</li>
  <li><b>Lorem ipsum, dolor sit amet consectetur adipisicing elit.</b><br> Voluptates praesentium, et iusto aspernatur itaque rerum minus officia repudiandae enim quis dolor dolorum numquam saepe similique incidunt consequuntur impedit? Numquam, deserunt?</li>
  <li><b>Lorem ipsum, dolor sit amet consectetur adipisicing elit.</b><br> Voluptates praesentium, et iusto aspernatur itaque rerum minus officia repudiandae enim quis dolor dolorum numquam saepe similique incidunt consequuntur impedit? Numquam, deserunt?</li>
  <li><b>Lorem ipsum, dolor sit amet consectetur adipisicing elit.</b><br> Voluptates praesentium, et iusto aspernatur itaque rerum minus officia repudiandae enim quis dolor dolorum numquam saepe similique incidunt consequuntur impedit? Numquam, deserunt?</li>
</ol>

3. Итог
   Вы - большой молодец! + персональный лайк за удобство при просмотре заданий)
   Всё круто, за исключением мелких недочётов
