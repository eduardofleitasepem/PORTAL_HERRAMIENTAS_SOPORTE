import { Module } from "@nestjs/common";
import { ErroresController} from "./errores.controller.js";
import { ErroresService } from "./errores.service.js";

@Module({
    controllers: [ErroresController],
    providers: [ErroresService],

})
export class ErroresModule{}