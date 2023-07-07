#include <iostream>
#include <cstdlib> // srand, rand
#include <ctime>
using namespace std;

int main(){
    srand(time(0)); //semilla

    int min, max, aleatorio, intentos=0, n;
    cout<<"Ingrese minimo: "; cin>>min;
    cout<<"Ingrese maximo: "; cin>>max;
    
    //cout<<RAND_MAX<<endl;
    aleatorio = min + rand()%((max-min) +1);

    clock_t t;
    t = clock();

    do{
        cout<<"Ingrese un numero: "; cin>>n;
        if(n>aleatorio){
            cout<<"El numero es menor"<<endl;
        }else if(n<aleatorio){
            cout<<"El numero es mayor"<<endl;
        }
        ++intentos;
    }while(n!=aleatorio);
    
    t = clock() - t;
    cout<<"El numero es: "<<aleatorio<<endl;
    cout<<"Intentos: "<<intentos<<endl;
    cout<<"Tiempo: "<<((float)t)/CLOCKS_PER_SEC<<" segundos"<<endl;

    return 0;
}