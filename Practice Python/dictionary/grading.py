scores={"Harry":81,"Ron":78,"Hermione":99,"Draco":74,"Neville":62}
grades={}
for s in scores:
    if scores[s] > 90:
        grades[s]="Oustanding"
    elif scores[s] > 80:
        grades[s] = "Exceeds Expectation"
    elif scores[s] > 70:
        grades[s]="Acceptable"
    else:
        grades[s]="Fails"
print(grades)