# Sitio web de Securint

Página corporativa de una sola vista para securint.com.mx. HTML, CSS y JS planos, sin build.

- `index.html` — página de inicio (a mano)
- `servicios/*.html` — una página por servicio. **No se editan a mano**: se generan con `python3 generar_servicios.py`, que tiene los textos de los seis servicios
- `css/styles.css` — estilos (tokens al inicio del archivo)
- `js/main.js` — menú móvil, animaciones de aparición y formulario de contacto
- `assets/img/` — fotos optimizadas para web (~200 KB); los originales viven en `insumos/fotos-originales/`
- `insumos/` — material original (logo, presentación PPT); no se publica

Preview local: `python3 -m http.server 8765` y abrir http://127.0.0.1:8765

## Publicación

El sitio se sirve con **GitHub Pages** desde la rama `main` (raíz del repo). Cada push a `main` actualiza el sitio en uno o dos minutos.

- URL provisional: https://eugeh13.github.io/securint-web/
- Dominio: `securint.com.mx` (GoDaddy). Los registros DNS apuntan a GitHub Pages; el archivo `CNAME` en la raíz fija el dominio.

Datos de contacto: están en `js/main.js` (constante `CONTACTO`) y en la sección de contacto de `index.html`.
