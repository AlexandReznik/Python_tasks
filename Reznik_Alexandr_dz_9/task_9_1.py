from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается')
            if i == 0:
                sleep(4)
                print(TrafficLight.__color[i], 4)
            elif i == 1:
                sleep(2)
                print(TrafficLight.__color[i], 2)
            elif i == 2:
                sleep(3)
                print(TrafficLight.__color[i], 3)
            i += 1


traffic = TrafficLight()
traffic.running()

# Светофор переключается
# red 4
# Светофор переключается
# yellow 2
# Светофор переключается
# green 3
