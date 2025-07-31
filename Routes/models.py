from django.db import models


class Route(models.Model):
    """ This defines a route we are supposed to follow e.g
    -Thika Road
    - Wayakiway
    - Kiambu road
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Stop(models.Model):
    """ This is the desisgnated stops and pickup points
    - A route will have many stops
    - Thika Road route:
        * juja
        * kmbo etc
    - we will order the routes from top to bottom i.e the pick-up to the destination
    """
    route = models.ForeignKey(Route, related_name='stops', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField() # this is the position of the stop in the route

    class meta:
        ordering = ['oder'] # make sure that the stops are always odered correctly

    def __str__(self):
        return self.name
