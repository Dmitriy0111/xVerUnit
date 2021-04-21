#
# File          : xVerUnit.py
# Autor         : Vlasov D.V.
# Data          : 14.04.2021
# Language      : Python
# Description   : main class for generating tcl scripts and run simulation processes
# Copyright(c)  : 2021 Vlasov D.V.
#

import os

from xVerUnit.sim_tools.tcl_modelsim_wrapper import tcl_modelsim_wrapper

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
                            "extra_opt" : [],
                            "post_sim"  : [],
                            "run_dir"   : "run",
                            "tb_name"   : "tb",
                            "run_opt"   : "-c -onfinish stop -onfinish final"
                            }

    def set_sim(self, sim_name):
        self.sim_params["sim_name"] = sim_name

    def set_tb_name(self, tb_name):
        self.sim_params["tb_name"] = tb_name

    def set_sv_std(self, sv_std):
        self.sim_params["lang_std"][0] = sv_std

    def set_v_std(self, v_std):
        self.sim_params["lang_std"][1] = v_std

    def set_vhdl_std(self, vhdl_std):
        self.sim_params["lang_std"][2] = vhdl_std

    def add_sim_opt(self, sim_opt):
        self.sim_params["sim_opt"].append(sim_opt)

    def set_run_dir(self, run_dir):
        self.sim_params["run_dir"] = run_dir

    def add_files(self, path, lib = "work"):
        self.sim_params["sim_paths"].append([path,lib])

    def add_wave(self, key, wave):
        self.sim_params["sim_waves"].append([key,wave])

    def add_extra_opt(self, extra_opt):
        self.sim_params["extra_opt"].append(extra_opt)

    def add_post_sim(self, post_sim):
        self.sim_params["post_sim"].append(post_sim)

    def clean_post_sim(self):
        self.sim_params["post_sim"] = []

    def gen_script(self):
        tcl_wrapper = 0
        if( self.sim_params["sim_name"] == "Modelsim" ):
            tcl_wrapper = tcl_modelsim_wrapper(self.sim_params)
        tcl_wrapper.gen_script()

    def set_run_opt(self, run_opt):
        self.sim_params["run_opt"] = run_opt

    def run_test(self):
        print("Run test : " + self.sim_params["test_name"])
        os.system("mkdir sim_modelsim")
        os.system("cd sim_modelsim && vsim " + self.sim_params["run_opt"] + " -do ../" + self.sim_params["run_dir"] + "/" + self.test_name + ".tcl")
        print("Finish test : " + self.sim_params["test_name"])
