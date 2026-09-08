from fpdf import FPDF
import os

class GuiaPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Calibri", "", 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "Portal de Herramientas de Soporte EPEM - Guia de aprendizaje", align="L")
        self.cell(0, 8, f"Pagina {self.page_no()}", align="R")
        self.ln(10)
        self.set_draw_color(180, 180, 180)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        if self.page_no() == 1:
            return
        self.set_y(-15)
        self.set_font("Calibri", "", 7)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, "Documento de aprendizaje - Generado automaticamente", align="C")

    def chapter_title(self, num, title):
        self.set_font("Calibri", "B", 15)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, f"{num}. {title}", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 51, 102)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)
        self.set_text_color(0, 0, 0)

    def section_title(self, text):
        self.set_font("Calibri", "B", 12)
        self.set_text_color(0, 51, 102)
        self.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(1)

    def body_text(self, text):
        self.set_font("Calibri", "", 11)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def code_block(self, lines):
        self.set_font("Courier", "", 8.5)
        self.set_fill_color(245, 245, 245)
        self.set_draw_color(200, 200, 200)
        max_width = 0
        for line in lines:
            max_width = max(max_width, self.get_string_width(line))
        max_width = min(max_width + 6, 190)
        for line in lines:
            self.cell(max_width, 5, f"  {line}", border="LR", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.cell(max_width, 0, "", border="TB", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def note_box(self, text):
        self.set_fill_color(255, 250, 230)
        self.set_draw_color(255, 193, 7)
        self.set_font("Calibri", "B", 10)
        self.set_text_color(180, 120, 0)
        self.cell(0, 7, f"  NOTA: {text}", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(2)

    def key_box(self, text):
        self.set_fill_color(230, 245, 255)
        self.set_draw_color(0, 51, 102)
        self.set_font("Calibri", "B", 10)
        self.set_text_color(0, 51, 102)
        self.cell(0, 7, f"  CONCEPTO CLAVE: {text}", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(2)

pdf = GuiaPDF()
pdf.add_font("Calibri", "", "C:/Windows/Fonts/calibri.ttf")
pdf.add_font("Calibri", "B", "C:/Windows/Fonts/calibrib.ttf")
pdf.add_font("Calibri", "I", "C:/Windows/Fonts/calibrii.ttf")
pdf.add_font("Courier", "", "C:/Windows/Fonts/cour.ttf")
pdf.set_auto_page_break(auto=True, margin=15)

# ===== PORTADA =====
pdf.add_page()
pdf.set_font("Calibri", "B", 26)
pdf.set_y(70)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 16, "PORTAL DE HERRAMIENTAS", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 16, "DE SOPORTE EPEM", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Calibri", "", 14)
pdf.set_text_color(80, 80, 80)
pdf.ln(10)
pdf.cell(0, 10, "Guia de aprendizaje paso a paso", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 10, "Backend NestJS + datos JSON", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(20)
pdf.set_font("Calibri", "I", 11)
pdf.cell(0, 10, "Modulo 1: Estructura, datos y primer modulo", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 10, "Septiembre 2026", align="C", new_x="LMARGIN", new_y="NEXT")

# ===== INDICE =====
pdf.add_page()
pdf.chapter_title("", "INDICE")
pdf.body_text("1. Concepto del proyecto")
pdf.body_text("2. Arquitectura general (backend + frontend + datos)")
pdf.body_text("3. Los archivos JSON como base de datos temporal")
pdf.body_text("4. Estructura de un modulo NestJS (Controller, Service, Module)")
pdf.body_text("5. El Service: procedimientos.service.ts (explicacion linea por linea)")
pdf.body_text("6. El Controller: procedimientos.controller.ts (explicacion linea por linea)")
pdf.body_text("7. El Module: procedimientos.module.ts")
pdf.body_text("8. Registrar el modulo en AppModule")
pdf.body_text("9. Errores comunes y sus soluciones")
pdf.body_text("10. Endpoints que funcionan")
pdf.body_text("11. Conceptos clave para recordar")

# ===== 1. CONCEPTO =====
pdf.add_page()
pdf.chapter_title(1, "Concepto del proyecto")
pdf.body_text("El Portal de Herramientas de Soporte EPEM es una aplicacion interna con diferentes modulos para que el equipo de soporte trabaje mejor con el sistema EPEM. NO se conecta a la base de datos de EPEM: los datos viven en archivos locales JSON.")
pdf.body_text("Modulos del portal:")
pdf.code_block([
    "  Base de conocimientos",
    "  Buscar errores",
    "  Generar reporte",
    "  Procedimientos",
    "  Herramientas",
    "  Documentacion"
])
pdf.key_box("La ventaja: no estamos desarrollando otra parte del sistema EPEM, sino una herramienta propia para que el equipo de soporte trabaje mejor con EPEM.")

# ===== 2. ARQUITECTURA =====
pdf.add_page()
pdf.chapter_title(2, "Arquitectura general")
pdf.body_text("El proyecto tiene dos partes que se comunican entre si:")
pdf.code_block([
    "PORTAL_DE_HERRAMIENTAS/",
    "  backend/     <- NestJS (API REST)",
    "    data/       <- archivos JSON (base de datos temporal)",
    "    src/        <- codigo del backend",
    "  frontend/     <- React + Vite (interfaz de usuario)"
])
pdf.body_text("Flujo de una peticion:")
pdf.code_block([
    "Frontend --GET /procedimientos--> Controller --> Service (lee JSON) --> JSON al Frontend"
])
pdf.body_text("El frontend consume el backend como una API REST normal. El frontend NO sabe que los datos vienen de archivos JSON: para el, es una API como cualquier otra.")

# ===== 3. JSON =====
pdf.add_page()
pdf.chapter_title(3, "Los archivos JSON como base de datos temporal")
pdf.body_text("Usamos JSON en lugar de una base de datos real por tres motivos:")
pdf.body_text("1. No necesitamos instalar nada (no MySQL, no PostgreSQL, no Docker).")
pdf.body_text("2. Los datos son de solo lectura al principio: el soporte los lee, no los edita desde el portal.")
pdf.body_text("3. Si en el futuro queremos pasar a una BD real, la estructura ya esta definida: cada JSON se convierte en una tabla.")
pdf.body_text("Los 4 archivos creados en backend/data/:")
pdf.code_block([
    "errores.json        <- Errores comunes con codigo, descripcion y solucion",
    "procedimientos.json <- Pasos paso a paso para resolver problemas",
    "soluciones.json     <- Respuestas rapidas tipo FAQ",
    "configuracion.json  <- Datos estaticos (grupos, estados, modulos)"
])
pdf.body_text("Cada archivo es una 'tabla' de nuestra base de datos temporal. El backend los lee del disco y los devuelve al frontend.")

# ===== 4. ESTRUCTURA MODULO =====
pdf.add_page()
pdf.chapter_title(4, "Estructura de un modulo NestJS")
pdf.body_text("En NestJS, un modulo se compone de 3 partes:")
pdf.code_block([
    "Controller  <- Recibe las peticiones HTTP (GET, POST, etc.)",
    "Service     <- Contiene la logica de negocio (leer archivos, filtrar)",
    "Module      <- Agrupa Controller + Service y lo registra en la app"
])
pdf.key_box("El Service es el 'cerebro' (logica). El Controller es el 'mesero' (recibe pedidos HTTP y delega al Service). El Module es el 'indice' (organiza y conecta todo).")

# ===== 5. SERVICE =====
pdf.add_page()
pdf.chapter_title(5, "El Service: procedimientos.service.ts")
pdf.body_text("El Service contiene la logica de negocio. No sabe nada de HTTP ni de URLs. Solo sabe donde estan los datos, como leerlos y como filtrarlos.")
pdf.section_title("Codigo completo:")
pdf.code_block([
    "import { Injectable } from '@nestjs/common';",
    "import * as fs from 'fs';",
    "import { fileURLToPath } from 'url';",
    "import * as path from 'path';",
    "",
    "export interface Paso {",
    "  orden: number;",
    "  descripcion: string;",
    "}",
    "",
    "export interface Procedimiento {",
    "  id: number;",
    "  titulo: string;",
    "  pasos: Paso[];",
    "  modulo: string;",
    "  nivel: string;",
    "  tiempo_estimado: string;",
    "}",
    "",
    "@Injectable()",
    "export class ProcedimientosService {",
    "  private readonly dataPath: string;",
    "",
    "  constructor() {",
    "    const __filename = fileURLToPath(import.meta.url);",
    "    const __dirname = path.dirname(__filename);",
    "    this.dataPath = path.join(__dirname, '..', '..', 'data', 'procedimientos.json');",
    "  }",
    "",
    "  findAll(): Procedimiento[] {",
    "    const rawData = fs.readFileSync(this.dataPath, 'utf-8');",
    "    const procedimientos: Procedimiento[] = JSON.parse(rawData);",
    "    return procedimientos;",
    "  }",
    "",
    "  findOne(id: number): Procedimiento | undefined {",
    "    const todos = this.findAll();",
    "    return todos.find((p) => p.id === id);",
    "  }",
    "",
    "  findByModulo(modulo: string): Procedimiento[] {",
    "    const todos = this.findAll();",
    "    return todos.filter((p) => p.modulo === modulo);",
    "  }",
    "}"
])

pdf.add_page()
pdf.section_title("Explicacion linea por linea")
pdf.body_text("import { Injectable } from '@nestjs/common';")
pdf.body_text("Importa el decorador @Injectable. Le dice a Nest: 'esta clase puede ser usada por otras clases'. Sin esto, el Controller no podria pedirle datos al Service.")
pdf.body_text("import * as fs from 'fs';  y  import * as path from 'path';")
pdf.body_text("Modulos nativos de Node.js: fs (file system) para leer archivos del disco, y path para construir rutas de forma segura (funciona en Windows y Linux).")
pdf.body_text("interface Paso { orden: number; descripcion: string; }")
pdf.body_text("Interfaces de TypeScript. No generan codigo JavaScript, solo le dicen al compilador la forma que deben tener los datos. Si escribis mal una propiedad, TypeScript te avisa antes de ejecutar.")
pdf.body_text("@Injectable()")
pdf.body_text("Decorador que registra esta clase en el contenedor de dependencias de NestJS.")
pdf.body_text("private readonly dataPath: string;")
pdf.body_text("Propiedad privada que guarda la ruta al archivo JSON. 'readonly' significa que solo se asigna una vez (en el constructor).")
pdf.body_text("constructor() { const __filename = fileURLToPath(import.meta.url); ... }")
pdf.body_text("En ES modules no existe __dirname (como en CommonJS). Usamos import.meta.url y fileURLToPath para obtener la ruta del archivo actual, y path.dirname para obtener la carpeta.")
pdf.body_text("findAll(): Procedimiento[] { ... }")
pdf.body_text("fs.readFileSync lee el archivo sincronicamente (espera a que termine). JSON.parse convierte el texto JSON (string) en objetos JavaScript reales. Devuelve un array de Procedimientos.")
pdf.body_text("findOne(id: number): Procedimiento | undefined { ... }")
pdf.body_text("Usa el metodo nativo .find() que devuelve el PRIMER elemento que cumpla la condicion. '| undefined' le dice a TypeScript que puede devolver un Procedimiento o undefined si no existe.")
pdf.body_text("findByModulo(modulo: string): Procedimiento[] { ... }")
pdf.body_text("Usa .filter() que devuelve TODOS los elementos que cumplan la condicion (no solo el primero).")

# ===== 6. CONTROLLER =====
pdf.add_page()
pdf.chapter_title(6, "El Controller: procedimientos.controller.ts")
pdf.body_text("El Controller es la puerta de entrada. Recibe las peticiones HTTP del navegador y decide que Service llamar, que metodo usar y que codigo HTTP devolver.")
pdf.section_title("Codigo completo:")
pdf.code_block([
    "import { Controller, Get, Param, Query } from '@nestjs/common';",
    "import { ProcedimientosService, Procedimiento } from './procedimientos.service.js';",
    "",
    "@Controller('procedimientos')",
    "export class ProcedimientosController {",
    "  constructor(private readonly procedimientosService: ProcedimientosService) {}",
    "",
    "  @Get()",
    "  findAll(@Query('modulo') modulo?: string): Procedimiento[] {",
    "    if (modulo) {",
    "      return this.procedimientosService.findByModulo(modulo);",
    "    }",
    "    return this.procedimientosService.findAll();",
    "  }",
    "",
    "  @Get(':id')",
    "  findOne(@Param('id') id: string): Procedimiento | { statusCode: number; message: string } {",
    "    const procedimiento = this.procedimientosService.findOne(Number(id));",
    "    if (!procedimiento) {",
    "      return { statusCode: 404, message: 'Procedimiento no encontrado' };",
    "    }",
    "    return procedimiento;",
    "  }",
    "}"
])

pdf.add_page()
pdf.section_title("Explicacion linea por linea")
pdf.body_text("import { Controller, Get, Param, Query } from '@nestjs/common';")
pdf.body_text("Importa los decoradores: @Controller (define la ruta base), @Get (responde a GET), @Param (extrae valores de la URL), @Query (extrae query params).")
pdf.body_text("@Controller('procedimientos')")
pdf.body_text("Todas las rutas de esta clase empiezan con /procedimientos. Ej: /procedimientos, /procedimientos/1.")
pdf.body_text("constructor(private readonly procedimientosService: ProcedimientosService) {}")
pdf.body_text("Inyeccion de dependencias. NestJS automaticamente crea una instancia de ProcedimientosService y la pasa al constructor. No hace falta hacer 'new ProcedimientosService()'.")
pdf.body_text("@Get()  findAll(@Query('modulo') modulo?: string)")
pdf.body_text("@Get() sin parametros responde a GET /procedimientos. @Query('modulo') busca ?modulo=... en la URL. El '?' significa que es opcional. Si la URL es /procedimientos?modulo=Comisiones, modulo vale 'Comisiones'.")
pdf.body_text("if (modulo) { return this.procedimientosService.findByModulo(modulo); } return this.procedimientosService.findAll();")
pdf.body_text("Si vino el query param modulo, filtra. Si no, devuelve todos.")
pdf.body_text("@Get(':id')  findOne(@Param('id') id: string)")
pdf.body_text("@Get(':id') responde a GET /procedimientos/1, /procedimientos/2, etc. @Param('id') captura el '1' de la URL como string.")
pdf.body_text("const procedimiento = this.procedimientosService.findOne(Number(id));")
pdf.body_text("Convierte el string '1' al numero 1 (Number(id)) y busca en el Service. Si no existe, devuelve un objeto con statusCode: 404.")

# ===== 7. MODULE =====
pdf.add_page()
pdf.chapter_title(7, "El Module: procedimientos.module.ts")
pdf.body_text("El Module es el registro. Le dice a NestJS que este modulo tiene un Controller y un Service, y los hace disponibles para el resto de la aplicacion.")
pdf.section_title("Codigo completo:")
pdf.code_block([
    "import { Module } from '@nestjs/common';",
    "import { ProcedimientosController } from './procedimientos.controller.js';",
    "import { ProcedimientosService } from './procedimientos.service.js';",
    "",
    "@Module({",
    "  controllers: [ProcedimientosController],",
    "  providers: [ProcedimientosService],",
    "})",
    "export class ProcedimientosModule {}"
])
pdf.body_text("controllers: lista de controladores que manejan rutas HTTP.")
pdf.body_text("providers: lista de servicios que pueden ser inyectados.")
pdf.body_text("El Module es simple: solo registra el Controller y el Service.")

# ===== 8. APPMODULE =====
pdf.add_page()
pdf.chapter_title(8, "Registrar el modulo en AppModule")
pdf.body_text("Sin registrar el ProcedimientosModule en el AppModule raiz, NestJS no sabe que existe. Hay que importarlo.")
pdf.section_title("Codigo de app.module.ts:")
pdf.code_block([
    "import { Module } from '@nestjs/common';",
    "import { AppController } from './app.controller.js';",
    "import { AppService } from './app.service.js';",
    "import { ProcedimientosModule } from './procedimientos/procedimientos.module.js';",
    "",
    "@Module({",
    "  imports: [ProcedimientosModule],",
    "  controllers: [AppController],",
    "  providers: [AppService],",
    "})",
    "export class AppModule {}"
])
pdf.note_box("Tambien se elimino el modulo ObserveModule (telemetria de NestJS) que venia por defecto y no necesitamos. Y en main.ts se quito la referencia a ObserveInstrument.")

# ===== 9. ERRORES =====
pdf.add_page()
pdf.chapter_title(9, "Errores comunes y sus soluciones")
pdf.section_title("Error 1: imports sin extension .js")
pdf.body_text("Sintoma: 'Cannot find module ./procedimientos.service'.")
pdf.body_text("Causa: el tsconfig usa moduleResolution 'nodenext', que exige la extension .js en los imports relativos.")
pdf.body_text("Solucion: escribir './procedimientos.service.js' en lugar de './procedimientos.service'.")
pdf.section_title("Error 2: __dirname is not defined")
pdf.body_text("Sintoma: 'ReferenceError: __dirname is not defined'.")
pdf.body_text("Causa: en ES modules no existe __dirname (es de CommonJS).")
pdf.body_text("Solucion: usar import.meta.url + fileURLToPath + path.dirname para obtener la carpeta actual.")
pdf.section_title("Error 3: Return type cannot be named")
pdf.body_text("Sintoma: 'Return type of public method ... cannot be named'.")
pdf.body_text("Causa: las interfaces no estaban exportadas, asi que el Controller no podia referenciarlas.")
pdf.body_text("Solucion: agregar 'export' delante de las interfaces (export interface Procedimiento).")
pdf.section_title("Error 4: EADDRINUSE (puerto ocupado)")
pdf.body_text("Sintoma: 'Error: listen EADDRINUSE: address already in use :::3000'.")
pdf.body_text("Causa: ya hay un proceso usando el puerto 3000.")
pdf.body_text("Solucion: levantar en otro puerto con PORT=3001 npm run start:dev, o matar el proceso anterior.")

# ===== 10. ENDPOINTS =====
pdf.add_page()
pdf.chapter_title(10, "Endpoints que funcionan")
pdf.body_text("Con el backend corriendo (npm run start:dev), estos endpoints responden:")
pdf.code_block([
    "GET http://localhost:3001/procedimientos",
    "    -> Todos los procedimientos",
    "",
    "GET http://localhost:3001/procedimientos?modulo=SIFEN",
    "    -> Filtra por modulo",
    "",
    "GET http://localhost:3001/procedimientos/1",
    "    -> Un procedimiento por ID"
])
pdf.body_text("Para probar desde la terminal:")
pdf.code_block([
    "curl -s http://localhost:3001/procedimientos"
])

# ===== 11. CONCEPTOS =====
pdf.add_page()
pdf.chapter_title(11, "Conceptos clave para recordar")
pdf.body_text("Service: contiene la logica de negocio, no sabe de HTTP.")
pdf.body_text("Controller: puerta de entrada HTTP, delega al Service.")
pdf.body_text("Module: registro de componentes en NestJS.")
pdf.body_text("Inyeccion de dependencias: Nest crea automaticamente las instancias y las pasa al constructor.")
pdf.body_text("Interfaces TypeScript: definen la forma de los datos para evitar errores en tiempo de compilacion.")
pdf.body_text("ES modules: usan import.meta.url en vez de __dirname.")
pdf.body_text("JSON como BD temporal: cada archivo es una 'tabla'; el backend los lee del disco.")
pdf.body_text("Decoradores: @Controller, @Get, @Param, @Query, @Injectable, @Module. Son funciones que agregan metadatos a clases y metodos.")
pdf.body_text("Metodos nativos de arrays: .find() devuelve el primero que cumpla, .filter() devuelve todos los que cumplan.")

# ===== GUARDAR =====
output_path = "C:/Users/eduardo.fleitas/Music/Proyecto Soporte/PORTAL_DE_HERRAMIENTAS/GUIA_APRENDIZAJE_MODULO1.pdf"
pdf.output(output_path)
print(f"PDF generado en:")
print(output_path)
