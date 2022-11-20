
import os
import datetime

def digest_path(path:list) -> list:
    """Function that digest path"""
    if os.path.isfile(path):
        path = [path]

    elif os.path.isdir(path): 
        path_r = list()
        for (dir, _, files) in os.walk(path): 
            for f in files: 
                path_temp = os.path.join(dir, f)
                if os.path.isfile(path_temp) \
                    and (path_temp[-4:].lower()==".txt" or path_temp[-4:].lower()==".log"):
                    path_r.append(path_temp)
        
        path = path_r

    return path

def mflip(ips: list) -> str:
    """main program function"""
    return  max(set(ips), key = ips.count)

def efip(ips: list) -> str:
    """main program function"""
    return min(set(ips), key = ips.count)

def eps(timestamps:  list) -> float:
    """main program function"""
    return len(timestamps)/(max(timestamps) - min(timestamps))

def bytes_(by_tes: list) -> float:
    """main program function"""
    return sum(by_tes)
