from BD.conexion import DAO
import funciones

def menuPrincipal(dao):
    continuar = True
    print("Iniciando el menú principal...")
    while continuar:
        print("\n================MENU PRINCIPAL===============")
        print("1 - Listar")
        print("2 - Registrar")
        print("3 - Actualizar")
        print("4 - Eliminar")
        print("5 - Ordenar")
        print("6 - Salir")
        print("7 - Registros a Hospital")
        print("=============================================\n")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 1 or opcion > 7:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 6:
                continuar = False
                print("\n Sistema Finalizado.\n")
            else:
                ejecutarOpcion(dao, opcion)
        except ValueError:
            print("Por favor, ingrese un número válido.")
#############################################################################################################################################
def ejecutarOpcion(dao, opcion):
    try:
        if opcion == 1:
            cursos = dao.listarCursos()
            if cursos:
                funciones.listarCursos(cursos)
            else:
                print("No se encontraron cursos.")
#############################################################################################################################################                
        elif opcion == 2:
            curso = funciones.pedirDatosRegistro()
            dao.registrarCurso(curso)
#############################################################################################################################################            
        elif opcion == 3:
            cursos = dao.listarCursos()
            if cursos:
                datos_actualizados = funciones.pedirDatosActualizacion(cursos)
                if datos_actualizados:
                    dao.actualizarCurso(datos_actualizados)
            else:
                print("No se encontraron cursos.")
#############################################################################################################################################                
        elif opcion == 4:
            cursos = dao.listarCursos()
            if cursos:
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if codigoEliminar:
                    confirmar = input(f"¿Está seguro que desea eliminar el curso con ID {codigoEliminar}? (s/n): ")
                    if confirmar.lower() == 's':
                        dao.eliminarCurso(codigoEliminar)
                        print("Curso eliminado correctamente.")
                    else:
                        print("Eliminación cancelada.")
            else:
                print("No se encontraron cursos.")
#############################################################################################################################################                
        elif opcion == 5:
            cursos = dao.listarCursos()
            if cursos:
                criterio = input("Ordenar por (nombre, apellido, dni): ")
                cursos_ordenados = funciones.ordenarCursos(cursos, criterio)
                funciones.listarCursos(cursos_ordenados)
            else:
                print("No se encontraron cursos.")
#############################################################################################################################################                
        elif opcion == 7:
            # Opción 7: Registrar a un paciente en un hospital
            pacientes = dao.listarCursos()  # Asumimos que 'listarCursos' devuelve la lista de pacientes
            hospitales = dao.listarHospitales()  # Lista de hospitales

            if pacientes and hospitales:
                # Seleccionar paciente
                print("Seleccione el paciente:")
                funciones.listar_cursos(pacientes)
                paciente_id = input("Ingrese el código del paciente para registrar: ")
                
                # Validar que el paciente existe
                paciente_encontrado = None
                for paciente in pacientes:
                    if str(paciente[0]) == paciente_id:
                        paciente_encontrado = paciente
                        break
                
                if not paciente_encontrado:
                    print("Paciente no encontrado.")
                    return

                # Seleccionar hospital
                hospital_id, cancelar = funciones.seleccionar_hospital(hospitales)
                if cancelar:
                    print("Registro cancelado.")
                    return

                # Registrar paciente en hospital
                if hospital_id:
                    dao.registrarEnHospital(paciente_id, hospital_id)
            else:
                print("No se encontraron pacientes o hospitales disponibles.")
        else:
            print("Opción inválida.")
    except Exception as e:
        print(f"Ocurrió un error al ejecutar la opción: {e}")

if __name__ == "__main__":
    try:
        dao = DAO()
        menuPrincipal(dao)
    except Exception as e:
        print(f"Error al inicializar el sistema: {e}")
