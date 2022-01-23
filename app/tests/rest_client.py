from requests import get

from prettytable import PrettyTable


resources = ['battery', 'network', 'memory', 'processor', '']
for resource in resources:
    data = get(f'http://localhost:5000/{resource}')
    assert data.status_code == 200, 'Test failed'

    res = data.json()
    
    if resource != '':
        if type(res) == list:
            print(res[0].keys())
            tbl = PrettyTable(list(res[0].keys()))
            for row in res:
                tbl.add_row(row.values())
        elif type(res) == dict:
            print(res.keys())
            tbl = PrettyTable(list(res.keys()))
            tbl.add_row(res.values())

        print(tbl)

print('test complete')