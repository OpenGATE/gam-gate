/* --------------------------------------------------
   Copyright (C): OpenGATE Collaboration
   This software is distributed under the terms
   of the GNU Lesser General  Public Licence (LGPL)
   See LICENSE.md for further details
   -------------------------------------------------- */

#ifndef GamPhaseSpaceActor_h
#define GamPhaseSpaceActor_h

#include <pybind11/stl.h>
#include "G4GenericAnalysisManager.hh"
#include "G4Cache.hh"
#include "GamVActor.h"
#include "GamHelpers.h"
#include "GamHitsCollection.h"

namespace py = pybind11;

class GamPhaseSpaceActor : public GamVActor {

public:

    //explicit GamPhaseSpaceActor(std::string type_name);
    explicit GamPhaseSpaceActor(py::dict &user_info);

    virtual ~GamPhaseSpaceActor();

    // Called when the simulation start (master thread only)
    void StartSimulationAction() override;

    // Called every time a Run starts (all threads)
    void BeginOfRunAction(const G4Run *run) override;

    // Called every time a Event starts (all threads)
    void BeginOfEventAction(const G4Event *event) override;

    // Called every time a batch of step must be processed
    void SteppingAction(G4Step *) override;

    // Called at the end of an event
    void EndOfEventAction(const G4Event *event) override;

    // Called every time a Run ends (all threads)
    void EndOfRunAction(const G4Run *run) override;

    void EndOfSimulationWorkerAction(const G4Run *run) override;

    // Called when the simulation end (master thread only)
    void EndSimulationAction() override;

    int fNumberOfAbsorbedEvents;

protected:

    // Local data for the threads (each one has a copy)
    struct threadLocalT {
        bool fCurrentEventHasBeenStored;
    };
    G4Cache<threadLocalT> fThreadLocalData;

    std::string fOutputFilename;
    std::string fHitsCollectionName;
    std::vector<std::string> fUserHitAttributeNames;
    GamHitsCollection *fHits;
    bool fDebug;
    bool fStoreAbsorbedEvent;
};

#endif // GamPhaseSpaceActor_h
