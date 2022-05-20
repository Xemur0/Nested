# Nested
Небольшая реализация комментариев к статье с любой вложенностью
<b>Запуск:</b>
1. Переход в директорию APItest
2. Сборка - <b>sudo docker build -t api .</b>
3. Запуск контейнера - <b>sudo docker run --name api -p 8000:8000 -d api</b>
4. <b>localhost:8000/api/v1/post</b>


Прикручен Swagger
<b>localhost:8000/swagger</b>



1. Добавление комментариев(к посту):
 
   http://localhost:8000/api/v1/comment/
   
   post - id поста

Формат:
<b>
{
"name":"test2",
"text":"test2",
"post":2
}
  </b>
  
2. Добавление комментариев к комментарию(вложенность любая):

   http://localhost:8000/api/v1/comment/
   
   parent - id комментария

<b>
Формат:
{
"name":"test2",
"text":"test2",
"post":2,
"parent": 52
}
 </b>
 
 3. Получение всех комментариев:
 
    http://localhost:8000/api/v1/comments/
    
 4. Получение комментариев со всеми потомками:
   
    Формат:
    <b>localhost:8000/api/v1/comments/\<id></b>
 
    http://localhost:8000/api/v1/comments/39


 
 
 
 
 
