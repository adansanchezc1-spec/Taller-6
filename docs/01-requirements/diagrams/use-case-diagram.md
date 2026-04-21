# Diagrama de Casos de Uso

```mermaid
graph LR
    usuario([Usuario])

    subgraph Sistema Taller 6
        uc1[UC-001 Registrar colegio]
        uc2[UC-002 Registrar alumno]
        uc3[UC-003 Calcular matrícula]
        uc4[UC-004 Consultar información]
        uc5[UC-005 Guardar y cargar datos]
    end

    usuario --> uc1
    usuario --> uc2
    usuario --> uc3
    usuario --> uc4
    usuario --> uc5
    uc2 -.-> uc1
    uc3 -.-> uc2
```

