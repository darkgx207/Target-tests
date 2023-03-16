const dados = require('./dados.json');

function max_and_min(dados){
    let min = 999999999999999; // Condição necessária para comparação de minimos
    let max = 0;
    let soma = 0;
    let dias_uteis = 0;
    let acima_da_media = []

    for(i of dados){
        let dia_semana = (Number.parseInt(i.dia) + 3) % 7;  
        if (dia_semana !== 0 && dia_semana !== 1){  // Verificando a possibilidade de final de semana
            if(i.valor > max){
                max = i.valor;
            }
            if(i.valor < min && i.valor != 0 ) {
                min = i.valor; 
            } 
            dias_uteis++; 
            soma = soma + i.valor;
        }
    }

    let media = (soma / dias_uteis).toFixed(2)

    for(j of dados ){
        if( j.valor >= media) { acima_da_media.push({'dia':j.dia, 'valor':j.valor})}
    }
    return {'max':max.toFixed(2),
            'min':min.toFixed(2),
            'media':media,
            'sup_media':acima_da_media}
}

console.log(max_and_min(dados))
