s = input()
dic = {':-)': 0, ':-(': 0}
dic[':-)'] = s.count(':-)')
dic[':-('] = s.count(':-(')
if dic[':-)'] == 0 and dic[':-('] == 0:
    print('none')
elif dic[':-)'] > dic[':-(']:
    print('happy')
elif dic[':-)'] < dic[':-(']:
    print('sad')
else:
    print('unsure')