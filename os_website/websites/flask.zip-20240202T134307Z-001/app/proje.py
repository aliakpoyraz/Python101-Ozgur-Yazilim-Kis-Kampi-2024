from flask import Flask, render_template
import sub_prosesor
app = Flask(__name__)

@app.route('/')
def index():
    blk_output = sub_prosesor.lsblk()
    #cpu_output = sub_prosesor.lscpu()

    return render_template('index.html', blk_output=blk_output)#, cpu_output=cpu_output)


def cpuAndBlk():
    blk_output = lsblk()
    cpu_output = lscpu()

if __name__ == '__main__':
    app.run(debug=True)
