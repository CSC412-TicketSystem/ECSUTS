import uuid
from django.db import models

# Create your models here.

#Two different tables:
# 1) student_info => will hold information such as (first & last name, residence hall, issues, etc.)
# 2) student_ticket => will create a student ticket number

class studentInfo(models.Model):
    student_name = models.CharField(max_length=150)
    
    UNIVERSITY_SUITES = 'US'
    UNIVERSITY_TOWERS = 'UT'
    VIKING_TOWERS = 'VT'
    VIKING_VILLAGE = 'VV'
    
    RESID_CHOICES = (
        (UNIVERSITY_SUITES, 'University Suites'),
        (UNIVERSITY_TOWERS, 'University Towers'),
        (VIKING_TOWERS, 'Viking Towers'),
        (VIKING_VILLAGE, 'Viking Village'),
    )
    
    Residence_Hall = models.CharField(
        max_length = 12,
        choices=RESID_CHOICES,
        default=''
        )
    
    room_Number = models.CharField(max_length=10)
    
    occupant = (
        ('single', 'Single'),
        ('double', 'Double'),
    )
    
    occupancy = models.CharField(max_length=10, choices=occupant)
    
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
        default=''
    )
    
    #rankOfTicket = models.IntegerField(null=True)
    rank_Of_Ticket = models.CharField(max_length=1, default='')
    brief_Description = models.CharField(max_length=300)
    studentEmail = models.EmailField(max_length=250, default='')
    
    def __str__(self):
        return u'%s %s %s %s %s %s %s %s %s' % (self.first_name, self.last_name, self.resid_hall, self.room_num, self.occupancy, self.issues, self.rankOfTicket, self.briefDescription, self.studentEmail)
    
    
    class studentTicket(models.Model):
        #ticket_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        studentinfo = models.ForeignKey('studentInfo', on_delete=models.CASCADE);
        
        
