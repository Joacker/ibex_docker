#include "/app/src/contractor/funtions_for_ANN.cpp"
#include "/app/kerasify/keras_model.h"
#include "/app/kerasify/keras_model.cc"
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
#include <cstdlib>

using namespace std;



float Model_output(string path, vector<float>& input,int size){
    KerasModel model;
    model.LoadModel(path);
    Tensor in(size),out;
    input=padWithZeros(input,size);
    normalize_l2(input);
    in.data_ = input;

    model.Apply(&in,&out);
    float proba=out.operator()(0);

    return proba;


}