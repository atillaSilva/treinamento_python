km = 1000
consumo_combustivel = {'fusca':{'autonomia': 7, 'consumo':0, 'custo':0}, 'gol':{'autonomia': 10, 'consumo':0, 'custo':0}, 'uno':{'autonomia': 12.5, 'consumo':0, 'custo':0}, 'vectra':{'autonomia': 9, 'consumo':0, 'custo':0},
'corsa':{'autonomia': 14.5, 'consumo':0, 'custo':0}}

for i in consumo_combustivel:
    consumo_combustivel[i]['consumo'] = km/consumo_combustivel[i]['autonomia']
    consumo_combustivel[i]['custo'] = consumo_combustivel[i]['consumo']*2.25

print 'R$: ' + str(consumo_combustivel['gol']['custo'])
print str(consumo_combustivel['gol']['consumo']) + ' litros'


