import { Module } from '@nestjs/common';
import { AppController } from './app.controller.js';
import { AppService } from './app.service.js';
import { ProcedimientosModule } from './procedimientos/procedimientos.module.js';
import { ErroresModule } from './errores/errores.module.js';
import { SolucionesModule } from './soluciones/soluciones.module.js';
import { ConfiguracionModule } from './configuracion/configuracion.module.js';

@Module({
  imports: [ProcedimientosModule,ErroresModule,SolucionesModule,ConfiguracionModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {} 
