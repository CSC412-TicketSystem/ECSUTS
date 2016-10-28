from django.db import models

# Create your models here.

#Two different tables:
# 1) student_info => will hold information such as (first & last name, residence hall, issues, etc.)
# 2) student_ticket => will create a student ticket number

class studentInfo(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    resid_hall = models.TextField()
    room_num = models.CharField(max_length=10)
    occupancy = models.CharField(max_length=1)
    
    BED = 'BD'
    DESK = 'DSK'
    DRESSER = 'DSSR'
    CLOSET = 'CLST'
    MATTRESS = 'MTTRESS'
    WINDOW = 'WNDOW'
    WINDOW_BLINDS = 'WNDOWBLNDS'
    WALLS = 'WLLS'
    MICROFRIDGE = 'MCROFRDGE'
    MICROWAVE = 'MCROWVE'
    DOORS = 'DOORS'
    FLOORS = 'FLOORS'
    LOCKS = 'LCKS'
    BATHROOM_SHOWER = 'BTHROOMSHWR'
    BATHROOM_WALLS = 'BTHROOMWLLS'
    BATHROOM_TOILET = 'BTHROOMTLIT'
    AIR_CONDITIONING_UNIT = 'AC'
    SINK_MIRROR = 'SNKMRROR'
    ELECTRICAL_OUTLETS = 'ELECTOUTLETS'
    LIGHTS = 'LGHTS'
    
    ISSUES_CHOICES = (
        (BED, 'Bed'),
        (DESK, 'Desk'),
        (DRESSER, 'Dresser'),
        (CLOSET, 'Closet'),
        (MATTRESS, 'Mattress'),
        (WINDOW, 'Window'),
        (WINDOW_BLINDS, 'Window_Blinds'),
        (WALLS, 'Walls'),
        (MICROFRIDGE, 'Microfridge'),
        (MICROWAVE, 'Microwave'),
        (DOORS, 'Doors'),
        (FLOORS, 'Floors'),
        (LOCKS, 'Locks'),
        (BATHROOM_SHOWER, 'Bathroom_Shower'),
        (BATHROOM_WALLS, 'Bathroom_walls'),
        (BATHROOM_TOILET, 'Bathroom_toilet'),
        (AIR_CONDITIONING_UNIT, 'Air_Conditioning_Unit'),
        (SINK_MIRROR, 'Sink/Mirror'),
        (ELECTRICAL_OUTLETS, 'Electrical_Outlets'),
        (LIGHTS, 'Lights'),
    )
    
    issues = models.CharField(
        max_length=12,
        choices=ISSUES_CHOICES, 
        default=BED
    )
    
    rankOfTicket = models.CharField(max_length=1)
    briefDescription = models.TextField()
    
    
    #class studentTicket(models.Model):
        #ticket_number = models.
