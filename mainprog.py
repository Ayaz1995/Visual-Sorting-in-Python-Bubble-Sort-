import sys
import random
from matplotlib import pyplot as plt
from matplotlib import animation
from extra.data import Data
from extra.bubble_sort import bubble_sort

def create_original_data():
    data = []
    data = list(range(1, Data.data_count + 1))
    random.shuffle(data)
    return data


def draw_chart(ar_data,finterval):
    fig = plt.figure(1, figsize=(15, 9))
    data_set = [Data(d) for d in ar_data]
    axs = fig.add_subplot(111)
    axs.set_xticks([])
    axs.set_yticks([])
    plt.subplots_adjust(left=0.01, bottom=0.10, right=0.99, top=0.95,
                        wspace=0.05, hspace=0.15)
    
    frames = bubble_sort(data_set)
    def animate(fi):
        bars = []
        if(len(frames) > fi):
            axs.cla()
            axs.set_xticks([])
            axs.set_yticks([])
            bars += axs.bar(list(range(Data.data_count)),        
                            [d.value for d in frames[fi]],      
                            1,                                   
                            color=[d.color for d in frames[fi]],
                            tick_label=[d.value for d in frames[fi]]
                            ).get_children()
        return bars

    anim = animation.FuncAnimation(fig, animate, frames=len(frames), interval=finterval,repeat=False)
    return plt, anim
    
    

if __name__ == "__main__":
    try:
        Data.data_count = int(input('Please set the number of items to be sorted(32): '))
    except:
        Data.data_count = 32
    
    od = create_original_data()
    try:
        fi = int(input('Please set the frame interval(100): '))
    except:
        fi = 100
    plt, b= draw_chart(od, fi)
    plt.show()