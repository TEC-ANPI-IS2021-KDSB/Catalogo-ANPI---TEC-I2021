#define WITHOUT_NUMPY
#include "matplotlibcpp.h"
namespace plt = matplotlibcpp;
int main() {
    std::vector<double> x(4), y(4);
    x= {1,2,3,4};
    y={1,2,3,4};
    plt::plot(x,y);
    plt::show();
}
