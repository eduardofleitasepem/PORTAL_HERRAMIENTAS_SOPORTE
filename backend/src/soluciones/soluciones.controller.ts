import { Controller,Get,Param,Query } from "@nestjs/common";
import { Solucion,SolcionesService } from "./soluciones.service.js";

@Controller('soluciones')
export class SolucionesController{
    constructor(private readonly solucionesServices: SolcionesService){}
    //Get Soluciones
    //Acepta filtros opcionales: ?modulo=Comisiones
    @Get()
    findAll(
        @Query('modulo')modulo?: string, //parametros opcionales
        @Query('categoria')categoria?: string,
    ): Solucion[]{ //devuelve un array
        let resultado = this.solucionesServices.findAll(); //llama todas las soluciones de JSON (who is json?)
        if (modulo){ //condicion que verifica si se envia el módulo
            resultado=resultado.filter(
                (s)=>s.modulo.toLocaleLowerCase()===modulo.toLocaleLowerCase(),
            );
        }
        if (categoria){// misma función que el del módulo
            resultado=resultado.filter(
                (s)=>s.categoria.toLocaleLowerCase()===categoria.toLocaleLowerCase() //filtra por módulo
            );
        }
        return resultado;
    }
    //GET soluciones Id 
    @Get(':id') 
    findOne(@Param('id')id:string):Solucion | {statusCode:number; message:string;}{ //se definen los parametros 
        const solucion= this.solucionesServices.findOne(Number(id)); //busca solucion según id que se introduzca
        if (!solucion){ //si la solución es distinta tira este mensaje
            return {statusCode: 404, message: 'Solucion no encontrada'};
        }
        return solucion;
    }
}