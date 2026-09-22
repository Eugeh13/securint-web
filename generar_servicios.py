#!/usr/bin/env python3
"""Genera las páginas de servicio en servicios/<slug>.html a partir de los datos de abajo.

Uso: python3 generar_servicios.py
Edita los textos aquí y vuelve a correrlo. index.html se mantiene a mano.
"""
from pathlib import Path

RAIZ = Path(__file__).parent
SALIDA = RAIZ / "servicios"

ICONOS = {
    "ejecutivos": '<svg viewBox="0 0 24 24"><path d="M12 3l7 3v5c0 5-3.5 8.5-7 10-3.5-1.5-7-5-7-10V6l7-3z"/><circle cx="12" cy="10" r="2.2"/><path d="M8.5 16.5c.8-1.8 2-2.6 3.5-2.6s2.7.8 3.5 2.6"/></svg>',
    "riesgo": '<svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5"/><path d="M8.5 11h5M11 8.5v5"/></svg>',
    "oficiales": '<svg viewBox="0 0 24 24"><circle cx="12" cy="7" r="3.5"/><path d="M5 21c0-4 3-6.5 7-6.5s7 2.5 7 6.5"/><path d="M12 14.5v6.5"/></svg>',
    "electronica": '<svg viewBox="0 0 24 24"><rect x="3" y="6" width="13" height="9" rx="2"/><path d="M16 9.5l5-2.5v8l-5-2.5"/><path d="M7 18.5h5M9.5 15v3.5"/></svg>',
    "inteligencia": '<svg viewBox="0 0 24 24"><path d="M3 12s3.5-6 9-6 9 6 9 6-3.5 6-9 6-9-6-9-6z"/><circle cx="12" cy="12" r="2.8"/></svg>',
    "consultoria": '<svg viewBox="0 0 24 24"><path d="M4 19h16"/><path d="M6 19V9l6-4 6 4v10"/><path d="M10 19v-5h4v5"/></svg>',
}

SERVICIOS = [
    {
        "clave": "ejecutivos",
        "slug": "proteccion-ejecutiva",
        "nombre": "Protección a ejecutivos y familias",
        "corto": "Protección ejecutiva",
        "eyebrow": "Protección ejecutiva",
        "resumen": "Prevención de secuestro y extorsión para ejecutivos, familias y personal clave.",
        "foto": "serv-ejecutivos.jpg",
        "alt": "Agente de protección abriendo la puerta del vehículo a un ejecutivo",
        "chips": ["Ruta alterna lista", "Protocolo de emergencia"],
        "titulo": "Protección que empieza antes de que exista la amenaza",
        "lead": "El sistema más moderno de protección a ejecutivos y familias, con un enfoque totalmente preventivo. Nuestros consultores le ayudan a prever el riesgo para que usted, su familia o su empresa no sufran un atentado con fines de secuestro o extorsión.",
        "contexto_titulo": "El riesgo ya no es sólo para el alto perfil",
        "contexto": "La violencia con la que actúan los criminales y la frecuencia de sus operaciones se han convertido en un tema de preocupación entre empresarios y ejecutivos. Las víctimas potenciales han aumentado en poco tiempo: los criminales ya no buscan sólo blancos de alto perfil, ahora la selección es más variada e incluye a medianos y pequeños propietarios de negocios.",
        "cita": "Ante este escenario, estamos convencidos de que la principal herramienta para combatirlo es la prevención.",
        "incluye": [
            ("Análisis de riesgos reales", "Estudiamos la rutina del ejecutivo, sus traslados, su entorno familiar y su exposición pública para identificar los riesgos reales, no los supuestos."),
            ("Plan de acción", "Medidas priorizadas por impacto y facilidad de implementación, con responsables y tiempos."),
            ("Procedimientos de emergencia", "Qué hacer, quién llama a quién y por dónde moverse ante un intento de secuestro, extorsión o emergencia médica."),
            ("Rutas y traslados seguros", "Diseño de rutas principales y alternas, puntos seguros y protocolos de abordaje y descenso."),
            ("Capacitación al círculo cercano", "Ejecutivos, familia, choferes y personal doméstico aprenden a detectar vigilancia y a reaccionar."),
            ("Acompañamiento y seguimiento", "Revisión periódica del plan cuando cambian la agenda, el domicilio o el entorno."),
        ],
        "pasos": [
            ("Entrevista confidencial", "Entendemos su situación, su familia y su empresa en una conversación privada."),
            ("Evaluación de vulnerabilidad", "Analizamos rutinas, traslados, domicilio y oficina."),
            ("Plan y capacitación", "Entregamos el plan, lo implementamos y entrenamos a las personas clave."),
            ("Seguimiento", "Ajustamos el plan cuando cambia el contexto."),
        ],
        "para": ["Directores y dueños de empresa", "Familias empresariales", "Personal clave con exposición", "Empresarios medianos y pequeños"],
        "cta": "Solicitar una entrevista confidencial",
    },
    {
        "clave": "riesgo",
        "slug": "evaluaciones-de-riesgo",
        "nombre": "Evaluaciones de riesgo",
        "corto": "Evaluaciones de riesgo",
        "eyebrow": "Diagnóstico",
        "resumen": "Análisis de vulnerabilidad de instalaciones, ejecutivos y familia antes de proponer cualquier medida.",
        "foto": "serv-riesgo.jpg",
        "alt": "Consultor revisando el perímetro de una planta industrial con una tableta",
        "chips": ["Agenda de riesgos", "Perímetro · Accesos · Rutinas"],
        "titulo": "Primero entender el riesgo, después decidir qué proteger",
        "lead": "Antes de presentar cualquier propuesta realizamos un análisis de vulnerabilidad de las instalaciones, de usted, su familia y los ejecutivos de su empresa. Así ofrecemos únicamente las contramedidas necesarias, sin equipo ni personal de más.",
        "contexto_titulo": "Ninguna propuesta sale sin un análisis previo",
        "contexto": "Es común que las empresas compren cámaras, guardias o equipo sin saber qué están cubriendo realmente. Nuestro método invierte el orden: visitamos las instalaciones, entendemos la operación y las rutinas, y sólo entonces determinamos las necesidades reales de equipamiento y personal.",
        "cita": "El resultado es una agenda de riesgos: un documento que dice qué proteger primero y qué no hace falta comprar.",
        "incluye": [
            ("Visita y recorrido de instalaciones", "Perímetro, accesos, estacionamientos, áreas críticas y horarios de operación."),
            ("Análisis de rutinas del ejecutivo", "Traslados, domicilio, agenda pública y exposición en redes."),
            ("Agenda de riesgos", "Riesgos identificados, priorizados por probabilidad e impacto."),
            ("Plan de acción", "Mejoras propuestas con alcance, tiempos de ejecución, entregables y costo por etapa."),
            ("Reporte quincenal de actividades", "Durante la evaluación, usted sabe en qué se avanza."),
            ("Presentación a dirección", "Explicamos los hallazgos y las prioridades al comité o al dueño."),
        ],
        "pasos": [
            ("Reunión inicial", "Definimos alcance: instalaciones, personas o ambos."),
            ("Trabajo de campo", "Recorridos, entrevistas y revisión de procedimientos actuales."),
            ("Agenda de riesgos", "Documento final con prioridades y plan de acción."),
            ("Decisión", "Usted elige qué etapas implementar y con quién."),
        ],
        "para": ["Plantas industriales", "Corporativos y oficinas", "Hospitales y clínicas", "Residencias y familias"],
        "cta": "Agendar una evaluación",
    },
    {
        "clave": "oficiales",
        "slug": "oficiales-de-seguridad",
        "nombre": "Oficiales de seguridad",
        "corto": "Oficiales de seguridad",
        "eyebrow": "Vigilancia",
        "resumen": "Vigilancia humana con personal de alta permanencia y tecnología incluida en cada punto de servicio.",
        "foto": "serv-oficiales.jpg",
        "alt": "Oficial de seguridad uniformado en la recepción de un edificio corporativo",
        "chips": ["Punto de servicio · 24 h", "4 cámaras en comodato"],
        "titulo": "Personal que se queda, con tecnología que lo respalda",
        "lead": "El sueldo que ofrecemos a nuestros elementos es de los más altos del mercado. Eso nos permite un reclutamiento constante de personal competente, con el deseo de formar parte del equipo, y garantiza un porcentaje de rotación muy bajo.",
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
        "eyebrow": "Tecnología",
        "resumen": "CCTV, control de acceso y centros de monitoreo: ingeniería, venta, renta, instalación y mantenimiento.",
        "foto": "serv-electronica.jpg",
        "alt": "Sala de monitoreo con pared de pantallas de CCTV y un operador",
        "chips": ["Control de acceso", "Centro de monitoreo"],
        "titulo": "Sistemas diseñados para su operación, no del catálogo",
        "lead": "Diseñamos, instalamos y mantenemos los sistemas de videovigilancia y control de acceso que hacen posible una seguridad integral. Antes de proponer equipo, analizamos el riesgo de las instalaciones para determinar las necesidades reales.",
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
    {
        "clave": "inteligencia",
        "slug": "inteligencia",
        "nombre": "Inteligencia y contrainteligencia",
        "corto": "Inteligencia",
        "eyebrow": "Inteligencia",
        "resumen": "Investigaciones, estudios sociales y contramedidas para proteger la información de su empresa y su familia.",
        "foto": "serv-inteligencia.jpg",
        "alt": "Técnico revisando una sala de juntas con un detector de dispositivos",
        "chips": ["Barrido electrónico", "Comunicación cifrada"],
        "titulo": "Saber más que quien lo observa",
        "lead": "Como parte del ciclo de inteligencia estratégica, nos especializamos en investigaciones y estudios sociales, y en contramedidas técnicas para proteger la información de su empresa y de su familia.",
        "contexto_titulo": "La información también es un activo que protege vidas",
        "contexto": "Antes de un secuestro o una extorsión hay vigilancia, recopilación de información y, muchas veces, alguien de confianza que la filtra. Investigar a tiempo, detectar dispositivos clandestinos y cifrar las comunicaciones del personal clave cierra esas puertas.",
        "cita": "Discreción absoluta: cada caso se maneja con un solo punto de contacto y sin dejar rastro en su operación.",
        "incluye": [
            ("Investigaciones", "Verificación de personas, proveedores y socios; estudios sociales y de entorno."),
            ("Detección de dispositivos clandestinos", "Barridos electrónicos en oficinas, salas de juntas, vehículos y residencias."),
            ("Comunicación celular cifrada", "Software de cifrado de punta a punta para familias y personal clave de la empresa."),
            ("Redes de comunicación segura", "Grupos cerrados de comunicación para directivos y familia."),
            ("Contrainteligencia", "Identificación de fugas de información y vigilancia hostil."),
            ("Informe confidencial", "Hallazgos y recomendaciones entregados en persona."),
        ],
        "pasos": [
            ("Consulta privada", "Un solo interlocutor, sin registro en su operación."),
            ("Recolección y análisis", "Investigación, barridos o verificaciones según el caso."),
            ("Informe", "Hallazgos, evidencia y recomendaciones."),
            ("Contramedidas", "Implementación de cifrado, protocolos o cambios de personal."),
        ],
        "para": ["Consejos y direcciones generales", "Familias empresariales", "Áreas legales y de recursos humanos", "Empresas con información sensible"],
        "cta": "Consultar en privado",
    },
    {
        "clave": "consultoria",
        "slug": "consultoria-y-capacitacion",
        "nombre": "Consultoría y capacitación",
        "corto": "Consultoría y capacitación",
        "eyebrow": "Consultoría",
        "resumen": "Comités de crisis, procedimientos de emergencia y cursos para guardias y ejecutivos.",
        "foto": "serv-consultoria.jpg",
        "alt": "Instructor de seguridad capacitando a un grupo de ejecutivos",
        "chips": ["Entrenamiento", "Comité de crisis"],
        "titulo": "Que su organización sepa qué hacer antes, durante y después",
        "lead": "Servicios estratégicos para que la empresa no dependa de la improvisación: un comité de crisis conformado y entrenado, procedimientos claros y personas capacitadas para reaccionar.",
        "contexto_titulo": "Un incidente se resuelve con lo que se preparó antes",
        "contexto": "Cuando ocurre un secuestro, una extorsión o una emergencia en planta, las primeras horas definen el desenlace. Un comité de crisis con roles claros, procedimientos escritos y gente que ya practicó la respuesta cambia por completo el resultado.",
        "cita": "Capacitamos a quien tiene que decidir y a quien tiene que ejecutar: directivos, familia y guardias.",
        "incluye": [
            ("Comité de manejo de crisis", "Conformación, roles, protocolos de decisión y entrenamiento con simulacros."),
            ("Procedimientos de emergencia", "Documentos operativos para secuestro, extorsión, intrusión y emergencias médicas."),
            ("Capacitación a guardias", "Consignas, control de acceso, detección de vigilancia y reporte de incidentes."),
            ("Capacitación a ejecutivos", "Conciencia situacional, hábitos seguros y manejo de extorsión telefónica."),
            ("Manejo defensivo y evasivo", "Curso práctico para choferes y ejecutivos que conducen su propio vehículo."),
            ("Evaluación de resultados", "Simulacros y auditorías para comprobar que el entrenamiento funciona."),
        ],
        "pasos": [
            ("Diagnóstico", "Qué procedimientos existen y qué falta."),
            ("Diseño del programa", "Comité, procedimientos y cursos a la medida."),
            ("Capacitación", "Sesiones teóricas y prácticas con su gente."),
            ("Simulacro y ajuste", "Probamos el plan y corregimos lo que no funcionó."),
        ],
        "para": ["Direcciones generales y consejos", "Recursos humanos y seguridad interna", "Familias empresariales", "Empresas con guardias propios"],
        "cta": "Diseñar un programa",
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
          <a class="mega__pie" href="../index.html#contacto">¿No sabe por dónde empezar? Solicite una evaluación de riesgo →</a>
        </div>
      </div>
      <a href="../index.html#proceso">Cómo trabajamos</a>
      <a href="../index.html#porque">Por qué Securint</a>
      <a href="../index.html#contacto">Contacto</a>
      <a class="boton boton--primario boton--chico" href="../index.html#contacto">Solicitar evaluación</a>
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
