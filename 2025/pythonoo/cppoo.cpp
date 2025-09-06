#include <iostream>
//#include<ctime>
using namespace std;

class Animal {
public:
  virtual void talk(){
    cout << "moo..heha..woof\n";
  }
  virtual void walk() {
    cout << "Animal walk\n";
  }
  void sleep() {
    cout << "Animal Sleep\n";
  }
};

class Cow:public Animal {
public:
  void talk() {
    cout << "Moo…\n";
  }

  void walk() {
    cout << "Cow walk\n";
  }
};


class Donkey:public Animal {
public:
  void talk() {
    cout << "bray…\n";
  }
};
//class Dog final:public Animal  {
class Dog :public Animal  {
public:
  void talk(){
    cout << "bark…\n";
  }

  void walk() { //final{
    cout << "Dog walk..\n";
  }
};

class Poodle:public Dog {
public:
  void talk(){
    cout << "poodle bark..\n";
  }

  void walk(){
    cout << "poodle walk..\n";
  }
};

int main( ) { 
  srand((unsigned int)time(0));
  Animal *a;
  switch(rand()%4){
    case 0: a = new Cow(); break;
    case 1: a = new Donkey(); break;
    case 2: a = new Dog(); break;
    case 3: a = new Poodle(); break;
 }
  a->talk();
  a->walk();
  a->sleep(); 
  delete a;
  return 0;
}