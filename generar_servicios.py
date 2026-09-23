#!/usr/bin/env python3
"""Genera las páginas de servicio en servicios/<slug>.html a partir de los datos de abajo.

Uso: python3 generar_servicios.py
Edita los textos aquí y vuelve a correrlo. index.html se mantiene a mano.
"""
from pathlib import Path

RAIZ = Path(__file__).parent
SALIDA = RAIZ / "servicios"

ICONOS = {
    "inteligencia": '<svg viewBox="0 0 24 24"><path d="M3 12s3.5-6 9-6 9 6 9 6-3.5 6-9 6-9-6-9-6z"/><circle cx="12" cy="12" r="2.8"/></svg>',
    "contra": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="2"/><path d="M8.5 8.5a5 5 0 0 0 0 7M15.5 8.5a5 5 0 0 1 0 7"/><path d="M5.5 5.5a9 9 0 0 0 0 13M18.5 5.5a9 9 0 0 1 0 13"/></svg>',
    "ejecutivos": '<svg viewBox="0 0 24 24"><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6l7-3z"/><circle cx="12" cy="10" r="2.2"/><path d="M8.5 16.5c.8-1.8 2-2.6 3.5-2.6s2.7.8 3.5 2.6"/></svg>',
    "oficiales": '<svg viewBox="0 0 24 24"><circle cx="12" cy="7" r="3.5"/><path d="M5 21c0-4 3-6.5 7-6.5s7 2.5 7 6.5"/><path d="M12 14.5v6.5"/></svg>',
    "electronica": '<svg viewBox="0 0 24 24"><rect x="3" y="6" width="13" height="9" rx="2"/><path d="M16 9.5l5-2.5v8l-5-2.5"/><path d="M7 18.5h5M9.5 15v3.5"/></svg>',
}

SERVICIOS = [
    {
        "clave": "inteligencia",
        "slug": "inteligencia",
        "nombre": "Inteligencia",
        "corto": "Inteligencia",
        "eyebrow": "Servicio principal · Inteligencia",
        "resumen": "Investigaciones, agenda de riesgos y manejo de crisis para decidir con información, no con suposiciones.",
        "foto": "serv-riesgo.jpg",
        "alt": "Consultor de Securint analizando el perímetro de una planta con una tableta",
        "chips": ["Agenda de riesgos", "Comité de crisis"],
        "titulo": "Decidir con información, no con suposiciones",
        "lead": "Como parte del ciclo de inteligencia estratégica, investigamos personas, entornos y situaciones; construimos la agenda de riesgos de su empresa o su familia; y preparamos a su organización para manejar una crisis antes de que ocurra.",
        "contexto_titulo": "Antes de un incidente siempre hubo señales que nadie leyó",
        "contexto": "Un secuestro, una extorsión o una fuga de información rara vez son una sorpresa: hay señales en el entorno, en las personas cercanas y en la rutina. El trabajo de inteligencia consiste en recoger esas señales a tiempo, ordenarlas en una agenda de riesgos y convertirlas en decisiones y procedimientos.",
        "cita": "La agenda de riesgos dice qué proteger primero. El comité de crisis dice quién decide cuando algo pasa.",
        "incluye": [
            ("Investigaciones", "Verificación de personas, proveedores, socios y empleados clave. Estudios sociales y de entorno."),
            ("Análisis de riesgos", "Etapa 1 de todo servicio: evaluación de vulnerabilidad de instalaciones, ejecutivos y familia."),
            ("Agenda de riesgos", "Documento con los riesgos priorizados y un plan de acción con alcance, tiempos, entregables y costo."),
            ("Manejo de crisis", "Conformación y entrenamiento del comité de manejo de crisis: roles, protocolos de decisión y simulacros."),
            ("Procedimientos de emergencia", "Qué hacer, quién decide y a quién llamar ante secuestro, extorsión, intrusión o emergencia médica."),
            ("Informe confidencial y seguimiento", "Hallazgos y recomendaciones entregados en persona. Revisión periódica de la agenda."),
        ],
        "pasos": [
            ("Consulta privada", "Un solo interlocutor. Entendemos su situación sin dejar rastro en su operación."),
            ("Recolección y análisis", "Investigaciones, entrevistas y recorridos según el caso."),
            ("Agenda de riesgos", "Prioridades y plan de acción presentados a la dirección."),
            ("Comité y procedimientos", "Conformamos y entrenamos a quienes tendrán que decidir."),
        ],
        "para": ["Consejos y direcciones generales", "Familias empresariales", "Áreas legales y de recursos humanos", "Empresas con operaciones expuestas"],
        "cta": "Contactar a un consultor",
    },
    {
        "clave": "contra",
        "slug": "contrainteligencia",
        "nombre": "Contrainteligencia",
        "corto": "Contrainteligencia",
        "eyebrow": "Servicio principal · Contrainteligencia",
        "resumen": "Barridos electrónicos, seguridad en comunicaciones y equipo táctico para que nadie escuche lo que no debe.",
        "foto": "serv-inteligencia.jpg",
        "alt": "Técnico de Securint realizando un barrido electrónico en una sala de juntas con un detector de radiofrecuencia",
        "chips": ["Barrido electrónico", "Comunicación cifrada"],
        "titulo": "Que nadie escuche lo que no debe",
        "lead": "Detectamos y neutralizamos la vigilancia hostil: barridos electrónicos en oficinas, salas de juntas, vehículos y residencias; comunicaciones cifradas para directivos y familia; y equipo táctico para investigaciones y contramedidas.",
        "contexto_titulo": "La información se fuga por donde nadie mira",
        "contexto": "Un micrófono en la sala de juntas, una cámara en la oficina del director o un teléfono intervenido valen más para un criminal que cualquier cerradura. La contrainteligencia cierra esas puertas: encuentra los dispositivos, protege las conversaciones y equipa a su gente para operar con discreción.",
        "cita": "Un solo punto de contacto, sin registro en su operación, y un informe entregado en persona.",
        "incluye": [
            ("Barridos electrónicos", "Detección de dispositivos clandestinos de audio y video en oficinas, salas de juntas, vehículos y residencias."),
            ("Seguridad en comunicaciones", "Telefonía celular cifrada de punta a punta, con instalación remota, y redes de comunicación segura para familia y personal clave."),
            ("Equipo táctico", "Equipos para investigaciones y contramedidas, con asesoría sobre su operación y su uso conforme a la ley."),
            ("Detección de vigilancia hostil", "Identificación de seguimiento y observación sobre ejecutivos, familia e instalaciones."),
            ("Protocolos de confidencialidad", "Manejo de información sensible en juntas, viajes, dispositivos y personal de confianza."),
            ("Informe y contramedidas", "Evidencia, hallazgos y medidas aplicadas, con verificación periódica."),
        ],
        "pasos": [
            ("Consulta privada", "Sin correos ni registros: una conversación directa con el consultor."),
            ("Barrido y diagnóstico", "Revisión técnica de los espacios, vehículos y dispositivos acordados."),
            ("Contramedidas", "Retiro de dispositivos, cifrado de comunicaciones y protocolos."),
            ("Verificación periódica", "Barridos programados antes de juntas o negociaciones críticas."),
        ],
        "para": ["Direcciones generales y consejos", "Familias empresariales", "Áreas legales y financieras", "Empresas en negociaciones sensibles"],
        "cta": "Consultar en privado",
    },
    {
        "clave": "ejecutivos",
        "slug": "proteccion-ejecutiva",
        "nombre": "Protección ejecutiva",
        "corto": "Protección ejecutiva",
        "eyebrow": "Servicio principal · Protección ejecutiva",
        "resumen": "Análisis de riesgos y entrenamiento de escoltas, guardias, ejecutivos y sus familias para prevenir secuestro y extorsión.",
        "foto": "serv-consultoria.jpg",
        "alt": "Consultor de Securint capacitando a un grupo de ejecutivos en una sala de juntas",
        "chips": ["Análisis de riesgos", "Entrenamiento"],
        "titulo": "La mejor protección es un ejecutivo preparado",
        "lead": "Un programa preventivo que empieza por el análisis de riesgos del ejecutivo y su familia, y continúa con el entrenamiento de quienes los protegen y de ellos mismos. Los servicios de escolta y transporte pueden integrarse cuando el análisis lo justifica, pero el centro del programa es la prevención.",
        "contexto_titulo": "El riesgo ya no es sólo para el alto perfil",
        "contexto": "La violencia con la que actúan los criminales y la frecuencia de sus operaciones se han convertido en un tema de preocupación entre empresarios y ejecutivos. Las víctimas potenciales han aumentado en poco tiempo: los criminales ya no buscan sólo blancos de alto perfil, ahora la selección es más variada e incluye a medianos y pequeños propietarios de negocios.",
        "cita": "Ante este escenario, la principal herramienta para combatirlo es la prevención: un ejecutivo, una familia y un equipo que saben qué hacer.",
        "incluye": [
            ("Análisis de riesgos", "Etapa 1: rutina del ejecutivo, traslados, domicilio, exposición pública y entorno familiar."),
            ("Plan de acción y procedimientos", "Medidas priorizadas y procedimientos de emergencia para secuestro, extorsión y traslados."),
            ("Entrenamiento de escoltas", "Selección, evaluación y capacitación de escoltas y choferes en protección preventiva."),
            ("Capacitación de guardias", "Consignas, control de acceso, detección de vigilancia y reporte de incidentes."),
            ("Entrenamiento del ejecutivo y su familia", "Conciencia situacional, hábitos seguros, extorsión telefónica, rutas y traslados."),
            ("Manejo defensivo y evasivo", "Curso práctico para choferes y para ejecutivos que conducen su propio vehículo."),
        ],
        "pasos": [
            ("Entrevista confidencial", "Entendemos su situación, su familia y su empresa en una conversación privada."),
            ("Análisis de riesgos", "Rutinas, traslados, domicilio y oficina."),
            ("Plan y entrenamiento", "Procedimientos, escoltas, guardias, ejecutivo y familia."),
            ("Seguimiento", "Ajustamos el programa cuando cambia el contexto."),
        ],
        "para": ["Directores y dueños de empresa", "Familias empresariales", "Equipos de escoltas y choferes", "Guardias de seguridad interna"],
        "cta": "Contactar a un consultor",
    },
    {
        "clave": "oficiales",
        "slug": "oficiales-de-seguridad",
        "nombre": "Oficiales de seguridad",
        "corto": "Oficiales de seguridad",
        "eyebrow": "Servicio complementario · Vigilancia",
        "resumen": "Vigilancia humana con personal de alta permanencia y tecnología incluida en cada punto de servicio.",
        "foto": "serv-oficiales.jpg",
        "alt": "Oficial de seguridad uniformado en la recepción de un edificio corporativo",
        "chips": ["Punto de servicio · 24 h", "4 cámaras en comodato"],
        "titulo": "Personal que se queda, con tecnología que lo respalda",
        "lead": "Complemento operativo de la consultoría: cuando el análisis de riesgos lo indica, ponemos oficiales en sus instalaciones. El sueldo que ofrecemos a nuestros elementos es de los más altos del mercado, lo que nos permite reclutamiento constante y una rotación muy baja.",
        "contexto_titulo": "Vigilancia humana complementada con vigilancia electrónica",
        "contexto": "Manejamos esquemas atractivos y, sobre todo, efectivos de seguridad. Con un contrato mínimo de un punto de servicio de 24 horas, entregamos al cliente sin ningún costo y en comodato un sistema básico de cuatro cámaras de seguridad con visión nocturna y una grabadora digital, incluyendo cableado, instalación y configuración del equipo.",
        "cita": "Así ponemos a su disposición una seguridad más integral y profesional, acorde a los tiempos de alta criminalidad que vivimos.",
        "incluye": [
            ("Oficiales seleccionados y capacitados", "Reclutamiento continuo, verificación de antecedentes y entrenamiento en procedimientos."),
            ("Baja rotación", "Sueldos por encima del mercado para que el personal conozca su punto y a su cliente."),
            ("Sistema de 4 cámaras en comodato", "Con cada punto de 24 horas: cámaras con visión nocturna y grabadora digital, sin costo."),
            ("Instalación y configuración incluidas", "Cableado, montaje y puesta en marcha a cargo de nuestro equipo técnico."),
            ("Análisis de riesgo previo", "Dimensionamos el servicio según las necesidades reales de la instalación."),
            ("Supervisión y reportes", "Rondas de supervisión y reporte de novedades al cliente."),
        ],
        "pasos": [
            ("Análisis de la instalación", "Definimos puntos, turnos y consignas."),
            ("Asignación de personal", "Elementos seleccionados para su tipo de operación."),
            ("Instalación del equipo", "Cámaras y grabadora en comodato, listas antes de arrancar."),
            ("Operación y supervisión", "Consignas, rondas y reportes periódicos."),
        ],
        "para": ["Corporativos y oficinas", "Plantas y bodegas", "Comercio y plazas", "Residenciales y fraccionamientos"],
        "cta": "Cotizar un punto de servicio",
    },
    {
        "clave": "electronica",
        "slug": "seguridad-electronica",
        "nombre": "Seguridad electrónica",
        "corto": "Seguridad electrónica",
        "eyebrow": "Servicio complementario · Tecnología",
        "resumen": "CCTV, control de acceso y centros de monitoreo: ingeniería, venta, renta, instalación y mantenimiento.",
        "foto": "serv-electronica.jpg",
        "alt": "Sala de monitoreo con pared de pantallas de CCTV y un operador",
        "chips": ["Control de acceso", "Centro de monitoreo"],
        "titulo": "Sistemas diseñados para su operación, no del catálogo",
        "lead": "Complemento técnico de la consultoría: diseñamos, instalamos y mantenemos los sistemas de videovigilancia y control de acceso que el análisis de riesgos recomienda, sin equipo de más.",
        "contexto_titulo": "Ingeniería antes que equipo",
        "contexto": "Un sistema de cámaras mal ubicado da una falsa sensación de seguridad. Por eso empezamos por la ingeniería: qué zonas cubrir, con qué tipo de cámara, dónde grabar, quién monitorea y cómo se integra con el control de acceso y con el personal en sitio.",
        "cita": "Venta o renta, instalación, monitoreo y mantenimiento: un solo responsable de que el sistema funcione.",
        "incluye": [
            ("Ingeniería y reingeniería", "Diseño de sistemas nuevos o corrección de sistemas existentes de CCTV y control de acceso."),
            ("Venta y renta de equipos", "Esquemas de compra o renta según el horizonte de su proyecto."),
            ("Instalación y configuración", "Cableado, montaje, configuración de grabación y accesos remotos."),
            ("Centros de monitoreo", "Diseño y desarrollo de salas de monitoreo: pantallas, consolas y procedimientos."),
            ("Control de acceso", "Lectores, credenciales, torniquetes y bitácoras de entrada y salida."),
            ("Pólizas de mantenimiento", "Preventivo y correctivo para que el sistema no deje de grabar."),
        ],
        "pasos": [
            ("Análisis de riesgo", "Recorrido de la instalación y definición de zonas críticas."),
            ("Propuesta de ingeniería", "Planos, equipo, alcance y costo por etapa."),
            ("Instalación", "Montaje, configuración y pruebas con el cliente."),
            ("Mantenimiento", "Póliza y revisiones programadas."),
        ],
        "para": ["Plantas industriales", "Corporativos", "Hospitales", "Comercio y logística"],
        "cta": "Solicitar un proyecto",
    },
]

# ---------------------------------------------------------------- plantilla

def menu_servicios(actual):
    items = []
    for s in SERVICIOS:
        activo = ' aria-current="page"' if s["clave"] == actual else ""
        items.append(
            f'<a class="mega__item" href="{s["slug"]}.html"{activo}>'
            f'<span class="mega__icono">{ICONOS[s["clave"]]}</span>'
            f'<span><strong>{s["corto"]}</strong><small>{s["resumen"]}</small></span></a>'
        )
    return "\n            ".join(items)


def cabecera(actual):
    return f'''<header class="cabecera" id="inicio">
  <div class="contenedor cabecera__fila">
    <a class="cabecera__logo" href="../index.html" aria-label="Securint, inicio">
      <img src="../assets/logo.png" alt="Securint" width="158" height="49">
    </a>
    <button class="cabecera__menu" type="button" aria-expanded="false" aria-controls="nav" aria-label="Abrir menú">
      <span></span><span></span><span></span>
    </button>
    <nav class="nav" id="nav" aria-label="Principal">
      <div class="nav__grupo">
        <button class="nav__desplegable" type="button" aria-expanded="false" aria-controls="menu-servicios">
          Servicios
          <svg class="nav__flecha" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6l4 4 4-4"/></svg>
        </button>
        <div class="mega" id="menu-servicios">
          <div class="mega__grid">
            {menu_servicios(actual)}
          </div>
          <a class="mega__pie" href="../index.html#contacto">¿No sabe por dónde empezar? Contacte a un consultor →</a>
        </div>
      </div>
      <a href="../index.html#proceso">Cómo trabajamos</a>
      <a href="../index.html#porque">Por qué Securint</a>
      <a href="../index.html#direccion">Dirección</a>
      <a href="../index.html#contacto">Contacto</a>
      <a class="boton boton--primario boton--chico" href="../index.html#contacto">Contactar a un consultor</a>
    </nav>
  </div>
</header>'''


PIE = '''<footer class="pie">
  <div class="contenedor pie__fila">
    <div>
      <strong class="pie__marca">Securint S.A. de C.V.</strong>
      <span class="pie__sub">Seguridad privada con enfoque preventivo · Monterrey, N.L.</span>
    </div>
    <nav class="pie__nav" aria-label="Pie de página">
      <a href="../index.html#servicios">Servicios</a>
      <a href="../index.html#proceso">Cómo trabajamos</a>
      <a href="../index.html#direccion">Dirección</a>
      <a href="../index.html#contacto">Contacto</a>
    </nav>
    <span class="pie__copy">© <span id="anio"></span> Securint. Todos los derechos reservados.</span>
  </div>
</footer>'''


def otros_servicios(actual):
    otros = [s for s in SERVICIOS if s["clave"] != actual][:3]
    tarjetas = []
    for s in otros:
        tarjetas.append(f'''        <a class="serv-card serv-card--chica" href="{s["slug"]}.html">
          <div class="serv-card__foto"><img src="../assets/img/{s["foto"]}" alt="" width="1400" height="939" loading="lazy"></div>
          <div class="serv-card__cuerpo">
            <h3>{s["nombre"]}</h3>
            <p>{s["resumen"]}</p>
            <span class="serv-card__mas">Ver servicio <svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8h10M9 4l4 4-4 4"/></svg></span>
          </div>
        </a>''')
    return "\n".join(tarjetas)


def pagina(s):
    incluye = "\n".join(
        f'''        <li class="incluye-card">
          <span class="incluye-card__num">{i:02d}</span>
          <h3>{t}</h3>
          <p>{d}</p>
        </li>''' for i, (t, d) in enumerate(s["incluye"], 1))
    pasos = "\n".join(
        f'''        <li class="paso">
          <span class="paso__num">{i:02d}</span>
          <h3>{t}</h3>
          <p>{d}</p>
        </li>''' for i, (t, d) in enumerate(s["pasos"], 1))
    para = "\n".join(f'        <li>{p}</li>' for p in s["para"])
    chips = "".join(
        f'<span class="visual__chip visual__chip--{l}">{c}</span>' for l, c in zip("ab", s["chips"]))

    return f'''<!doctype html>
<html lang="es-MX">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{s["nombre"]} · Securint</title>
  <meta name="description" content="{s["resumen"]} Securint, seguridad privada con enfoque preventivo en Monterrey.">
  <meta property="og:title" content="{s["nombre"]} · Securint">
  <meta property="og:description" content="{s["resumen"]}">
  <meta property="og:type" content="website">
  <meta property="og:image" content="https://securint.com.mx/assets/img/{s["foto"]}">
  <meta name="theme-color" content="#071527">
  <link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@600;700;800&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/styles.css">
</head>
<body class="pagina-servicio">

<a class="saltar" href="#contenido">Ir al contenido</a>

{cabecera(s["clave"])}

<main id="contenido">

  <section class="hero hero--servicio">
    <div class="hero__fondo" aria-hidden="true">
      <img class="hero__foto" src="../assets/img/{s["foto"]}" alt="" width="1400" height="939" fetchpriority="high">
      <div class="hero__velo"></div>
    </div>
    <div class="contenedor hero__servicio">
      <nav class="migas" aria-label="Ubicación">
        <a href="../index.html">Inicio</a><span>/</span><a href="../index.html#servicios">Servicios</a><span>/</span><span aria-current="page">{s["corto"]}</span>
      </nav>
      <p class="etiqueta etiqueta--clara">{s["eyebrow"]}</p>
      <h1>{s["titulo"]}</h1>
      <p class="hero__bajada">{s["lead"]}</p>
      <div class="hero__acciones">
        <a class="boton boton--primario boton--grande" href="../index.html#contacto">{s["cta"]}</a>
        <a class="boton boton--fantasma" href="#incluye">Ver qué incluye</a>
      </div>
      <div class="hero__chips" aria-hidden="true">{chips}</div>
    </div>
  </section>

  <section class="seccion">
    <div class="contenedor contexto__grid">
      <div>
        <p class="etiqueta">El contexto</p>
        <h2>{s["contexto_titulo"]}</h2>
        <p class="parrafo">{s["contexto"]}</p>
      </div>
      <blockquote class="cita-grande">
        <p>{s["cita"]}</p>
        <footer>Securint · Enfoque preventivo</footer>
      </blockquote>
    </div>
  </section>

  <section class="seccion seccion--oscura" id="incluye">
    <div class="seccion__fondo" aria-hidden="true"></div>
    <div class="contenedor">
      <div class="seccion__cabeza">
        <p class="etiqueta etiqueta--clara">Qué incluye</p>
        <h2>Todo lo que forma parte de {s["corto"].lower()}</h2>
      </div>
      <ul class="incluye-grid">
{incluye}
      </ul>
    </div>
  </section>

  <section class="seccion">
    <div class="contenedor">
      <div class="seccion__cabeza">
        <p class="etiqueta">Cómo trabajamos</p>
        <h2>Así se desarrolla este servicio</h2>
      </div>
      <ol class="pasos pasos--claros">
{pasos}
      </ol>
    </div>
  </section>

  <section class="seccion seccion--para">
    <div class="contenedor para__grid">
      <div>
        <p class="etiqueta">Para quién</p>
        <h2>Pensado para</h2>
      </div>
      <ul class="para__lista">
{para}
      </ul>
    </div>
  </section>

  <section class="banda">
    <div class="contenedor banda__fila">
      <div>
        <h2>Hablemos de su caso.</h2>
        <p>Un consultor le responde para agendar una visita o una llamada, sin compromiso y con total confidencialidad.</p>
      </div>
      <a class="boton boton--primario boton--grande" href="../index.html#contacto">{s["cta"]}</a>
    </div>
  </section>

  <section class="seccion">
    <div class="contenedor">
      <div class="seccion__cabeza">
        <p class="etiqueta">Otros servicios</p>
        <h2>Lo que suele acompañar a este servicio</h2>
      </div>
      <div class="serv-grid serv-grid--tres">
{otros_servicios(s["clave"])}
      </div>
    </div>
  </section>

</main>

{PIE}

<script src="../js/main.js" defer></script>
</body>
</html>
'''


def main():
    SALIDA.mkdir(exist_ok=True)
    for s in SERVICIOS:
        destino = SALIDA / f'{s["slug"]}.html'
        destino.write_text(pagina(s), encoding="utf-8")
        print("escrito", destino.relative_to(RAIZ))


if __name__ == "__main__":
    main()
