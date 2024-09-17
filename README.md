## How to start a django webpage font justdjango.com
<br>
<table>
<tr>
  <td>
    1
  </td>
  <td>
    the first moment is necessary a virtual environment  
  </td>
</tr>

<tr>
  <td>
    2
  </td>
  <td>
    install django
  </td>
</tr>

<tr>
  <td>
    3
  </td>
  <td>
    use django-admin startproject <nome do projeto>
  </td>
</tr>

<tr>
  <td>
    4
  </td>
  <td>
    python manage.py migrate creates the db.sqlite3
  </td>
</tr>


<tr>
  <td>
    5
  </td>
  <td>
    python manage.py runserver to see if the server is running correctly
  </td>
</tr>

<tr>
  <td>
    6
  </td>
  <td>
    you need to create a superuser to administer the page with 'python manage.py createsuperuser'
  </td>
</tr>

<tr>
  <td>
    7
  </td>
  <td>
    another step is create an app 'python manage.py startapp <App's name>'  
  </td>
</tr>


<tr>
  <td>
    8
  </td>
  <td>
    in models.py create a model to manage data 
  </td>
</tr>

<tr>
  <td>
    9
  </td>
  <td>
    after this you need to update the migrate 'python manage.py makemigrations' 
  </td>
</tr>


<tr>
  <td>
    10
  </td>
  <td>
    python manage.py migrate to apply the changes at the database  
  </td>
</tr>
</table>




