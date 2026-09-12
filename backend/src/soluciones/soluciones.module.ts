import { Module } from "@nestjs/common";
import { SolucionesController } from "./soluciones.controller.js";
import { SolcionesService } from "./soluciones.service.js";

@Module({
    controllers: [SolucionesController],
    providers: [SolcionesService],
})
export class SolucionesModule{}