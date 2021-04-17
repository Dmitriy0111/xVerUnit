#
# File          : tcl_modelsim_wrapper.py
# Autor         : Vlasov D.V.
# Data          : 14.04.2021
# Language      : Python
# Description   : This is script for generating tcl script for Modelsim
# Copyright(c)  : 2021 Vlasov D.V.
#

import os
from os         import listdir
from os.path    import isfile, join

class tcl_modelsim_wrapper:

    def __init__(self, sim_params, tcl_creator_name = "Modelsim tcl creator"):
        self.sim_params = sim_params
        self.tcl_file = 0
        self.tcl_creator_name = tcl_creator_name

    def gen_script(self):
        os.system("mkdir {:s}".format(self.sim_params["run_dir"]))
        self.tcl_file = open(self.sim_params["run_dir"] + "\\" + self.sim_params["test_name"] + ".tcl", "w");
        self.write_comps()
        self.tcl_file.write("\n")
        self.write_extra_opt()
        self.tcl_file.write("\n")
        self.write_vsim()
        self.tcl_file.write("\n")
        self.write_waves()
        self.tcl_file.write("\n")
        self.tcl_file.write("run -all\n")
        self.write_post_sim()
        self.tcl_file.write("\n")
        self.tcl_file.write("quit\n")

    def write_comps(self):
        for path in self.sim_params["sim_paths"]:
            if( self.find_src_type(path[0]) == "SV" ):
                self.write_comp_str("vlog ", self.sim_params["lang_std"][0], " ../" + path[0], path[1] )
            elif( self.find_src_type(path[0]) == "V" ):
                self.write_comp_str("vlog ", self.sim_params["lang_std"][1], " ../" + path[0], path[1] )
            elif( self.find_src_type(path[0]) == "VHDL" ):
                self.write_comp_str("vcom ", self.sim_params["lang_std"][2], " ../" + path[0], path[1] )
            else:
                files = [f for f in listdir(path[0]) if isfile(join(path[0],f))]
                for file in files:
                    if( self.find_src_type(file) == "SV" ):
                        self.write_comp_str("vlog ", self.sim_params["lang_std"][0], " ../" + path[0] + "/" + file, path[1] )
                    if( self.find_src_type(file) == "V" ):
                        self.write_comp_str("vlog ", self.sim_params["lang_std"][1], " ../" + path[0] + "/" + file, path[1] )
                    if( self.find_src_type(file) == "VHDL" ):
                        self.write_comp_str("vcom ", self.sim_params["lang_std"][2], " ../" + path[0] + "/" + file, path[1] )

    def write_vsim(self):
        vsim_str = "vsim "
        for sim_opt in self.sim_params["sim_opt"]:
            vsim_str += sim_opt + " "
        vsim_str += "work." + self.sim_params["tb_name"]
        self.tcl_file.write(vsim_str + "\n")

    def write_post_sim(self):
        for post_sim in self.sim_params["post_sim"]:
            self.tcl_file.write(post_sim + "\n")

    def write_extra_opt(self):
        for extra_opt in self.sim_params["extra_opt"]:
            self.tcl_file.write(extra_opt + "\n")

    def write_waves(self):
        for wave in self.sim_params["sim_waves"]:
            if( wave[0] == "-d" ):
                self.tcl_file.write("add wave -divider " + "\"" + wave[1] + "\"\n")
            if( wave[0] == "-p" ):
                self.tcl_file.write("add wave -position insertpoint sim:/" + wave[1] + "\n")

    def find_src_type(self, name):
        if( name[-3:] == ".sv" ):
            return "SV"
        if( name[-2:] == ".v" ):
            return "V"
        if( name[-4:] == ".vhd" ):
            return "VHDL"
        return "Unknown"

    def write_comp_str(self, comp_name, lang_std, path2file, lib):
        self.tcl_file.write(comp_name + lang_std + path2file + " -work " + lib + "\n")
