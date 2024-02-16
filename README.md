# **PADELCHIQUITO**

## **Descripción**

Este proyecto de Django, denominado "Padel Chiquito", es una plataforma avanzada dedicada a la comparación y revisión de palas de pádel. Utilizando Django como framework principal, hemos diseñado una experiencia de usuario intuitiva y eficiente. La interfaz del sitio se ha desarrollado con Tailwind CSS, garantizando un diseño responsivo y moderno.

Una característica destacada del proyecto es la inclusión de un programa ejecutable que automatiza el proceso de scraping para obtener precios actualizados de palas de pádel de diferentes tiendas en línea. Estos precios se integran directamente en la base de datos de "Padel Chiquito" para mantener la información al día, asegurando que los usuarios tengan acceso a los precios más recientes.

## **Características Principales**

### **Comparador de Palas**
![image](https://github.com/aritzjl/PadelChiquito/assets/129123101/5dc07007-5e98-4632-b5de-f5b6d0cf2cc7)

Los usuarios pueden filtrar y comparar palas de pádel basándose en especificaciones detalladas como la forma, el balance, el tacto, y otras características técnicas importantes. Este enfoque en las especificaciones técnicas, por encima de los precios y tiendas, permite a los usuarios tomar decisiones informadas basadas en lo que más valoran en una pala.
![image](https://github.com/aritzjl/PadelChiquito/assets/129123101/7c657cdf-4e8f-4ebe-8f7c-bcd3d97f0f05)


### **Actualización de Precios mediante Scraping**

Un script de scraping ejecutable se encarga de recopilar información de precios de múltiples tiendas en línea, actualizando automáticamente la base de datos del sitio. Esto mantiene a los usuarios informados sobre las mejores ofertas disponibles sin tener que visitar diferentes sitios web.

### **Panel de Administración Avanzado**
![image](https://github.com/aritzjl/PadelChiquito/assets/129123101/e6a202af-7a1b-47c7-a458-97c7592928fb)


El proyecto incluye un panel de administración personalizado que permite al cliente gestionar de manera eficiente todos los aspectos del sitio web. Desde la actualización de información de palas hasta la configuración de códigos promocionales para tiendas, este panel asegura una administración completa del contenido y las promociones del sitio.

### **Soporte para Códigos Promocionales**
![image](https://github.com/aritzjl/PadelChiquito/assets/129123101/a41dd90f-926c-4ff4-9414-5bc6823210e7)

Los administradores pueden crear y gestionar códigos promocionales específicos para tiendas, incentivando a los usuarios a realizar compras a través de la plataforma. Esta característica añade un valor adicional tanto para los usuarios como para las tiendas asociadas.

### **Sistema de Comentarios**
![image](https://github.com/aritzjl/PadelChiquito/assets/129123101/a6fc8498-287d-4747-bfe6-cd76a4a9cfa1)

El proyecto integra un sistema de comentarios robusto, permitiendo a los usuarios compartir sus opiniones y experiencias sobre las distintas palas de pádel. Este sistema fomenta una comunidad activa donde los usuarios pueden realizar preguntas, ofrecer consejos y proporcionar valoraciones detalladas sobre el rendimiento y la calidad de las palas. Los comentarios son una herramienta invaluable para ayudar a otros usuarios a tomar decisiones informadas basadas en experiencias reales de la comunidad.

### **Gestión de Emails**
![image](https://github.com/aritzjl/PadelChiquito/assets/129123101/68110e48-6242-439c-9d86-6ca7fde0fd62)

![image](https://github.com/aritzjl/PadelChiquito/assets/129123101/d027d77c-d173-4dd5-8d39-f621e05c9a67)

"Padel Chiquito" implementa un sistema de gestión de emails avanzado, utilizado para la verificación de cuentas, recuperación de contraseñas y notificaciones promocionales. Este sistema asegura que los usuarios puedan fácilmente verificar sus cuentas y restablecer contraseñas de manera segura, mejorando la experiencia del usuario. Además, permite al administrador enviar códigos promocionales y ofertas especiales directamente a los usuarios, incentivando la fidelidad y el compromiso con la plataforma.

## **Tecnologías Utilizadas**

- **Backend:** Django
- **Frontend:** HTML, CSS (Tailwind CSS), JavaScript
- **Base de Datos:** PostgreSQL (recomendado para producción), SQLite (para desarrollo)
- **Herramientas de Scraping:** Scripts personalizados en Python

## **Cómo Empezar**

Para poner en marcha el proyecto localmente, sigue estos pasos:

1. Clona el repositorio a tu máquina local.
2. Asegúrate de tener Python instalado y configura un entorno virtual dentro del directorio del proyecto.
3. Instala las dependencias utilizando **`pip install -r requirements.txt`**.
4. Realiza las migraciones de Django con **`python manage.py migrate`** para configurar la base de datos.
5. Inicia el servidor de desarrollo con **`python manage.py runserver`**.
6. Visita **`http://127.0.0.1:8000/`** en tu navegador para acceder al sitio.
