#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <map>
#include <stdexcept>

class Term;
class Variable {
    private:
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

        Term operator*(double coeff);
        Term operator/(double coeff);
};

class Equation;
class Term {
    private:
        std::string var;
        double coeff;
    public:
        Term(std::string var = "x", double coeff = 1) {
            this->var = var;
            this->coeff = coeff;
        }
        
        std::string getVar() {
            return this->var;
        }
        
        double getCoeff() {
            return this->coeff;
        }

        std::string toString() {
            return this->var + " \\cdot " + std::to_string(this->coeff);
        }

        Equation operator+(Term term);
        Equation operator-(Term term);
};

class Equation {
    private:
        std::map<std::string, double>* vars = NULL;
        double known = 0;
        
        void init() {
            this->vars = new std::map<std::string, double>();
        }

        void addTerm(std::string var, double coeff) {
            this->vars->operator[](var) += coeff;
        }

        Equation clone() {
            Equation result = this->known;
            for(std::pair<std::string, double> pair : *(this->vars)) {
                result.addTerm(pair.first, pair.second);
            }
            return result;
        }
    public:
        Equation(double known = 0) {
            this->init();
            this->known = known;
        }

        Equation(Term term) {
            this->init();
            this->addTerm(term.getVar(), term.getCoeff());
        }

        Equation operator-(double known) {
            Equation result = this->clone();
            result.known -= known;
            return result;
        }

        Equation operator+(double known) {
            Equation result = this->clone();
            result.known += known;
            return result;
        }

        Equation operator+(Term term) {
            Equation result = this->clone();
            result.addTerm(term.getVar(), term.getCoeff());
            return result;
        }

        Equation operator-(Term term) {
            Equation result = this->clone();
            for(std::pair<std::string, double> pair : *(this->vars)) {
                result.addTerm(pair.first, pair.second);
            }
            result.addTerm(term.getVar(), - term.getCoeff());
            return result;
        }

        Equation operator+(Equation other) {
            Equation result = this->clone();
            result.known += other.known;
            
            for(std::pair<std::string, double> pair : *(this->vars)) {
                result.addTerm(pair.first, pair.second);
            }
            
            for(std::pair<std::string, double> pair : *(other.vars)) {
                result.addTerm(pair.first, pair.second);
            }

            return result;
        }

        Equation operator-(Equation other) {
            Equation result = this->clone();
            result.known += other.known;
            
            for(std::pair<std::string, double> pair : *(this->vars)) {
                result.addTerm(pair.first, pair.second);
            }
            
            for(std::pair<std::string, double> pair : *(other.vars)) {
                result.addTerm(pair.first, - pair.second);
            }

            return result;
        }

        std::string toString() {
            std::string result;
            for(std::pair<std::string, double> pair : *(this->vars)) {
                if (pair.second < 0)
                    result += "- " + pair.first + " \\cdot " + std::to_string(-pair.second) + " ";
                else
                    result += "+ " + pair.first + " \\cdot " + std::to_string(pair.second) + " ";
            }
            if (known < 0)
                return result + "- " + std::to_string(-known) + " = 0";
            else
                return result + "+ " + std::to_string(known) + " = 0";
        }
};

Term Variable::operator*(double coeff) {
    return Term(this->name, coeff);
}

Term Variable::operator/(double coeff) {
    throw new std::runtime_error("divisionByZeroException");
    return Term(this->name, 1/coeff);
}

Equation Term::operator+(Term term) {
    return Equation(*(this)) + term;
}

Equation Term::operator-(Term term) {
    return Equation(*(this)) - term;
}

int main () {
    try {
        Variable x = "x", y = "y", z = "z";
        Equation f = x * 2 + y * 3 - z * 4 - 7;
        std::cout << f.toString() << std::endl;
    } catch(std::runtime_error* error) {
        std::cout << error->what() << std::endl;
    }
    //
    return 0;
}
