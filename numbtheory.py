import math

def euclidex1(a,b):
    '''Función que implementa el algoritmo extendido de Euclides. Toma a, b y
    devuelve (m,n,mcd) donde ma + nb = mcd siendo mcd el máximo común divisor.
      Parameters
          ----------
          a,b : int
   '''
    Q=a//b
    A=0;B=1
    C=1;D=-Q
    while a%b!=0:
        bx=b;b=a%b
        a=bx
        Q=a//b
        Ax=C;Bx=D
        C=A-Q*C;D=B-Q*D
        A=Ax;B=Bx
    return A,B,b

def euclidex(a,b):
    '''Implementación del algoritmo extendido de Euclides usando una función 
    recursiva. Toma a,b y devuelve (m,n,mcd) donde ma + nb = mcd donde mcd es 
    el máximo común divisor.
        Parameters
            ----------
            a,b : int
    '''
    if a%b==0:
        return 0,1,b
    else:
        A,B,r=euclidex(b,a%b)
        return B,A-(a//b)*B,r

def chino(m,r):
    '''Esta función acepta dos arreglos de enteros, m y r, de igual dimensión.
    A partir del teorema chino del residuo, resuelve el conjunto de ecuaciones:
        x congruente con r[i] módulo de m[i]
    Y devuelve x.
        Parameters
            ----------
            m,r : list
        Ejemplo de listas:
            m = [5,6,7]
            r = [1,2,3]
    '''
    M=1;Mi=[];Yi=[];k=len(m)
    for i in range(k):
        M=M*m[i]
    for i in range(k):
        Mi=Mi+[M/m[i]]
    for i in range(k):
        A,B,C=euclidex(Mi[i],m[i])
        Yi=Yi+[A]
    X=0
    for i in range(k):
        X=X+Yi[i]*Mi[i]*r[i]
    return X%M

def euclides(a,b):
    '''Función recursiva que calcula el máximo común múltiplo de a y b, usando
    el algoritmo de Euclides.
        Parameters
            ----------
            a,b : int
    '''
    if a%b==0:
        return b
    else:
        return euclides(b,a%b)

def facp(n,p):
    '''Función para el cálculo de coordenadas primas de un entero. Recibe un
    entero n y un arreglo de los números primos p. Devuelve un arreglo con 
    las coordenadas primas.
        Parameters
            ----------
            n : int
            p : list 
        Ejemplo de lista de primos:
            p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    '''
    e=[]
    if n==1:
        return [0]
    i=0
    while n!=1:
        k=0
        while n%p[i]==0:
            k=k+1
            n=n//p[i]
        e=e+[k]
        i=i+1
    return e

def criba(n):
    '''Función que utiliza el algoritmo de la criba de Eratóstenes para
    encontrar todos los números primos menores que n.
        Parameters
            ----------
            n : int
    '''
    # Se crea la lista de enteros menores que n
    a=[]
    for i in range(n):
        a=a+[i]
    ap=[]
    # Se eliminan los enteros que no sean primos
    i=2;imax=math.sqrt(n)
    while i<imax:
        k=2
        while k*a[i]<n:
            a[k*a[i]]=0
            k=k+1
        i=i+1
        while a[i]==0:
            i=i+1
    for j in range(2,n):
        if a[j]!=0:
            ap=ap+[a[j]]
    return ap

def number(e,p):
    '''Función que recibe dos arreglos e y p. El primero debe contener las
    coordenadas primas de un número m. Esta función calcula y devuelve el 
    número m.
        Parameters
            ----------
            e,p : list
        Ejemplo de listas:
            e = [1, 0, 1]
            p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    '''
    n=len(e)
    m=1
    for i in range(n):
        # Calcula el entero m multiplicando cada primo por el valor de la
        # coordenada correspondiente
        m=m*(p[i]**e[i])
    return m

def fr(x,n):
    '''Función pseudoaleatoria módulo n utilizada en el algoritmo Rho de
    Pollard.
        Parameters
            ----------
            x,n : int'''
    return (x*x+1)%n

def r0(n):
    '''Implementación del algoritmo Rho de Pollard. Recibe un número compuesto
    n y devuelve un factor del mismo (típicamente el primo más pequeño).
        Parameters
            ----------
            n : int
    '''
    x=y=0;f=1
    while f==1:
        x=fr(x,n);y=fr(fr(x,n),n)
        # Cálcula el mcd con el algoritmo de euclides
        m=euclides(n,y-x)
        if m!=1 and m!=n:
            f=0
    return m

def triald(n):
    '''Función que toma un entero n y devuelve un factor del mismo, típicamente
    el primo más pequeño.
        Parameters
            ----------
            n : int
    '''
    k=3;f=1
    while f==1:
        if n%k!=0:
            k=k+2
        else:
            f=0
    return k

def emcd(e,f):
    '''Recibe 2 arreglos, e y f, y devuelve un arreglo g donde:
        g[i]=mín(e[i],f[i])
    Si los 2 arreglos no tiene la misma longitud entonces devuelve 0 para
    aquellas posiciones que no puedan ser comparadas.
        Parameters
            ----------
            e,f : list
        Ejemplo de listas:
            e = [7, 1, 9]
            f = [5, 2]
    '''
    g=[]
    m=min(len(e),len(f))
    n=max(len(e),len(f))
    for i in range(n):
        if i<m:
            # Agrega los valores mínimos a la lista g
            g=g+[min(e[i],f[i])]
        else:
            # Agrega un cero para las posiciones que no pueden ser comparadas
            g=g+[0]
    return g

def mcm(a,b):
    '''Esta función devuelve el mínimo común múltiplo de dos enteros, a y b.
        Parameters
            ----------
            a,b : int
    '''
    # Para calcular el mcm se obtiene el producto y se divide sobre el máximo
    # común divisor. Este último se calcula usando el algoritmo de euclides.
    return (a*b)/euclides(a,b)

def emcm(e,f):
    '''Recibe 2 arreglos, e y f, y devuelve un arreglo g donde:
        g[i]=máx(e[i],f[i])
    Si los 2 arreglos no tiene la misma longitud entonces devuelve 0 para
    aquellas posiciones que no puedan ser comparadas.
        Parameters
            ----------
            e,f : list
        Ejemplo de listas:
            e = [7, 1, 9]
            f = [5, 2]
    '''
    g=[]
    m=min(len(e),len(f))
    n=max(len(e),len(f))
    for i in range(n):
        if i<m:
            # Agrega los valores máximos a la lista g
            g=g+[max(e[i],f[i])]
        else:
            # Agrega un cero para las posiciones que no pueden ser comparadas
            g=g+[0]
    return g

def phi(n,p):
    '''Implentación de la función phi de Euler la cual calcula  la cantidad de 
    enteros positivos menores o iguales a n y coprimos con n.
        Parameters
            ----------
            n : int
            p : list 
        Ejemplo de lista de primos:
            p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    '''
    # Cálculo las coordenadas primas
    e=facp(n,p)
    # Obtención de la longitud de la lista de coordenadas e inicialización de r
    m=len(e);r=1
    for k in range(m):
        if e[k]!=0:
            # Fórmula de la función phi de Euler
            r=r*((p[k]**e[k])-(p[k]**(e[k]-1)))
    return r

def numfr(f):
    '''Función recursiva de toma un arreglo de números enteros f y devuelve el
    resultado de la fracción continua usando dichos números.
        Parameters
            ----------
            f : list 
        Ejemplo de lista:
            f = [3, 7, 15, 1, 292, 1, 1]
    '''
    if len(f)==1:
        return f[0]
    else:
        return f[0]+1/float(numfr(f[1:]))

def permu(xs):
    '''Función auxiliar en la obtención de las permutaciones de un arreglo xs.
        Parameters
            ----------
            xs : list 
        Ejemplo de lista:
            xs = [1,2,3]
    '''
    if len(xs) <= 1:
        yield xs
    else:
        for i in range(len(xs)):
            for p in permu(xs[:i] + xs[i + 1:]):
                yield [xs[i]] + p

def permu1(xs):
    '''Recibe un arreglo xs y devuelve las permutaciones de dicho arreglo.
        Parameters
            ----------
            xs : list 
        Ejemplo de lista:
            xs = [1,2,3]
    '''
    if len(xs) <= 1:
        # Devuelve el arreglo si sólo tiene un elemento
        return xs
    else:
        permus = [] 
        for i in range(len(xs)):
            # Cálcula cada permutación y se agrega a la lista permus
            for p in permu(xs[:i] + xs[i + 1:]):
                permus.append([xs[i]] + p)
    return permus
        
def fie(n):
    '''Recibe un número entero n y calcula cuántos coprimos menores que n 
    tiene n.
        Parameters
            ----------
            xs : list 
    '''
    c=0
    for i in range(1,n):
        if euclides(n,i) == 1:
            # Se usa el algoritmo de euclides para determinar si son coprimos
            # y si lo son se suma al contador c
            c=c+1
    return c
  
def bin(x):
    '''Función recursiva que recibe un entero x y delvueve un arreglo con los
    valores en sistema binario de dicho número, empezando con el dígito menos 
    significativo.
        Parameters
            ----------
            x : int 
    '''
    if x<2:
        return [x]
    else:
        return [x%2]+bin(x//2)

def residuo(b,x,r):
    '''Parameters
            ----------
            b,x,r : int
    '''
    l=[]
    # Convierte x a binario y obtiene el número de dígitos
    a=bin(x)
    n=len(a)
    for i in range(n):
        # Cálcula b módulo r y agrega el valor a la lista l.
        c=b%r
        l=l+[c]
        # Redefine b como el cuadrado de b módulo r
        b=c*c
    s=1
    for i in range(n):
        if a[i]==1:
            # Si el dígito del valor en binario es 1 entonces cálcula esto:
            s=s*l[i]
            s=s%r
    return s,l

def bezout(a,b,m,n):
    '''Esta función recibe cuatro enteros que satisfacen la identidad de Bezout:
        m*a + n*b = (a,b)
    Dónde (a,b) es el máximo común denominador. La función calcula y devuelve 
    m1 y n1 que también cumplan con la identidad pero con m1 positivo.
        Parameters
            ----------
            a,b,m,n : int 
    '''
    if m>0:
        # Si m ya es mayor que 0 se devuelve m,n
        return m,n
    else:
        k=0; m1=m;
        while m1<=0:
            # Mientras no se encuentre una m1 postiva se usa la identidad de 
            # Bezout para calcualr nuevos valores de m1 y n1
            k = k+1
            m1 = m + k*b
            n1 = n - k*a
        return m1,n1