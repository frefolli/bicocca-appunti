import numpy
import matplotlib.pyplot

def plot_radar(file: str, labels: numpy.ndarray, data: numpy.ndarray):
  n = len(labels)
  # Define the values for each attribute
  values = numpy.array(data)
  values = numpy.append(values, values[0])  # Close the radar chart
  # Compute the angle for each axis
  angles = numpy.linspace(0, 2 * numpy.pi, n, endpoint=False).tolist()
  angles += angles[:1]  # Close the radar chart
  # Create the radar chart
  fig, ax = matplotlib.pyplot.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
  # ax.set(rmin=0)
  ax.fill(angles, values, color='blue', alpha=0.3)
  ax.plot(angles, values, color='blue', linewidth=2)
  ax.set_rgrids([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], labels=['0', '10', '20', '30', '40', '50', '60', '70', '80', '90', '100'], angle=0, fontsize=10)
  ax.set_xticks(angles[:-1])
  ax.set_xticklabels(labels)
  ax.set_yticklabels([])  # Hide radial labels
  matplotlib.pyplot.savefig(file)

def main():
  labels = numpy.array(["Complexity", "Frequency",
                        "Delay", "Location",
                        "Extra flows", "Intra flows",
                        "Sharing", "Control flows"])
  files = ['metriche-livellata.png', 'metriche-settoriale.png']
  data = [numpy.array([30,60,70,0,40,40,10,10]),
          numpy.array([30,60,60,0,40,30,10,0])]
  for file, data_ in zip(files, data):
    plot_radar(file, labels, data_)

if __name__ == "__main__":
  main()
