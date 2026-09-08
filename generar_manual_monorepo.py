from fpdf import FPDF
import os

class ManualPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Calibri", "", 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "Guia: Como crear un monorepo con Git", align="L")
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
        self.cell(0, 10, "Documento generado automaticamente", align="C")

    def chapter_title(self, num, title):
        self.set_font("Calibri", "B", 14)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, f"PASO {num}: {title.upper()}", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 51, 102)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)
        self.set_text_color(0, 0, 0)

    def body_text(self, text):
        self.set_font("Calibri", "", 11)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def code_block(self, lines):
        self.set_font("Courier", "", 9)
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

    def warning_box(self, text):
        self.set_fill_color(255, 235, 238)
        self.set_draw_color(239, 83, 80)
        self.set_font("Calibri", "B", 10)
        self.set_text_color(180, 40, 40)
        self.cell(0, 7, f"  IMPORTANTE: {text}", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(0, 0, 0)
        self.ln(2)

# Detectar fuentes
font_path = "C:/Windows/Fonts/"
fonts = {
    "Calibri": ("calibri.ttf", "calibrib.ttf", "calibrii.ttf"),
    "Courier": ("cour.ttf", "courbd.ttf", None),
}

pdf = ManualPDF()

# Registrar fuentes
pdf.add_font("Calibri", "", f"{font_path}calibri.ttf")
pdf.add_font("Calibri", "B", f"{font_path}calibrib.ttf")
pdf.add_font("Calibri", "I", f"{font_path}calibrii.ttf")
pdf.add_font("Courier", "", f"{font_path}cour.ttf")
pdf.set_auto_page_break(auto=True, margin=15)

# === PORTADA ===
pdf.add_page()
pdf.set_font("Calibri", "B", 28)
pdf.set_y(70)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 18, "COMO CREAR UN MONOREPO", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 18, "CON GIT", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Calibri", "", 14)
pdf.set_text_color(80, 80, 80)
pdf.ln(10)
pdf.cell(0, 10, "Unificar backend y frontend en un solo repositorio", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 10, "para commitear todo desde una sola vista", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(20)
pdf.set_font("Calibri", "I", 11)
pdf.cell(0, 10, "Basado en la experiencia con el proyecto GESTION_TICKET_EPEM", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 10, "Septiembre 2026", align="C", new_x="LMARGIN", new_y="NEXT")

# === CONTENIDO ===
pdf.add_page()
pdf.chapter_title(1, "Pararse en la raiz del proyecto")
pdf.body_text("Abrí una terminal (Git Bash, VS Code o Fork) y navegá hasta la carpeta que contiene tanto el backend como el frontend.")
pdf.code_block([
    'cd "/c/Users/tu-usuario/ruta/PORTAL_DE_HERRAMIENTAS"'
])
pdf.note_box("Usa comillas dobles si la ruta tiene espacios.")

pdf.add_page()
pdf.chapter_title(2, "Eliminar el .git interno del backend")
pdf.body_text("Si el backend ya fue inicializado como un repositorio git aparte (tiene su propia carpeta .git), hay que eliminar ese control de versiones interno. De lo contrario, el monorepo raiz no detectara los archivos del backend.")
pdf.code_block([
    "rm -rf backend/.git"
])
pdf.warning_box("Esto NO borra archivos de codigo. Solo elimina el historial git interno del backend. Como aun no tenia commits, no se pierde nada.")

pdf.add_page()
pdf.chapter_title(3, "Inicializar git en la raiz (el monorepo)")
pdf.body_text("Crea un unico repositorio git en la carpeta raiz. Este sera el unico .git que controle todo el proyecto.")
pdf.code_block([
    "git init"
])

pdf.add_page()
pdf.chapter_title(4, "Crear un .gitignore raiz")
pdf.body_text("Es fundamental ignorar archivos que no deben versionarse: dependencias, builds, variables de entorno, bases de datos locales, etc.")
pdf.code_block([
    "cat > .gitignore << 'EOF'",
    "# Dependencias",
    "**/node_modules/",
    "**/dist/",
    "**/.env",
    "**/.env.local",
    "**/*.sqlite",
    "**/data.sqlite",
    "",
    "# Logs y builds",
    "*.log",
    "**/build/",
    "**/coverage/",
    "",
    "# IDE",
    ".vscode/",
    ".idea/",
    "",
    "# Sistema operativo",
    ".DS_Store",
    "Thumbs.db",
    "EOF"
])
pdf.note_box("El prefijo **/ indica que aplica en cualquier subcarpeta, ya sea backend o frontend.")

pdf.add_page()
pdf.chapter_title(5, "Revisar que se va a commitear")
pdf.body_text("Antes de agregar archivos, siempre revisa el estado. Esto te permite detectar si algo se esta versionando por error.")
pdf.code_block([
    "git status"
])
pdf.body_text("Deberias ver algo como:")
pdf.code_block([
    "Untracked files:",
    "  .gitignore",
    "  backend/",
    "  frontend/"
])

pdf.add_page()
pdf.chapter_title(6, "Agregar todo y commitear")
pdf.body_text("Hay dos formas de hacerlo. La mas rapida es un solo commit. La mas prolija es por partes.")

pdf.set_font("Calibri", "B", 11)
pdf.cell(0, 8, "Opcion A: Todo en un solo commit", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Calibri", "", 11)
pdf.code_block([
    "git add -A",
    'git commit -m "init: monorepo PORTAL_DE_HERRAMIENTAS"',
    "",
    "# O con mensaje detallado:",
    'git commit -m "init: monorepo PORTAL_DE_HERRAMIENTAS" -m "- Backend: NestJS base" -m "- Frontend: React + Vite + Tailwind base"'
])

pdf.set_font("Calibri", "B", 11)
pdf.cell(0, 8, "Opcion B: Por partes (mas prolijo)", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("Calibri", "", 11)
pdf.code_block([
    "# Primero el backend",
    "git add backend/ .gitignore",
    'git commit -m "feat: agregar backend NestJS"',
    "",
    "# Luego el frontend",
    "git add frontend/",
    'git commit -m "feat: agregar frontend React/Vite"'
])

pdf.add_page()
pdf.chapter_title(7, "Verificar el resultado")
pdf.body_text("Comproba que los commits quedaron bien y que la estructura es correcta.")
pdf.code_block([
    "git log --oneline"
])
pdf.body_text("Deberia mostrar 1 o 2 commits, segun la opcion elegida.")
pdf.code_block([
    "ls -la"
])
pdf.body_text("Deberias ver:")
pdf.code_block([
    "backend/",
    "frontend/",
    ".git/",
    ".gitignore"
])

pdf.add_page()
pdf.chapter_title(8, "Abrir el repo en Fork")
pdf.body_text("Para trabajar visualmente con el monorepo desde Fork:")
pdf.body_text("1. En Fork: File -> Add Existing Repository")
pdf.body_text("2. Selecciona la carpeta raiz (ej: PORTAL_DE_HERRAMIENTAS)")
pdf.body_text("3. Listo — ahora tenes una sola ventana con todo el proyecto.")
pdf.note_box("A partir de ahora, todos los commits del backend y frontend aparecen en una sola linea de tiempo.")

# === RESUMEN ===
pdf.add_page()
pdf.set_font("Calibri", "B", 16)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 12, "RESUMEN RAPIDO", new_x="LMARGIN", new_y="NEXT")
pdf.set_draw_color(0, 51, 102)
pdf.line(10, pdf.get_y(), 200, pdf.get_y())
pdf.ln(6)
pdf.set_text_color(0, 0, 0)

pdf.set_font("Calibri", "", 11)
summary = """1. cd "ruta/al/proyecto"
2. rm -rf backend/.git
3. git init
4. Crear .gitignore raiz
5. git status (verificar)
6. git add -A && git commit -m "init: monorepo..."
7. git log --oneline (confirmar)
8. Abrir en Fork
"""
pdf.multi_cell(0, 7, summary)
pdf.ln(6)

pdf.set_font("Calibri", "B", 11)
pdf.set_text_color(0, 51, 102)
pdf.cell(0, 8, "Comandos clave para no olvidar:", new_x="LMARGIN", new_y="NEXT")
pdf.set_text_color(0, 0, 0)
pdf.code_block([
    "git add -A          # Agregar todos los cambios",
    'git commit -m "..." # Commitear con mensaje',
    "git status          # Ver estado antes de commitear",
    "git log --oneline   # Ver historial resumido"
])

# === GUARDAR ===
output_path = "C:/Users/eduardo.fleitas/Music/Proyecto Soporte/PORTAL_DE_HERRAMIENTAS/MANUAL_MONOREPO_GIT.pdf"
pdf.output(output_path)
print(f"PDF generado exitosamente en:")
print(output_path)
