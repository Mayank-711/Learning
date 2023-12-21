log=[
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","Lille","Dijon"]

    },
    {
        "country":"Germany",
        "visits":5,
        "cities":["Berlin","Hamberg","Stuttgart"]

    }
]
def insertion(countryv,visitsv,citiesv):
    new_country={}
    new_country["country"]=countryv
    new_country["visits"] = visitsv
    new_country["cities"] = citiesv
    log.append(new_country)
    
insertion("Russia",2,["Moscow","Saint PetersBurg"])
print(log)