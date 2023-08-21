#include <iostream>

int main() {
    std::string x;
    std::cout << "What is your name? "<<std::endl;
    std::cin >> x;
    std::cout << "Hello " << x <<std::endl;
    int y;
    std::cout << "What is your Student ID?"<<std::endl;
    std::cin >> y;
    std:: cout<<"Your ID is "<<y<<std::endl;

    std::cout<<"---------------------------------------"<<std::endl;
    int var1;
    int var2;
    std::cout<< "Please enter one number: "<<std::endl;
    std::cin>>var1;
    std::cout<< "Please enter another number: "<<std::endl;
    std::cin>>var2;
    int sum=var1+var2;
    int diff=var1-var2;
    int prod=var1*var2;
    std::cout <<"Summation:"<<sum<<std::endl;
    std::cout <<"Difference:"<<diff<<std::endl;
    std::cout <<"Multiplication:"<<prod<<std::endl;
    std::cout<<"---------------------------------------"<<std::endl;

    std::string name;
    std::cout<<"What is your name ?"<<std::endl;
    std::cin>>name;
    int labGrade;
    std::cout<<"What is your lab grade? "<<std::endl;
    std::cin>>labGrade;
    int midtermGrade;
    std::cout<<"What is your midterm grade? "<<std::endl;
    std::cin>>midtermGrade;
    int finalGrade;
    std::cout<<"What is your final grade?"<<std::endl;
    std::cin>>finalGrade;
    labGrade=labGrade/4;
    midtermGrade=midtermGrade*35/100;
    finalGrade=finalGrade*4/10;
    int lastScore=(labGrade+midtermGrade+finalGrade)/3;
    std::cout<<"Name: "<<name<<std::endl;
    std::cout<<"Lab: "<<labGrade<<std::endl;
    std::cout<<"Midterm: "<<midtermGrade<<std::endl;
    std::cout<<"Final: "<<finalGrade<<std::endl;
    std::cout<<"Last Score: "<<lastScore<<std::endl;
    std::cout<<"---------------------------------------"<<std::endl;

    std::cout<<"*\n**\n***\n**\n*"<<std::endl;


    return 0;
}
