# Motor de Búsqueda Semántica con FastAPI y Supabase

En este proyecto, vamos a crear una **API REST** para un motor de búsqueda semántica.

---

## 🚀 Características

- **API REST**: Expone dos _endpoints_ principales: uno para insertar documentos y otro para realizar búsquedas semánticas.
- **Base de Datos Vectorial**: Utiliza **Supabase** con la extensión `pgvector` para almacenar y consultar _embeddings_.
- **Generación de Embeddings**: Usa el modelo `paraphrase-multilingual-MiniLM-L12-v2` de la librería `Sentence Transformers` para generar los vectores.
- **Entorno de Desarrollo**: Configuración con Python y un entorno virtual.
- **Documentación Automática**: FastAPI genera automáticamente la documentación interactiva con Swagger UI.

---

## 🛠️ Requisitos

Para poder seguir este proyecto, necesitarás:

- **Python 3.8+** instalado.
- Una cuenta en **Supabase**.

---

## 💻 Configuración del Proyecto

### 1. Clonar el Repositorio

Primero, clona este repositorio a tu máquina local usando `git`:

```bash
git clone git@github.com:codigoarqui/api_motor_semantico.git
cd api_motor_semantico
```

### 2. Configurar Supabase

Si aún no lo has hecho, ve a [Supabase](https://supabase.com) y crea un nuevo proyecto.

Una vez que el proyecto esté creado, sigue estos pasos:

1.  Ve al **SQL editor** y ejecuta el siguiente script para activar la extensión `pgvector`:
    ```sql
    create extension if not exists vector;
    ```
2.  Crea la tabla donde se almacenarán nuestros documentos y _embeddings_. Recuerda que el campo `embedding` debe coincidir con las dimensiones del modelo que usamos (384 en este caso).

    ```sql
    create table documentos (
      id uuid primary key default gen_random_uuid(),
      texto text,
      metadatos jsonb,
      embedding vector(384)
    );
    ```

3.  Crea la función RPC `buscar_similares` para realizar las búsquedas eficientes con el operador `<->`.
    ```sql
    create or replace function buscar_similares(query vector(384), top_k int)
    returns table(id uuid, texto text, metadatos jsonb)
    language sql stable
    as $$
      select id, texto, metadatos
      from documentos
      order by embedding <-> query
      limit top_k;
    $$;
    ```

### 3. Configurar el Entorno de Python

Desde la terminal, en la raíz del proyecto, crea y activa un entorno virtual de Python.

**Para Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Para macOS y Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar Dependencias

Con el entorno virtual activado, instala todas las librerías necesarias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Configurar Variables de Entorno

1.  Copia el archivo `.env.example` y renómbralo a `.env`.
2.  Ve a tu proyecto de Supabase, en la sección **Project Settings** > **Data API**.
3.  Copia la **Project URL** y pégala como el valor de `SUPABASE_URL` en tu archivo `.env`.
4.  Luego, en **API Keys**, copia la clave pública `anon` y pégala como el valor de `SUPABASE_KEY`.

Tu archivo `.env` debería verse así:

```ini
SUPABASE_URL="https://tuproyecto.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI..."
```

---

## ▶️ Ejecutar la API

Con toda la configuración lista, puedes ejecutar la API localmente usando `uvicorn`:

```bash
uvicorn main:app --reload
```

Una vez que el servidor esté corriendo, verás un mensaje en tu terminal indicando la dirección.

---

## 🔍 Probar los Endpoints

La API de FastAPI genera automáticamente una documentación interactiva con **Swagger UI**. Puedes acceder a ella abriendo tu navegador y yendo a la siguiente URL:

```
http://localhost:8000/docs
```

Desde esta página, puedes probar ambos _endpoints_ de la API:

- **`POST /documentos/`**: Para insertar nuevos documentos con sus respectivos _embeddings_ en la base de datos de Supabase.
- **`POST /buscar/`**: Para realizar una búsqueda semántica. Solo necesitas ingresar una consulta de texto y la API devolverá los documentos más relevantes.

¡Y eso es todo! Con esto ya tienes tu API de búsqueda semántica funcionando, lista para ser consumida por cualquier aplicación.

---

Si te ha sido útil, no olvides suscribirte a mi canal **Del Código a la Arquitectura** para más. ¡Nos vemos en la próxima! 🚀
