import { Module } from '@nestjs/common';
import { AppController } from './app.controller.js';
import { AppService } from './app.service.js';
import { ProcedimientosModule } from './procedimientos/procedimientos.module.js';
import { ErroresModule } from './errores/errores.module.js';

@Module({
  imports: [ProcedimientosModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {} 
