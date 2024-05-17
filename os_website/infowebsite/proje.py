from flask import Flask, render_template
import sub_prosesor
import python_version
import sistem_bilgisi
import platform_psutils
app = Flask(__name__)

@app.route('/')
def index():
    blk_output = sub_prosesor.lsblk()
    cpu_output = sub_prosesor.lscpu()
    sys_output = sistem_bilgisi.platform()
    pyver = python_version.version()
    platfrm_outputs2 = platform_psutils.platformsOutputs()
    cpuCoreValue = platform_psutils.aboutCpus()
    networkinfo = platform_psutils.aboutNetwork()
    return render_template('index.html', 
                           blk_output=blk_output, 
                           cpu_output=cpu_output , 
                           sys_output = sys_output,
                           pyver = pyver,
                           plat_psu = platfrm_outputs2,
                           psu_coreCount = cpuCoreValue,
                           networkInfo = networkinfo)


def cpuAndBlk():
    blk_output = lsblk()
    cpu_output = lscpu()



if __name__ == '__main__':
    app.run(host= "0.0.0.0",debug=True)
