import json

def montar_grade_gulosa(professores: list, slots: list, semanas: int = 12):
    
    proporcao_eixo = {
        '1': semanas * 4 * 5 * 0.3, #72
        '2': semanas * 20 * 0.3, #72
        '3': semanas * 20 * 0.15, #36
        '4': semanas * 20 * 0.15, #36
        '5': semanas * 20 * 0.1, #24
    }

    plano_trimestral = {semana: [] for semana in range(1, semanas + 1)}
    total_horas_eixo = {eixo: 0 for eixo in proporcao_eixo}
    total_horas_prof_semana = {prof['id']: {sem: 0 for sem in range(1, semanas + 1)} for prof in professores}
    total_horas_prof_trimestre = {prof['id']: 0 for prof in professores}
    custo_total_periodo = 0.0

    for semana in range(1, semanas + 1):
        
        horas_semanais = {prof['id']: 0 for prof in professores}
        
        for slot in slots:
            
            eixo_alvo = max(proporcao_eixo, key=proporcao_eixo.get)
            
            if proporcao_eixo[eixo_alvo] <= 0:
                break
            
            professor_escolhido = None
            menor_custo = float('inf')
            
            for prof in professores:
                if eixo_alvo in prof['eixos_habilitados']:
                    if slot in prof['disponibilidade_da_semana']:
                        if horas_semanais[prof['id']] < prof['max_horas_por_semana']:
                             
                            if prof['custo_aula'] < menor_custo:
                                professor_escolhido = prof
                                menor_custo = prof['custo_aula']
                                
            if professor_escolhido:
                
                plano_trimestral[semana].append({
                    'slot': slot,
                    'eixo': eixo_alvo,
                    'professor': professor_escolhido['id']
                })
                
                proporcao_eixo[eixo_alvo] -= 1
                horas_semanais[professor_escolhido['id']] += 1
                
                total_horas_eixo[eixo_alvo] += 1
                total_horas_prof_semana[professor_escolhido['id']][semana] += 1
                total_horas_prof_trimestre[professor_escolhido['id']] += 1
                custo_total_periodo += menor_custo

    return {
        "plano_trimestral_por_semana": plano_trimestral,
        "total_horas_por_eixo": total_horas_eixo,
        "total_horas_prof_por_semana": total_horas_prof_semana,
        "total_horas_prof_trimestre": total_horas_prof_trimestre,
        "custo_total_periodo": custo_total_periodo
    }


with open("exemplo.json", "r") as f:
    dados = json.load(f)

resultado = montar_grade_gulosa(
    dados["professores"],
    dados["slots"],
    dados["semanas"]
)

print(json.dumps(resultado, indent =2))