import csv

def cut(in_list, morceau):
    part = len(in_list) // morceau
    reste = len(in_list) % morceau
    l = [24,24,24,24+3]    
    print(part, reste)
    inf_part = 0
    sup_part = part
    print(inf_part, sup_part)
    result = []
    for i in range(1, morceau+1):        
        if i != morceau:
            result.append(in_list[inf_part:sup_part])            
        else:
            print('Entrée dans la 4ème boucle')
            result.append(in_list[inf_part:])
            print('Sortie de la boucle')
            break
        inf_part += part
        sup_part += part        
    print('All tasks are finished')
    return result

def save(output_name='new_fine.csv', content=''):
    if content:
        with open(output_name, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        return 'error_empty'

if __name__ == '__main__':
    fname = 'csv_test.csv'
    f = open(fname, 'r')
    try:
        reader = csv.reader(f)
        csv_list = [e[0] for e in reader]    
    finally:
        f.close()    
    list_result = cut(csv_list, 4)
    txt_result_list = ['\n'.join(e) for e in list_result]
    [save('part%s.csv' % str(i+1), content=e) for i,e in enumerate(txt_result_list)]