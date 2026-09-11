import { Injectable} from "@nestjs/common";
import * as fs from 'fs';
import { fileURLToPath } from "url";
import * as path from 'path';
// import { find } from "rxjs";
// import e from "express";

// Interfaz que va a definir la forma de nuestro error
export interface Error{
    id: number;
    codigo: string;
    titulo: string;
    descripcion: string;
    causa: string;
    solucion: string;
    modulo_afectado: string;
    frecuencia: string;
    tags: string[];
}
@Injectable()
export class ErroresService{
    private readonly dataPath: string; 
   //contruimos la ruta completa que nos lleva hacia el archivo errores.json
    constructor(){
        //en ES modules no existe __dirname, tons usamos import.meta.url
        const __filename = fileURLToPath(import.meta.url); //representa la ruta completa del archivo
        const __dirname= path.dirname(__filename);
        this.dataPath = path.join(__dirname, //contruye la ruta 
            '..',
            '..',
            'data',
            'errores.json'
        );
    }


//Devuelve TODOS los errores 
findAll(): Error[]{
    const rawData= fs.readFileSync(this.dataPath, 'utf-8');
    const errores: Error[]= JSON.parse(rawData);
    return errores;
}
//Busca error por Id 
findOne(id:number):Error | undefined {
    const todos= this.findAll();
    return todos.find((e)=>e.id === id);
}
// Filtra por módulo afectado
findByModulo(modulo:string): Error[]{
const todos = this.findAll();
return todos.filter(
    (e) => e.modulo_afectado.toLowerCase() === modulo.toLowerCase()
)
}
//Filtra por frecuencia
findByFrecuencia(frecuencia: string): Error[]{
    const todos = this.findAll();
    return todos.filter(
        (e) =>e.frecuencia.toLowerCase() === frecuencia.toLowerCase()
    );
}
}