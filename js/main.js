/* Securint — comportamiento de la página.
   Datos de contacto: cambiar aquí y se reflejan en toda la página. */

const CONTACTO = {
  telefono: "",          // ej. "+52 81 1234 5678"
  whatsapp: "",          // sólo dígitos con lada, ej. "528112345678"
  correo: "",            // ej. "contacto@securint.com.mx"
};

(function () {
  const movil = () => window.matchMedia("(max-width: 860px)").matches;

  // Año en el pie
  const anio = document.getElementById("anio");
  if (anio) anio.textContent = new Date().getFullYear();

  // Datos de contacto: si están definidos, reemplazan los marcadores "pendiente"
  const enlaces = {
    tel: CONTACTO.telefono && { href: "tel:" + CONTACTO.telefono.replace(/\s+/g, ""), texto: CONTACTO.telefono },
    whatsapp: CONTACTO.whatsapp && { href: "https://wa.me/" + CONTACTO.whatsapp, texto: "Escribir por WhatsApp" },
    correo: CONTACTO.correo && { href: "mailto:" + CONTACTO.correo, texto: CONTACTO.correo },
  };
  document.querySelectorAll("[data-contacto]").forEach((a) => {
    const dato = enlaces[a.dataset.contacto];
    if (!dato) return;
    a.href = dato.href;
    a.textContent = dato.texto;
    a.classList.remove("pendiente");
    if (a.dataset.contacto === "whatsapp") { a.target = "_blank"; a.rel = "noopener"; }
  });

  // ---------- Menú móvil ----------
  const botonMenu = document.querySelector(".cabecera__menu");
  const nav = document.getElementById("nav");
  const cerrarMenuMovil = () => {
    nav.classList.remove("abierto");
    botonMenu.setAttribute("aria-expanded", "false");
    botonMenu.setAttribute("aria-label", "Abrir menú");
  };
  if (botonMenu && nav) {
    botonMenu.addEventListener("click", () => {
      const abierto = nav.classList.toggle("abierto");
      botonMenu.setAttribute("aria-expanded", String(abierto));
      botonMenu.setAttribute("aria-label", abierto ? "Cerrar menú" : "Abrir menú");
    });
  }

  // ---------- Desplegable de servicios ----------
  const grupo = document.querySelector(".nav__grupo");
  const disparador = grupo && grupo.querySelector(".nav__desplegable");
  let temporizador = null;
  const abrirMega = () => { grupo.classList.add("abierto"); disparador.setAttribute("aria-expanded", "true"); };
  const cerrarMega = () => { grupo.classList.remove("abierto"); disparador.setAttribute("aria-expanded", "false"); };

  if (grupo && disparador) {
    disparador.addEventListener("click", () => {
      grupo.classList.contains("abierto") ? cerrarMega() : abrirMega();
    });
    // En escritorio también abre al pasar el cursor
    grupo.addEventListener("mouseenter", () => { if (!movil()) { clearTimeout(temporizador); abrirMega(); } });
    grupo.addEventListener("mouseleave", () => { if (!movil()) temporizador = setTimeout(cerrarMega, 180); });
    document.addEventListener("click", (ev) => { if (!grupo.contains(ev.target)) cerrarMega(); });
    document.addEventListener("keydown", (ev) => { if (ev.key === "Escape") { cerrarMega(); if (movil()) cerrarMenuMovil(); } });
  }

  // Cierra el menú móvil al elegir un enlace normal
  if (nav && botonMenu) {
    nav.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => { cerrarMega(); cerrarMenuMovil(); }));
  }

  // ---------- Aparición al hacer scroll ----------
  const objetivos = document.querySelectorAll(".paso, .razon, .franja__cita, .franja__respuesta, .seccion__cabeza, .serv-card, .incluye-card, .cita-grande, .banda__fila, .formulario, .datos");
  objetivos.forEach((el) => el.classList.add("aparece"));
  if ("IntersectionObserver" in window) {
    const obs = new IntersectionObserver(
      (entradas) => {
        entradas.forEach((e, i) => {
          if (!e.isIntersecting) return;
          e.target.style.transitionDelay = Math.min(i * 60, 240) + "ms";
          e.target.classList.add("visible");
          obs.unobserve(e.target);
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.1 }
    );
    objetivos.forEach((el) => obs.observe(el));
  } else {
    objetivos.forEach((el) => el.classList.add("visible"));
  }

  // ---------- Formulario ----------
  // Abre el correo del visitante con la solicitud prellenada.
  // Cuando haya un backend (Formspree, función de Vercel), se cambia aquí.
  const form = document.getElementById("formulario");
  const nota = document.getElementById("formulario-nota");
  if (form) {
    form.addEventListener("submit", (ev) => {
      ev.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      if (!CONTACTO.correo) {
        nota.textContent = "El correo de contacto aún no está configurado. Por favor llámenos o escríbanos por WhatsApp.";
        nota.className = "formulario__nota formulario__nota--error";
        return;
      }
      const d = new FormData(form);
      const asunto = "Solicitud de consultoría: " + d.get("interes");
      const cuerpo = [
        "Nombre: " + d.get("nombre"),
        "Empresa: " + (d.get("empresa") || "-"),
        "Teléfono: " + d.get("telefono"),
        "Correo: " + d.get("correo"),
        "Interés: " + d.get("interes"),
        "",
        d.get("mensaje") || "",
      ].join("\n");
      window.location.href = "mailto:" + CONTACTO.correo + "?subject=" + encodeURIComponent(asunto) + "&body=" + encodeURIComponent(cuerpo);
      nota.textContent = "Se abrió su aplicación de correo con la solicitud lista para enviar.";
      nota.className = "formulario__nota formulario__nota--ok";
    });
  }
})();
