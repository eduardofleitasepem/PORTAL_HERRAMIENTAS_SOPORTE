import { Injectable } from "@nestjs/common";
import * as fs from 'fs'
import { fileURLToPath } from "url";
import  * as path from 'path'

//Interfaces para cada sesion JSON
export interface GrupoTicket{
    id: number;
    nombre: string;
}
export interface EstadoTicket{
    id:number;
    nombre: string;
    ed_final:boolean;
}

//La forma del archivo JSON completo
export interface Configuracion{
    grupos_tickets: GrupoTicket[];
    estados_tickets: EstadoTicket[]
}

@Injectable()
export class ConfiguracionServices{
    private readonly dataPath: string;
    constructor(){
        const __filename=fileURLToPath(import.meta.url);
        const __dirname=path.dirname(__filename);
        this.dataPath=path.join(
            __dirname,
            '..',
            '..',
            'data',
            'configuracion.json',
        );
    }
    //Lee el archivo y devuelve todo el objeto
    findAll():Configuracion{
        const rawData= fs.readFileSync(this.dataPath,'utf-8');
        const configuracion: Configuracion= JSON.parse(rawData);
        return configuracion;
    }
    //Solo los grupos de tickets
    getGruposTickets():GrupoTicket[]{
        return this.findAll().grupos_tickets;
    }
    //Solo los estados de tickets
    getEstadosTickets(): EstadoTicket[]{
        return this.findAll().estados_tickets;
    }
}