import pygame
import sys
import time
import multiprocessing as mp
import queue
from typing import List


class MagicList(list):
    def __init__(self, iterable, delay=10):
        super().__init__(iterable)
        self.delay=10
        self.queue = mp.Queue()
        self.process = mp.Process(target=MagicList._visu, args=(self.queue,))
        self.process.start()
        self.__triggerUpdate()

    def __setitem__(self, index, item):
        super().__setitem__(index, item)
        self.__triggerUpdate()

    def insert(self, index, item):
        super().insert(index, item)
        self.__triggerUpdate()

    def append(self, item):
        super().append(item)
        self.__triggerUpdate()

    def extend(self, other):
        super().extend(other)
        self.__triggerUpdate()
        
    def sort(self):
        raise RuntimeError("Programmier's selber!")
        
        
    def join(self):
        self.process.join()
        
    def _visu(queueue: mp.Queue):
        def _draw_list(l: List):
            screen.fill(WHITE)

            # Calculate the width of each rectangle based on the number of elements
            rect_width = WIDTH // len(l)

            for i, value in enumerate(l):
                rect_height = value * 10  # Adjust the height of the rectangle based on the list value
                pygame.draw.rect(screen, BLACK, (i * rect_width, HEIGHT - rect_height, rect_width, rect_height))

            pygame.display.flip()
            
        
        # Initialize pygame
        pygame.init()
        currList = []
        
        # Constants
        WIDTH, HEIGHT = 800, 600
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        FPS = 24
        
        # Create a window
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Real-Time List Visualization")
        clock = pygame.time.Clock()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Get newest list if available
            try:
                newestList = queueue.get_nowait()
                currList = newestList
            except queue.Empty:
                pass
            
            _draw_list(currList)
            clock.tick(FPS)
        
    def __triggerUpdate(self):
        # put list to queue
        self.queue.put(self.copy())      
        time.sleep(self.delay)
    

