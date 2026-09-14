import { Get, Controller } from "@nestjs/common";

import { ConfiguracionServices } from "./configuracion.service.js";

import type {
  Configuracion,
  EstadoTicket,
  GrupoTicket,
  ModuloPortal
} from "./configuracion.service.js";

@Controller('configuracion')
export class ConfiguracionController {

  constructor(
    private readonly configuracionServices: ConfiguracionServices
  ) {}

  // GET /configuracion
  @Get()
  findAll(): Configuracion {
    return this.configuracionServices.findAll();
  }

  // GET /configuracion/grupos-tickets
  @Get('grupos-tickets')
  getGrupoTickets(): GrupoTicket[] {
    return this.configuracionServices.getGruposTickets();
  }

  // GET /configuracion/estados-tickets
  @Get('estados-tickets')
  getEstadosTickets(): EstadoTicket[] {
    return this.configuracionServices.getEstadosTickets();
  }
  @Get('modulos-portal')
  getModulosPortal(): ModuloPortal[]{
    return this.configuracionServices.getModulosPortal(); 
  }
}