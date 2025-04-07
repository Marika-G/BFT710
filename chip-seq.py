#!/bin/env python3

import os
import sys

def read_config(filename):
    """
    Read the parameters from config file, use '=' to split key and value, and return a dictionary of param.
    """
    config = {}
    with open(filename, 'r') as config_file:
        for line in config_file:  # Read line by line
            if line[0] != "#": 
                key, value = line.strip().split('=')  # Removes the EOL and split on =
                config[key] = value

    return config


def read_readset(readset_filename):
    """
    Read the readsets from a file and returns a dictionary of {'samples' : 'file_path'}.
    """
    readset = {}
    #à compléter!!
    
    return readset


def header_submission_file(config):
    """
    Return the shebang and the file header containing SBATCH arguments from the slurm config file.
    """
    shebang = "#!/bin/bash"
    
    sbatch_args = ""
    for arg, value in config.items():
        sbatch_args += f"#SBATCH --{arg}={value}\n"
        
    return f"{shebang}\n\n{sbatch_args}"


def load_modules(config):
    """
    Return the commands to load the modules from the commands config file.
    """
    delimiter="#####################"
    comment="# Load Modules"
    cmd=""
    #à compléter!!
    
    return f"{delimiter}\n{comment}\n{delimiter}\n{cmd}"


def job_header(jobName,sample,jobOutdir):
    """
    Create a job header specifying the job name, the sample to be processed and the output directory.
    """
    delimiter="#####################"
    jobNameLine=f"# JobName = {jobName}_{sample}"
    sampleName=f"# SampleName = {sample}"
    outputdirName=f"# OutputDir = {jobOutdir}"

    return f"{delimiter}\n{jobNameLine}\n{sampleName}\n{outputdirName}\n{delimiter}"


def bwa(sample, path, outdir): #à compléter!!
    """
    Return a formatted `bwa + samtools` command.
    """
    jobOutdir = outdir + sample + '/'
    jobHeader = job_header("BWA", sample, jobOutdir)
    
    cmd=f"mkdir -p {jobOutdir}\n"
    cmd+=f"bwa mem -t 6" #à compléter!!

    return f"{jobHeader}\n{cmd}\n"


#Ajouter les autres définitions de fonctions!



#Main function
def main(readset_filename, slurm_config_filename, cmd_config_filename):
    #read the slurm and commands config files
    slurm_config = read_config(slurm_config_filename)
    cmd_config = read_config(cmd_config_filename)  

    #print file header (shebang, slurm args and modules to load)
    print(header_submission_file(slurm_config))
    print(load_modules(cmd_config))

    #read the readset file
    readset = read_readset(readset_filename) 

    #loop on each sample and print the call to the different tools
    output_dir = os.getcwd() + '/output/'
    #à compléter!!
    #for...
    print(f'echo "***End of the script {sys.argv[0]}***"')


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f'Missing argument(s). Expected {sys.argv[0]} <readset file> <slurm config file> <commands config file>')
        exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])
