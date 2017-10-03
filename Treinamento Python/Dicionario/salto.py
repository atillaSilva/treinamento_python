rodrigo = {'nome': 'Rodrigo', 'saltos': [6.5,6.1,6.2,5.4,5.3]}
soma = 0
for i in rodrigo['saltos']:
    soma = soma + i
rodrigo['media'] = soma
print str(rodrigo['media']/len(rodrigo['saltos'])) + ' m'
