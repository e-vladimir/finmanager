data = {'174517-429479-127108-880502': False, '174517-434091-465401-050641': True, '174515-092011-722204-810090': True}

print({ido for ido, result in data.items() if result})
