import { Injectable } from '@nestjs/common';
import * as fs from 'fs';
import { fileURLToPath } from 'url';
import * as path from 'path';

// Interfaz: define la forma que tienen los datos
// Esto es TypeScript: le dice al compilador "un procedimiento tiene estas propiedades"
export interface Paso {
  orden: number;
  descripcion: string;
}

export interface Procedimiento {
  id: number;
  titulo: string;
  pasos: Paso[];
  modulo: string;
  nivel: string;
  tiempo_estimado: string;
}

@Injectable() // Decorador: le dice a NestJS "esta clase puede ser inyectada en otros lugares"
export class ProcedimientosService {
  private readonly dataPath: string;

  constructor() {
    // En ES modules no existe __dirname, usamos import.meta.url
    const __filename = fileURLToPath(import.meta.url);
    const __dirname = path.dirname(__filename);
    this.dataPath = path.join(
      __dirname,
      '..',
      '..',
      'data',
      'procedimientos.json'
    );
  }

  // Metodo: lee el archivo y devuelve todos los procedimientos
  findAll(): Procedimiento[] {
    // Lee el archivo como texto
    const rawData = fs.readFileSync(this.dataPath, 'utf-8');
    // Convierte el texto JSON a objetos de JavaScript
    const procedimientos: Procedimiento[] = JSON.parse(rawData);
    return procedimientos;
  }

  // Metodo: busca un procedimiento por su ID
  findOne(id: number): Procedimiento | undefined {
    const todos = this.findAll();
    return todos.find((p) => p.id === id);
  }

  // Metodo: filtra por modulo (ej: "Comisiones", "SIFEN")
  findByModulo(modulo: string): Procedimiento[] {
    const todos = this.findAll();
    return todos.filter((p) => p.modulo === modulo);
  }
}
