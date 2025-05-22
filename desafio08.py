
nome = str(input('Qual o seu nome ?'))

medida = float(input('Uma distância em metros: '))
km = medida / 1000
hm = medida / 100 
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print (f'A medida de {medida} m corresonde em quilômetros {km} km. \n Hectômetros {hm} hm. \n Decâmetro {dam}. dam \n Decímetro {dm} dm. \n Centímetro {cm} cm. \n Milímetros {mm} mm. \n')

resposta = input("O calculo apresentado lhe atende ? (Sim/Não): ")

if resposta == 'sim':
    print (f'Agradecemos por escolher a ferramenta da rainha das Construtoras.')

 
elif resposta == 'não':
    continuar = input(f'Gostaria de realizar a conversão, com outro número ? (Sim/Não): ').lower()
    if continuar == 'não':
        print ('Agradecemos pelo seu tempo, tenha um ótimo dia!')


elif resposta == '':
    print (f'Resposta invalida. Por favor, digite (sim ou não)). ')