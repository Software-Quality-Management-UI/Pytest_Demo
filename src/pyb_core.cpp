#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "money.hpp"

namespace py = pybind11;

PYBIND11_MODULE(_core, m) {
    m.doc() = "pybind11 class wrapping a Money helper";
    py::class_<pybtst::Money>(m, "Money")
        .def(py::init<double>())
        .def("getAmount", &pybtst::Money::getAmount)
        .def("__add__", &pybtst::Money::operator+)
        .def("__eq__", &pybtst::Money::operator=)
        .def("__repr__", &pybtst::Money::toString);
}
