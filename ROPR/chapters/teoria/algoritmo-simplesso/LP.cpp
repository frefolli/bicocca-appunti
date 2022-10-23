#include <iostream>

class Variable {
        std::string name;
    public:
        Variable(std::string name = "x") {
            this->name = name;
        }
        
        Variable(const char* name) {
            this->name = std::string(name);
        }
        
        std::string getName() {
            return this->name;
        }
        
        std::string toString() {
            return this->name;
        }
}

class Term {
    std::string var;
    double coeff;
        public:
            Term(std::string var = "x", double coeff = 1) {
                this->var = var;
                this->coeff = 1;
            }
            
            std::string getVar() {
                return this->var;
            }
            
            double getCoeff() {
                return this->coeff;
            }
}

class Equation {
        std::map<std::string, double>* vars = NULL;
        double known = 0;
        void init() {
            this->vars = new std::map<std::string, double>();
        };
    public:
        Equation(double known = 0) {
            this->init();
            this->known = known;
        };
}

int main () {
  std::cout << "Hello World";

  return 0;
}