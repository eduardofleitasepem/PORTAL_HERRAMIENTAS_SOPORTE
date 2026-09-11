import { Controller,Get,Param,Query } from "@nestjs/common";
import { ErroresService, Error } from "./errores.service.js";

//creamos el endpoint de errores 
@Controller('errores')
export class ErroresController{
    constructor(private readonly erroresService: ErroresService){} //injección de dependencias
        // GET Puede recibir filtros opcionales : ?modulo=SIFEN o ?frecuencia=alta
        @Get()
        findAll(
            @Query('modulo') modulo?:string,
            @Query('frecuencia') frecuencia?:string,
        ): Error[]{
            let resultado= this.erroresService.findAll();
            if (modulo){
                resultado = resultado.filter(
                    (e)=>e.modulo_afectado.toLocaleLowerCase()===modulo.toLocaleLowerCase(),
                );
            }
            if (frecuencia){
                resultado= resultado.filter(
                    (e)=>e.frecuencia.toLocaleLowerCase()===frecuencia.toLocaleLowerCase(),
                )
            }
            return resultado;
        }
        //GET /errores/:id
        @Get(':id')
            findOne(@Param('id') id: string): Error|{statusCode: number; message: string}{
                const error= this.erroresService.findOne(Number(id));
                
                if(!error){
                    return {statusCode: 404, message: 'Error no encontrado'};
                }
                return error;
            }
    }


