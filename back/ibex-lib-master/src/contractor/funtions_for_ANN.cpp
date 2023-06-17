#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <eigen3/Eigen/Dense>
#include <numeric>

using namespace std;
using namespace Eigen;

vector<float> padWithZeros(vector<float> v, int N) {
    float originalSize = v.size();

    if (N > originalSize) {
        v.resize(N);
        fill(v.begin() + originalSize, v.end(), 0.0);
    }

    return v;
}
void normalize_l2(std::vector<float>& v) {
    float norm = std::sqrt(std::accumulate(v.begin(), v.end(), 0.0, [](float acc, float x) {
        return acc + x * x;
    }));

    if (norm != 0.0) {
        std::transform(v.begin(), v.end(), v.begin(), [norm](float x) {
            return x / norm;
        });
    }
}