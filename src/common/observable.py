class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, value):
        for observer in self._observers:
            observer.update_material(value)

class Observer:
    def update_material(self, value):
        pass