from mesa import Agent

import random

class TreeCell(Agent):
    """
    A tree cell.

    Attributes:
        x, y: Grid coordinates
        condition: Can be "Fine", "On Fire", or "Burned Out"
        unique_id: (x,y) tuple.

    unique_id isn't strictly necessary here, but it's good
    practice to give one to each agent anyway.
    """

    def __init__(self, pos, model, biome):
        """
        Create a new tree.
        Args:
            pos: The tree's coordinates on the grid.
            model: standard model reference for agent.
            biome: biome
        """
        super().__init__(pos, model)
        self.pos = pos
        self.condition = "Fine"
        self.biome = biome

    def step(self):
        """
        If the tree is on fire, spread it to fine trees nearby.

        If biome = Amazonia: Fogo tem menos intensidade e menos chance de espalhar
                   Cerrado:  Fogo com alta intensidade e mais chance de espalhar
                   Mata Atlantica: Fogo com media intensidade
                   Caatinga: Espalha com certeza
                   Pantanal: Fogo não espalha
        """
        if self.condition == "On Fire":
            if self.biome != "Default":
                for neighbor in self.model.grid.neighbor_iter(self.pos):
                    if neighbor.condition == "Fine":
                        spread = random.randint(0, 10)
                        if self.biome == "Amazonia":
                            if spread >= 5:
                                neighbor.condition = "On Fire"

                        elif self.biome == "Mata Atlantica":
                            if spread >= 3:
                                neighbor.condition = "On Fire"

                        elif self.biome == "Cerrado":
                            if spread >= 1:
                                neighbor.condition = "On Fire"

                        elif self.biome == "Caatinga":
                            neighbor.condition = "On Fire"
            else:
                for neighbor in self.model.grid.neighbor_iter(self.pos):
                        if neighbor.condition == "Fine":
                            neighbor.condition = "On Fire"

            self.condition = "Burned Out"
