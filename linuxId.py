import subprocess as s
import platform
from numpy import byte, std


class MacineId:

    def getMachineId(self, os_name: str):
        if(os_name == "Linux") :
            pipe = s.Popen(["dmidecode", "-s", "system-uuid"], stdout = s.PIPE)
            p, err = pipe.communicate()
            return p.splitlines()[0]

        else:
            pipe = s.Popen(["wmic", "csproduct", "get", "UUID"], stdout = s.PIPE)
            p, err = pipe.communicate()
            return p.splitlines()[0]

    def getDiskId(self, os_name: str) -> byte:
        if(os_name == "Linux") :
            pipe = s.Popen(["lsblk", "--nodeps", "-o", "serial"], stdout = s.PIPE)
            p, err = pipe.communicate()
            return p.splitlines()[1]
        else:
            pipe = s.Popen(["wmic", "diskdrive", "get", "SerialNumber"], stdout = s.PIPE)
            p, err = pipe.communicate()
            return p.splitlines()[1]

    def getTimeId(self, fname) -> byte:
        pipe = s.Popen(["stat", "-c", "‘%y’", fname], stdout=s.PIPE)
        p, err = pipe.communicate()
        return p

    def getId(self) -> byte: 
        os_name = platform.system()
        #print(type(self.getMachineId(os_name)+bytes('\n', 'utf-8')+self.getDiskId(os_name)+bytes('\n', 'utf-8')+self.getTimeId("test.txt")))
        return self.getMachineId(os_name)+bytes('\n', 'utf-8')+self.getDiskId(os_name)+bytes('\n', 'utf-8')+self.getTimeId("test.txt")


if __name__ == "__main__":
    m = MacineId()

    m.getId()
