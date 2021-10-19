import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import argparse, sys


VERSION = "0.1.0"

def plot_data(path:str):
    data = []
    try:
        with open(path, "r") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                data.append(line.split()[1])
        data = data[1:]
        data = [float(val) for val in data]
    except:
        print("Bad path or bad file format")
        sys.exit(0)
    # print(data)
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()
    plt.title("Test graph", fontsize = 24)
    plt.xlabel("Sample", fontsize = 14)
    plt.ylabel("Adc value", fontsize = 14)
    plt.plot(data)
    plt.show()

def main():
    parser = argparse.ArgumentParser(prog='BmsGraph', description='Tool for visualisation data from BMS v' + VERSION)
    parser.add_argument('-f', '--file', type=str, help='File with data from BMS', required=True)
    try:
        args = parser.parse_args()
    except:
        return
    plot_data(args.file)


if __name__ == "__main__":
    main()