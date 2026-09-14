import { Module } from "@nestjs/common";
import { ConfiguracionController } from "./configuracion.controller.js";
import { ConfiguracionServices } from "./configuracion.service.js";

@Module({
    controllers:[ConfiguracionController],
    providers:[ConfiguracionServices],
})
export class ConfiguracionModule{}