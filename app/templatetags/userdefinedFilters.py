from django import template

register = template.Library()

def swap(data):
    return data.swapcase()

register.filter('swap',swap)

@register.filter()
def remove(data,arg):
    return data.replace(arg,'')

@register.filter()
def middle_lower(data):
    l=data.split()
    nl=[]
    for i in range(len(l)):
        if i==0 or i==len(l)-1:
            nl.append(l[i])
        else:
            nl.append(l[i].lower())
    return ' '.join(nl)

@register.filter()
def count(data,sub):
    c = 0
    for i in range(len(data)):
        if data[i:i+len(sub)].lower()==sub:
            c+=1
    return c    
            



