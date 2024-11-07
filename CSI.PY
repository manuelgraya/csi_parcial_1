import random
import os


enunciado = {
    "1": "Según The Standish Group, entre las causas exógenas del fracaso del software se encuentran…",
    "3": "Según The Standish Group, entre las causas endógenas del fracaso del software se encuentran…",
    "5": "En el trabajo a medida de la Edad Media no se encontraban…",
    "7": "En el trabajo a medida del Renacimiento no se encontraban…",
    "9": "¿Cuál de las siguientes acciones forma parte de la filosofía del taylorismo?",
    "11": "La crisis de la calidad de mediados del siglo XX se debió a…",
    "13": "Según Garvin, a la calidad reconocible, pero no definible, se la conoce como calidad…",
    "15": "Según Garvin, a la satisfactoria adecuación a las necesidades del cliente se la conoce como calidad…",
    "17": "Según Garvin, a la calidad derivada de las cualidades inherentes a un producto se la denomina calidad…",
    "19": "Según Garvin, a la calidad asociada a la empresa productora se la denomina calidad…",
    "21": "Según Garvin, a la calidad asociada al interés y urgencia del cliente se la denomina calidad…",
    "23": "El motivo por el que una botella de agua cuesta más en el desierto se explica por la calidad…",
    "25": "La Calidad actual no se basa en…",
    "27": "Según Alan Davis, ¿quién es la persona más importante de un proyecto?",
    "29": "La necesidad 'tecnológica' de un cliente implica que…",
    "31": "El objetivo del diagnóstico al estudiar una demanda de un cliente es…",
    "33": "La necesidad 'procedimental' de un cliente implica que…",
    "35": "La necesidad 'directiva' de un cliente implica que…",
    "37": "Indica cuál de estos capítulos no tiene por qué formar parte de una memoria de proyecto.",
    "39": "¿Qué debe contener la sección 'Conceptos básicos' de una memoria de proyectos?",
    "41": "Un objetivo de la recolección de requisitos es…",
    "43": "Según Dunning-Kruger, los individuos incompetentes…",
    "45": "La competencia real se logra con el tiempo mediante…",
    "47": "La gestión de la información comprende considerar…",
    "49": "¿Cuál de este contenido no lo consideramos un dato?",
    "51": "Según Celko, implementar un almacén de datos con pobre calidad de datos puede aumentar su costo…",
    "53": "¿Cuál de estos factores producen polución de datos?",
    "55": "Las normas ISO están orientadas a ordenar y establecer niveles…",
    "57": "Qué característica de las siguientes no se encuentra en la calidad de datos inherentes en la ISO/IEC 25012.",
    "59": "¿Qué características debe tener un usuario para garantizar la calidad de los datos que gestiona?",
    "61": "Definida por el Reglamento General sobre Protección de Datos europeo REU 679/2016, el tratamiento de datos personales para que no puedan atribuirse a una persona física se denomina...",
    "63": "Indica cuál de estas razones no es una excepción que permita el tratamiento de datos especiales según la Ley 3/2018.",
    "65": "El servicio de exclusión publicitaria de la Agencia Española de Protección de Datos se denomina lista…",
    "67": "En el ámbito del desarrollo software, un actor es…",
    "69": "Indica qué expresión no es un requisito funcional correcto.",
    "71": "El diagrama que representa los requisitos de información se denomina diagrama…",
    "73": "Indica qué expresión no es un requisito funcional correcto.",
    "75": "Los requisitos funcionales se representan visualmente como…",
    "77": "Las agrupaciones funcionales generalmente contienen los casos de uso que atañen…",
    "79": "Del análisis de requisitos debe obtenerse una relación…",
    "81": "Con relación al análisis, escoge la opción correcta.",
    "83": "Indica el requisito funcional denominado correctamente.",
    "85": "El tipo de datos físico habitual para cadenas de texto pequeñas de tamaño variable es…",
    "87": "Un jugador puede participar en varias ligas y viceversa. Dicha relación se almacenará en la tabla…",
    "89": "¿Qué beneficio tiene la regla de identificador universal?",
    "91": "En una tabla Partido, el campo de referencia al equipo local debe denominarse…",
    "93": "Un array que contiene instancias de la clase Persona se denomina…",
    "95": "La variable txtName es de tipo…",
    "97": "El método RandomNumber() está escrito en notación…",
    "99": "La estructura del almacén determina…"
}

solucion = {
    "1": "los usuarios finales, los requisitos y las expectativas.",
    "3": "el soporte ejecutivo, los recursos y la competencia tecnológica.",
    "5": "las piezas estandarizadas.",
    "7": "los productos fabricados en cadena.",
    "9": "El trabajador no debe realizar movimientos inútiles.",
    "11": "Todas las respuestas son correctas.",
    "13": "trascendente.",
    "15": "de usuario.",
    "17": "de producto.",
    "19": "de fabricación.",
    "21": "basada en valor.",
    "23": "basada en valor.",
    "25": "Ninguna de las otras respuestas es correcta.",
    "27": "El usuario.",
    "29": "el cliente necesita informatizar procedimientos correctos.",
    "31": "saber si tengo interés y capacidad para hacerlo.",
    "33": "el cliente necesita revisar sus procedimientos antes de informatizarlos.",
    "35": "Ninguna de las otras respuestas es correcta.",
    "37": "Concepción.",
    "39": "Las definiciones necesarias para entender el modelo.",
    "41": "estudiar el contexto del negocio.",
    "43": "tienden a sobreestimar sus propias habilidades.",
    "45": "experiencia, esfuerzo y capacidad.",
    "47": "los datos, su estructura y su gestión.",
    "49": "Letra del DNI.",
    "51": "en un 100%.",
    "53": "Redundancia no controlada.",
    "55": "de homogeneidad y calidad.",
    "57": "Seguridad.",
    "59": "Formación, capacidad y actitud.",
    "61": "seudonomización.",
    "63": "Requerimiento por parte de la Administración Pública.",
    "65": "Robinson.",
    "67": "todo perfil que actúa directamente con el sistema.",
    "69": "Alquilar Vehículo.",
    "71": "conceptual.",
    "73": "Visualizar Factura.",
    "75": "casos de uso.",
    "77": "a la misma entidad.",
    "79": "de las necesidades del cliente.",
    "81": "Un actor puede representar a varios usuarios.",
    "83": "Mostrar incidencia.",
    "85": "VARCHAR.",
    "87": "Jugador_Liga.",
    "89": "Todas las respuestas son correctas.",
    "91": "equipo_local_id.",
    "93": "aPersona.",
    "95": "TextBox.",
    "97": "Pascal.",
    "99": "el patrón de almacenamiento."
}

opciones = {
    "1": "los usuarios finales, los requisitos y las expectativas./el soporte ejecutivo, los recursos y la competencia tecnológica./los objetivos, los cronogramas y la formación./los requisitos, los cronogramas y el coste final",
    "3": "los usuarios finales, los requisitos y las expectativas./el soporte ejecutivo, los recursos y la competencia tecnológica./los objetivos, los cronogramas y la formación./los requisitos, los cronogramas y el coste final",
    "5": "los gremios especializados./las categorías maestro-aprendiz./las piezas estandarizadas./las revisiones por parte del comprador.",
    "7": "las primeras máquinas./las primeras fábricas./las piezas estandarizadas./los productos fabricados en cadena.",
    "9": "El trabajador forma parte de la cadena de decisiones./El trabajador debe estar satisfecho./El trabajador no debe realizar movimientos inútiles./Ninguna de las otras respuestas es correcta.",
    "11": "un incremento de las regulaciones gubernamentales./el origen de la obsolescencia programada./un aumento del consumo./Todas las respuestas son correctas.",
    "13": "trascendente./basada en valor./intrascendente./subjetiva.",
    "15": "de cliente./de usuario./de fabricación./basada en valor.",
    "17": "inherente./de producto./de fabricación./háptica.",
    "19": "de especificación./de proceso./de fabricación./basada en producto.",
    "21": "potencial./de usuario./de cliente./basada en valor.",
    "23": "basada en valor./de producto./de usuario./transcendental.",
    "25": "medidas y normas./expectativas de cliente./perspectivas de Garvin./Ninguna de las otras respuestas es correcta.",
    "27": "El desarrollador./El comercial./El usuario./El analista o quien recabe los requisitos.",
    "29": "el cliente necesita informatizar procedimientos correctos./el cliente necesita documentar sus soluciones informáticas./el cliente necesita procedimientos adecuados para su informatización./Ninguna de las otras respuestas es correcta.",
    "31": "establecer los requisitos funcionales del sistema./saber si tengo interés y capacidad para hacerlo./definir los requisitos de información del sistema./Todas las respuestas son correctas.",
    "33": "el cliente necesita documentar sus soluciones informáticas./el cliente necesita revisar sus procedimientos antes de comenzar el proyecto./el cliente necesita revisar sus procedimientos antes de informatizarlos./el cliente necesita revisar la funcionalidad de sus aplicaciones informáticas.",
    "35": "el cliente presenta necesidades primordialmente resolubles mediante tecnología./el cliente requiere soluciones informáticas para la dirección de la entidad./el cliente solicita un proyecto externalizado bajo nuestra dirección./Ninguna de las otras respuestas es correcta.",
    "37": "Planificación./Implementación./Conclusiones./Concepción.",
    "39": "Las siglas y los acrónimos./Las definiciones necesarias para entender el modelo./La explicación de todos los términos técnicos que pudiera no entender el cliente./Cualquier anotación de interés para entender la memoria.",
    "41": "estudiar el contexto del negocio./conocer el sistema actual./determinar necesidades y límites./Todas las respuestas son correctas.",
    "43": "tienden a refugiarse en su incompetencia para evitar responsabilidades./tienden a sobreestimar sus propias habilidades./tienden a evitar tomar decisiones./tienden a trabajar más duramente para compensar esta condición.",
    "45": "mérito, formación y competencia./principios, integridad y determinación./experiencia, esfuerzo y capacidad./colaboración, liderazgo y trabajo en equipo.",
    "47": "los campos, las tablas y sus relaciones./la gestión del conocimiento y su aplicación./los datos, su estructura y su gestión./los principios de Dilbert, Peter y Dunning-Kruger.",
    "49": "Letra del DNI./Fila y asiento de una entrada de cine./Suma de propinas recibidas./Todas las respuestas son datos.",
    "51": "en un 100%./en un 50%./en un 25%./en un 120%.",
    "53": "Ausencia de integridad referencial./Redundancia no controlada./Antonimia terminológica./Todas las respuestas son correctas.",
    "55": "de gestión y administración./de garantías de cumplimiento./de gestión y desarrollo./de homogeneidad y calidad.",
    "57": "Exactitud./Credibilidad./Seguridad./Actualidad.",
    "59": "Formación, capacidad y actitud./Experiencia, conocimiento y predisposición./Implicación, autoridad y convicción./Resolución y cultura de empresa.",
    "61": "reificación./seudonomización./recodificación./constructivización.",
    "63": "Obligaciones del responsable del tratamiento./Datos publicados por el interesado./Interés público esencial./Requerimiento por parte de la Administración Pública.",
    "65": "eAEPD./Robinson./Aarón./AEPD+.",
    "67": "todo perfil relacionado con el dominio del problema./todo perfil que actúa directamente con el sistema./básicamente un usuario./Todas las respuestas son correctas.",
    "69": "Crear Aula./Eliminar Usuario./Alquilar Vehículo./Imprimir Factura.",
    "71": "de relaciones./Entidad-Relación./de entidades./conceptual.",
    "73": "Actualizar Producto./Visualizar Factura./Rechazar Solicitud./Enviar Confirmación",
    "75": "casos de uso./entidades./agrupaciones funcionales./actores.",
    "77": "al mismo actor./a la misma entidad./al mismo requisito funcional./al mismo dominio del problema.",
    "79": "de las necesidades del cliente./de alternativas tecnológicas./de objetivos y del ámbito del problema./de todos los componentes del sistema.",
    "81": "Un actor puede representar a varios usuarios./Un actor representa a un usuario./Existe un único actor principal, pero puede haber varios secundarios./Un actor puede representar a varios perfiles de usuario.",
    "83": "Consultar Datos de usuario./Mostrar incidencia./Ver Proveedor./Comprar Vehículo.",
    "85": "CHAR./VARCHAR./TEXT./T_TEXT.",
    "87": "Jugador_Liga./Liga./Jugador./Participa.",
    "89": "Consistencia y garantía de concurrencia./Mayor eficiencia en la búsqueda./Independiza la clave del dominio del problema./Todas las respuestas son correctas.",
    "91": "local_id./equipo_local_id./equipo1_id./Ninguna de las otras respuestas es correcta.",
    "93": "personas./aPersonas./aPersona./_persona.",
    "95": "String./Text./TextBox./Name",
    "97": "Pascal./Dromedario./eslovena./C.",
    "99": "los detalles de la información a almacenar./los requisitos técnicos del sistema de almacenamiento./el tratamiento y protección de la información./el patrón de almacenamiento."
}


def ratemwar():
    aux="1"
    while aux != "x":
        os.system('color F0')
        os.system('cls' if os.name == 'nt' else 'clear')
        clave_aleatoria = random.choice(list(enunciado.keys()))
        # clave_aleatoria = "35" # Para pruebas
        print("\n\n\t" + enunciado[clave_aleatoria] + "\n")
        i = 1
        opciones_mezcladas = random.sample(opciones[clave_aleatoria].split('/'), len(opciones[clave_aleatoria].split('/')))
        for opcion in opciones_mezcladas:
            print("\t\t"+ str(i) + ". " + opcion)
            i = i + 1

        while True:
            respuesta = input("\n\t\tSelecciona una respuesta (1-4)(x para salir):")
            if respuesta in ["1", "2", "3", "4","x"]:
                break
            else:
                print("\n\t\tPor favor, selecciona una opción válida entre 1 y 4.")
        if respuesta != "x":    
            aux=respuesta
            respuesta = opciones_mezcladas[int(aux) - 1]
            if respuesta == solucion[clave_aleatoria]:
                os.system('color F2')
                print("\n")
                print("\t  ____ ___  ____  ____  _____ ____ _____ ___ ")
                print("\t / ___/ _ \|  _ \|  _ \| ____/ ___|_   _/ _ \ ")
                print("\t| |  | | | | |_) | |_) |  _|| |     | || | | |")
                print("\t| |__| |_| |  _ <|  _ <| |__| |___  | || |_| |")
                print("\t \____\___/|_| \_\_| \_\_____\____| |_| \___/")
            else:
                os.system('color F4')
                print ("\t  ___ _   _  ____ ___  ____  ____  _____ ____ _____ ___  ")
                print ("\t |_ _| \ | |/ ___/ _ \|  _ \|  _ \| ____/ ___|_   _/ _ \ ")
                print ("\t  | ||  \| | |  | | | | |_) | |_) |  _|| |     | || | | |")
                print ("\t  | || |\  | |__| |_| |  _ <|  _ <| |__| |___  | || |_| |")
                print ("\t |___|_| \_|\____\___/|_| \_\_| \_\_____\____| |_| \___/\n")
                print("\tLa respuesta correcta es: " + solucion[clave_aleatoria])
        else:
            break
        print("\n\n\n\n")
        input("\n\t\tPulsa Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear') # Limpiar pantalla al salir del bucle while principal del juego 
if __name__ == '__main__':
    ratemwar()