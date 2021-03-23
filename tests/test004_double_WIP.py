#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gam

# verbose level
gam.log.setLevel(gam.INFO)
gam.log.setLevel(gam.DEBUG)

# create the simulation
sim = gam.Simulation()

# main options
sim.set_g4_verbose(True)
sim.set_g4_visualisation_flag(False)
sim.set_g4_multi_thread(False)
sim.set_g4_random_engine("MersenneTwister", 123654)

# set the world size like in the Gate macro
m = gam.g4_units('m')
world = sim.world
world.size = [3 * m, 3 * m, 3 * m]

# add a simple waterbox volume
waterbox = sim.add_volume('Box', 'Waterbox')
cm = gam.g4_units('cm')
waterbox.size = [40 * cm, 40 * cm, 40 * cm]
waterbox.translation = [0 * cm, 0 * cm, 25 * cm]
waterbox.material = 'G4_WATER'

# physic list # FIXME will be changed
# print('Phys lists :', sim.get_available_physicLists())

# default source for tests
keV = gam.g4_units('keV')
mm = gam.g4_units('mm')
Bq = gam.g4_units('Bq')
source = sim.add_source('Generic', 'Default')
source.particle = 'gamma'
source.energy.mono = 80 * keV
source.direction.type = 'momentum'
source.direction.momentum = [0, 0, 1]
source.activity = 20 * Bq

# add stat actor
sim.add_actor('SimulationStatisticsActor', 'Stats')

#sim.save('a.json')
#sim = Simulation.load('a.json')
# FIXME -> cannot get result AND new RM

# create G4 objects
sim.initialize()

# start simulation
# sim.apply_g4_command("/run/verbose 1")
gam.source_log.setLevel(gam.RUN)
sim.start()
stats = sim.get_actor('Stats')
print(stats)

sim.initialized = False
sim.initialize()
sim.start()
stats = sim.get_actor('Stats')
print(stats)

# print('del sim')
# ui = sim.g4_ui  # to avoid delete
# print(ui)
# del sim.g4_RunManager
# print(ui)
# del sim
# print(ui)
# del ui
# ui = None
# print(ui)

# print('new sim')
# sim2 = gam.Simulation(ui)

# print('before init')

# sim2.initialize()
# print('after init')
# sim2.start()
# stats = sim2.get_actor('Stats')
# print(stats)
