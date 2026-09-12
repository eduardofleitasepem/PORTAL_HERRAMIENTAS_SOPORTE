import { Injectable } from "@nestjs/common";
import * as fs from 'fs'
import { fileURLToPath } from "url";
import  * as path from 'path'

//Interfaz que define la forma de una solución/FAQ
export interface Solucion{
    id: number;
    pregunta: string;
    respuesta: string;
    modulo: string;
    categoria: string;
}

@Injectable()
export class SolcionesService{
    private readonly dataPath: string;
    constructor(){
        //contruimos la ruta hacia el jason (who is json?)
        const __filename = fileURLToPath(import.meta.url)
        const __dirname = path.dirname(__filename)
        this.dataPath= path.join(
            __dirname,
            '..',
            '..',
            'data',
            'soluciones.json',
        );
    }
    //Devuelve todas las soluciones
    findAll(): Solucion[] { //declaramos la función , Solucion[] devuelve un array
        const rawData= fs.readFileSync(this.dataPath, 'utf-8'); //Lee el archivo
        const soluciones: Solucion[]= JSON.parse(rawData); //convierte en JSON el contenido del archivo (who is Json?)
        return soluciones;
    }
    //Busca soluciones por ID
    findOne(id: number): Solucion | undefined{ //se declara la función llamando al metodo findOne
        const todos= this.findAll(); //obtener todas las soluciones
        return todos.find((s)=>s.id===id)//buscar por ID
    }
    //Filtra por modulo
    findByModulo(modulo:string):Solucion[]{ //se define la función llamando al metodo findByModulo
        const todos= this.findAll(); //obtener todas las soluciones
        return todos.filter(
            (s)=>s.modulo.toLocaleLowerCase()===modulo.toLocaleLowerCase() //devuelve los solicitado segun el módulo (todo en minuscula)
        );
    }
}