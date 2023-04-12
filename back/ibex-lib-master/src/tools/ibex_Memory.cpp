//============================================================================
//                                  I B E X                                   
// File        : ibex_Memory.cpp
// Author      : Gilles Chabert
// Copyright   : IMT Atlantique (France)
// License     : See the LICENSE file
// Created     : Jul 05, 2014
// Last Update : Nov 21, 2017
//============================================================================

#include "ibex_Memory.h"

using namespace std;

namespace ibex {

Memory::Object::~Object() {
	switch(type) {
	case CTC:          delete (Ctc*) data; break;
	case BSC:          delete (Bsc*) data; break;
	case SYSTEM:       delete (System*) data; break;
	case CELL_BUFFER:  delete (CellBuffer*) data; break;
	case LINEARIZER:   delete (Linearizer*) data; break;
	default:		   /* subclass responsability. See e.g. ibex_OptimMemory.h */ break;
	}
}

Memory::~Memory() {
	// deleted in reverse order (in case some objects depend on
	// previous objects)
	while (!objs.empty()) {
		delete objs.front();
		objs.pop_front();
	}
}

} // end namespace ibex
