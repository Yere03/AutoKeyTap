# AutoKeyTap

En este proyecto se ha utilizado la biblioteca gráfica GTK 4.0. 

Para la instalacion de GTK vease:

https://www.gtk.org/docs/installations/windows/ (Windows)

https://www.gtk.org/docs/installations/linux/ (Linux)

https://www.gtk.org/docs/language-bindings/python/ (PyGObject)

## Inicial UI Version
![image](https://github.com/user-attachments/assets/01586831-5713-463f-8d54-7304907b6bd8)


Esta aplicación presta la utilidad de presionar teclas automaticamente con un intervalo de tiempo entre pulsaciones.

Para la ejecución en segundo plano sin paralizar la interfaz gráfica se ha empleado concurrencia mediante hilos utilidad de python Thread referencia https://docs.python.org/es/3.8/library/threading.html.

Se ha utilzado los paquetes: 

- PyGObject (binding for Gobjects)
  
- pynput (Entrada salida)

- pyinstaller (para crear el instalador)

Si se quiere crear el ejecutable lo puede hacer mendiante el siguiente comando "pyinstaller .\main.spec." desde la carpeta del proyecto. Se debe de haber instalado todas las dependecias necesarias para ello.
