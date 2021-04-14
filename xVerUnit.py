#
# File          : xVerUnit.py
# Autor         : Vlasov D.V.
# Data          : 14.04.2021
# Language      : Python
# Description   : main class for generating tcl scripts and run simulation processes
# Copyright(c)  : 2021 Vlasov D.V.
#

import os

from tcl_modelsim_wrapper import tcl_modelsim_wrapper

class xVerUnit:

    def __init__(self, test_name):
        self.test_name = test_name
        self.sim_params =   {
                            "test_name" : test_name,
                            "sim_name"  : "unknown", 
                            "lang_std"  : ["-sv", "-vlog01compat", "-2008"],
                            "sim_paths" : [],
                            "sim_waves" : [],
                            "sim_opt"   : [],
                            "tb_name"   : "tb",
                            "run_opt"   : "-c -onfinish stop -onfinish final"
                            }
        self.sim_name = "unknown"
        self.paths = []
        self.waves = []
        self.sim_opt = []
        self.tb_name = "tb"

    def set_sim(self, sim_name):
        self.sim_params["sim_name"] = sim_name
        self.sim_name = sim_name

    def set_tb_name(self, tb_name):
        self.sim_params["tb_name"] = tb_name
        self.tb_name = tb_name

    def set_sv_std(self, sv_std):
        self.sim_params["lang_std"][0] = sv_std

    def set_v_std(self, v_std):
        self.sim_params["lang_std"][1] = v_std

    def set_vhdl_std(self, vhdl_std):
        self.sim_params["lang_std"][2] = vhdl_std

    def add_sim_opt(self, sim_opt):
        self.sim_params["sim_opt"].append(sim_opt)
        self.sim_opt.append(sim_opt)

    def add_files(self, path, lib = "work"):
        self.sim_params["sim_paths"].append([path,lib])
        self.paths.append(path)

    def add_wave(self, key, wave):
        self.sim_params["sim_waves"].append([key,wave])
        self.waves.append([key,wave])

    def gen_script(self):
        tcl_wrapper = 0
        if( self.sim_name == "Modelsim" ):
            tcl_wrapper = tcl_modelsim_wrapper(self.sim_params)
        tcl_wrapper.gen_script()

    def set_run_opt(self, run_opt):
        self.sim_params["run_opt"] = run_opt

    def run_test(self):
        print("Run test : " + self.sim_params["test_name"])
        os.system("make sim_dir")
        os.system("cd sim_modelsim && vsim " + self.sim_params["run_opt"] + " -do ../py_run/" + self.test_name + ".tcl")
        print("Finish test : " + self.sim_params["test_name"])
