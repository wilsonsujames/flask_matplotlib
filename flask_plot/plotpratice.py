
import io
import random
from flask import Response, Flask,render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot.png')
def plot_png():
     #fig=plt.Figure() 如果只有一張圖的用法
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    # axis.scatter()
    # axis.legend()
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)


    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')




if __name__ == "__main__":
    app.run(debug=True)    