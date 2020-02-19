[![implementation](https://img.shields.io/badge/implementation-python-blue.svg)][python]

[python]: http://docs.oracle.com/javase/8/docs/api/

# Melt Group Coding Challenge

## Problema

#### Primera parte:

Escribe un programa de consola que acepte como su único parámetro de entrada la URL de una
página web. Al ejecutarse el programa, debe acceder a la URL que se le ha pasado como
parámetro, recuperar su contenido, e imprimir por pantalla todas las URLs que haya detectado
en la respuesta devuelta por el servidor. 
Puedes usar cualquier lenguaje de programación y cualquier librería que consideres oportuno.

#### Segunda parte:

Modifica el programa para que por cada una de las URLs encontradas se haga de nuevo una
petición y se recupere una nueva lista de URLs. El programa debe aceptar por línea de comandos
un parámetro adicional N que indique el “máximo número de iteraciones” que se quieren seguir.

Por ejemplo, para N=3 deberías imprimir los resultados en el siguiente formato:

```
--- URL-A
   --- URL-A-1
      --- URL-A-1-1
      --- URL-A-1-2
   --- URL-A-2
   --- URL-A-3
--- URL-B
   --- URL-B-1
   --- URL-B-2
   --- URL-B-3
      --- URL-B-3-1
--- URL-C
   --- URL-C-1
   --- URL-C-2
```

Entrega:
Debes entregar un .zip con el código fuente del programa y un fichero llamado readme.pdf con
el listado de las dependencias usadas y las instrucciones necesarias para compilar/ejecutar el
programa. 
 

## Ejemplo del Programa
```
(venv) C:\Users\Eric\PycharmProjects\Melt-Group-Challenge>python ProblemOne.py
https://www.meltgroup.com/en/
https://www.meltgroup.com/en/consulting/
https://www.meltgroup.com/en/consulting/
https://www.meltgroup.com/en/our-history/
https://www.meltgroup.com/en/areas-of-expertise/
https://www.meltgroup.com/en/our-values/
https://www.meltgroup.com/en/work-with-us/
https://www.meltgroup.com/en/services/
https://www.meltgroup.com/en/service/recruitment-and-selection/
https://www.meltgroup.com/en/service/payroll/
https://www.meltgroup.com/en/service/workforce-management/
https://www.meltgroup.com/en/service/training/
https://www.meltgroup.com/en/blog/
https://www.meltgroup.com/en/contactus/
https://www.meltgroup.com/en/jobs/
https://www.meltgroup.com
https://www.meltgroup.com/fr/
https://www.meltgroup.com/en/
#
https://www.meltgroup.com/en/consulting/
https://www.meltgroup.com/en/consulting/
https://www.meltgroup.com/en/our-history/
https://www.meltgroup.com/en/areas-of-expertise/
https://www.meltgroup.com/en/our-values/
https://www.meltgroup.com/en/work-with-us/
https://www.meltgroup.com/en/services/
https://www.meltgroup.com/en/service/recruitment-and-selection/
https://www.meltgroup.com/en/service/payroll/
https://www.meltgroup.com/en/service/workforce-management/
https://www.meltgroup.com/en/service/training/
https://www.meltgroup.com/en/blog/
https://www.meltgroup.com/en/contactus/
https://www.meltgroup.com/en/jobs/
https://www.meltgroup.com
https://www.meltgroup.com/fr/
https://www.facebook.com/MeltGroupSL
https://twitter.com/Melt_Group
https://plus.google.com/112901454802758704331
https://es.linkedin.com/company/melt-consulting-s-l-
https://www.meltgroup.com/en/contactus/
https://www.meltgroup.com/en/services/
https://www.meltgroup.com/en/jobs/
#
https://www.meltgroup.com/en/services/
https://www.meltgroup.com/en/
https://www.meltgroup.com/en//jobs
https://www.meltgroup.com/en//cv
https://www.meltgroup.com/en/work/responsable-en-gestion-de-activos-e-inventario-en-operadores-red-madrid/
https://www.meltgroup.com/en/work/product-manager-junior-madrid/
https://www.meltgroup.com/en/work/senior-project-manager-madrid-2/
https://www.meltgroup.com/en/work/jefe-de-recursos-humanos-mallorca/
https://www.meltgroup.com/en/work/java-developer-la-haya/
https://www.meltgroup.com/en/work/medico-radiologo-guipuzcoa/
https://www.meltgroup.com/en/work/javascript_frontend-barcelona/
https://www.meltgroup.com/en/work/controller-financiero-almazora/
https://www.meltgroup.com/en/work/ingeniero-comercial-zaragoza/
https://www.meltgroup.com/en/blog/
https://www.meltgroup.com/en/encuesta-trabaja-4-dias-y-cobra-5/
https://www.meltgroup.com/en/navidad-en-la-empresa-parada-obligatoria/
https://www.meltgroup.com/en/blog-abc-direccion-de-personas-edem/
https://www.meltgroup.com/en/ya-somos-mas-de-30-000-en-linkedin/
https://www.meltgroup.com/en/
https://www.meltgroup.com/en/contactus/
https://www.meltgroup.com/en/
https://www.meltgroup.com/en/consulting/
https://www.meltgroup.com/en/services/
https://www.meltgroup.com/en/blog/
https://www.meltgroup.com/en/contactus/
https://www.meltgroup.com/en/jobs/
https://www.meltgroup.com/en/cv/
https://www.facebook.com/MeltGroupSL
https://twitter.com/Melt_Group
https://plus.google.com/106912417646101196509/about
https://www.linkedin.com/company/melt-consulting-s.l.?trk=top_nav_home
#
https://www.meltgroup.com/politica-de-cookies/
https://www.meltgroup.com
https://www.meltgroup.com/fr/
https://www.meltgroup.com/en/
En la pagina de https://www.meltgroup.com/en/hay un total de 79links encontrados

(venv) C:\Users\Eric\PycharmProjects\Melt-Group-Challenge>python ProblemOne.py
https://www.meltgroup.com/en/
https://www.meltgroup.com/en/consulting/
https://www.meltgroup.com/en/consulting/
https://www.meltgroup.com/en/our-history/
https://www.meltgroup.com/en/areas-of-expertise/
https://www.meltgroup.com/en/our-values/
https://www.meltgroup.com/en/work-with-us/
https://www.meltgroup.com/en/services/
https://www.meltgroup.com/en/service/recruitment-and-selection/
https://www.meltgroup.com/en/service/payroll/
https://www.meltgroup.com/en/service/workforce-management/
https://www.meltgroup.com/en/service/training/
https://www.meltgroup.com/en/blog/
https://www.meltgroup.com/en/contactus/
https://www.meltgroup.com/en/jobs/
https://www.meltgroup.com
https://www.meltgroup.com/fr/
https://www.meltgroup.com/en/
#
https://www.meltgroup.com/en/consulting/
https://www.meltgroup.com/en/consulting/
https://www.meltgroup.com/en/our-history/
https://www.meltgroup.com/en/areas-of-expertise/
https://www.meltgroup.com/en/our-values/
https://www.meltgroup.com/en/work-with-us/
https://www.meltgroup.com/en/services/
https://www.meltgroup.com/en/service/recruitment-and-selection/
https://www.meltgroup.com/en/service/payroll/
https://www.meltgroup.com/en/service/workforce-management/
https://www.meltgroup.com/en/service/training/
https://www.meltgroup.com/en/blog/
https://www.meltgroup.com/en/contactus/
https://www.meltgroup.com/en/jobs/
https://www.meltgroup.com
https://www.meltgroup.com/fr/
https://www.facebook.com/MeltGroupSL
https://twitter.com/Melt_Group
https://plus.google.com/112901454802758704331
https://es.linkedin.com/company/melt-consulting-s-l-
https://www.meltgroup.com/en/contactus/
https://www.meltgroup.com/en/services/
https://www.meltgroup.com/en/jobs/
#
https://www.meltgroup.com/en/services/
https://www.meltgroup.com/en/
https://www.meltgroup.com/en//jobs
https://www.meltgroup.com/en//cv
https://www.meltgroup.com/en/work/responsable-en-gestion-de-activos-e-inventario-en-operadores-red-madrid/
https://www.meltgroup.com/en/work/product-manager-junior-madrid/
https://www.meltgroup.com/en/work/senior-project-manager-madrid-2/
https://www.meltgroup.com/en/work/jefe-de-recursos-humanos-mallorca/
https://www.meltgroup.com/en/work/java-developer-la-haya/
https://www.meltgroup.com/en/work/medico-radiologo-guipuzcoa/
https://www.meltgroup.com/en/work/javascript_frontend-barcelona/
https://www.meltgroup.com/en/work/controller-financiero-almazora/
https://www.meltgroup.com/en/work/ingeniero-comercial-zaragoza/
https://www.meltgroup.com/en/blog/
https://www.meltgroup.com/en/encuesta-trabaja-4-dias-y-cobra-5/
https://www.meltgroup.com/en/navidad-en-la-empresa-parada-obligatoria/
https://www.meltgroup.com/en/blog-abc-direccion-de-personas-edem/
https://www.meltgroup.com/en/ya-somos-mas-de-30-000-en-linkedin/
https://www.meltgroup.com/en/
https://www.meltgroup.com/en/contactus/
https://www.meltgroup.com/en/
https://www.meltgroup.com/en/consulting/
https://www.meltgroup.com/en/services/
https://www.meltgroup.com/en/blog/
https://www.meltgroup.com/en/contactus/
https://www.meltgroup.com/en/jobs/
https://www.meltgroup.com/en/cv/
https://www.facebook.com/MeltGroupSL
https://twitter.com/Melt_Group
https://plus.google.com/106912417646101196509/about
https://www.linkedin.com/company/melt-consulting-s.l.?trk=top_nav_home
#
https://www.meltgroup.com/politica-de-cookies/
https://www.meltgroup.com
https://www.meltgroup.com/fr/
https://www.meltgroup.com/en/
En la pagina https://www.meltgroup.com/en/hay un total de 79 links encontrados.
```
