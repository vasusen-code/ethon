import subprocess 

def bash(cmd):    
    bashCommand = f"{cmd}"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE) 
    output, error = process.communicate()
    return output, error
    
