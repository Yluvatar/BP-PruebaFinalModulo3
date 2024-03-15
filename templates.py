from string import Template

html_template = Template("""
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="ISO-8859-1">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello World!</title>
    </head>
    <body>
        $contenido
    </body>
</html>
""")

aves_template = Template("""
<p><h2>Nombre Ave: $ave</h2></p>
<p><h2>Name Bird: $bird</h2></p>
<img src="$img" size="100x100">
""")
