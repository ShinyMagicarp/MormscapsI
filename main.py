import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

import math
from math import sqrt


class mainpage(GridLayout):
    
    def __init__(self, **kwargs):
        super(mainpage, self).__init__(**kwargs)

        self.title = AnchorLayout()
        self.appname = Label(text = 'CAPS', font_size = 77, color=(0,0.5,1,1))
        self.title.add_widget(self.appname)
        self.add_widget(self.title)
        self.title.anchor_y = 'top'
        self.title.anchor_x = 'center'

        self.anchor_layout_label = AnchorLayout()
        self.label = Label(text="Pick a Conic Section", size_hint_y=None, height=50, size_hint_x=None, width=400)
        self.anchor_layout_label.add_widget(self.label)
        self.add_widget(self.anchor_layout_label)
        self.anchor_layout_label.anchor_x = 'center'
        
        self.cols = 1

        self.al_circle = AnchorLayout()
        self.enter = Button(text="Circle", size_hint_y=None, height=180, size_hint_x=None, width=600)
        self.al_circle.add_widget(self.enter)
        self.add_widget(self.al_circle)
        self.enter.bind(on_press=self.press)
        self.al_circle.anchor_x = 'center'

        self.al_parabola = AnchorLayout()
        self.enter = Button(text="Parabola", size_hint_y=None, height=180, size_hint_x=None, width=600)
        self.al_parabola.add_widget(self.enter)
        self.add_widget(self.al_parabola)
        self.enter.bind(on_press=self.press1)
        self.al_parabola.anchor_x = 'center'

        self.al_ellipse = AnchorLayout()
        self.enter = Button(text="Ellipse", size_hint_y=None, height=180, size_hint_x=None, width=600)
        self.al_ellipse.add_widget(self.enter)
        self.add_widget(self.al_ellipse)
        self.enter.bind(on_press=self.press2)
        self.al_ellipse.anchor_x = 'center'

        self.al_hyperbola = AnchorLayout()
        self.enter = Button(text="Hyperbola", size_hint_y=None, height=180, size_hint_x=None, width=600)
        self.al_hyperbola.add_widget(self.enter)
        self.add_widget(self.al_hyperbola)
        self.enter.bind(on_press=self.press3)
        self.al_hyperbola.anchor_x = 'center'

        
    
    def press(self, instance):
            self.clear_widgets()
            self.add_widget(circlepage())
    def press1(self, instance):
            self.clear_widgets()
            self.add_widget(parabolapage())
    def press2(self, instance):
            self.clear_widgets()
            self.add_widget(ellipsepage())
    def press3(self, instance):
            self.clear_widgets()
            self.add_widget(hyperbolapage())
        


class circlepage(GridLayout): 
    def __init__(self, **kwargs):
        self.cols = 1
        super(circlepage, self).__init__(**kwargs)

        self.a_grid = GridLayout(
            row_force_default=True,
            row_default_height=70,
            col_force_default=True,
            col_default_width=720
            )
        self.tp_grid = GridLayout(
            row_force_default=True,
            row_default_height=70,
            col_force_default=True,
            col_default_width=720
        )
        self.tp_grid.cols = 1

        self.bt_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=68
        )
        self.bt_grid.cols = 10
        self.bt_grid.rows = 1
#background_color=(1,1,1,1)
        self.al = AnchorLayout()
        self.al.anchor_x = 'center'
        self.al.anchor_y = 'top'

        self.a_grid.add_widget(Label(text='Circle', font_size = 40)) 
        self.a_grid.add_widget(Label(text='                Center, Radius, and\nGeneral form of the equation Finder'))
        self.a_grid.cols = 1
        self.a_grid.rows = 9

        self.bt_grid.add_widget(Label(text='( x', font_size = 32))
        self.op1 = TextInput(multiline = False, font_size = 28)
        self.bt_grid.add_widget(self.op1)
        self.h = TextInput(multiline = False, font_size = 28)
        self.bt_grid.add_widget(self.h)
        self.bt_grid.add_widget(Label(text=')²', font_size = 32))
        self.bt_grid.add_widget(Label(text=' + ', font_size = 32))
        self.bt_grid.add_widget(Label(text='( y', font_size = 32))
        self.op2 = TextInput(multiline = False, font_size = 28)
        self.bt_grid.add_widget(self.op2)
        self.k = TextInput(multiline = False, font_size = 28)
        self.bt_grid.add_widget(self.k)
        self.bt_grid.add_widget(Label(text='  )² =  ', font_size = 32))
        self.r2 = TextInput(multiline = False , font_size = 28)
        self.bt_grid.add_widget(self.r2)
        self.r2.size_hint_y = None  # Disable relative sizing
        self.r2.height = 40  # Set fixed height
        self.r2.size_hint_x = None  # Disable relative sizing
        self.r2.width = 80 # Set fixed width
        self.add_widget(self.al)

        self.submit = Button(text="Submit Circle Equation")
        self.tp_grid.add_widget(self.submit)
        self.submit.bind(on_press=self.press)

        self.submit = Button(text="clear")
        self.tp_grid.add_widget(self.submit)
        self.submit.bind(on_press=self.press1)

        self.returnpage = Button(text="Return")
        self.tp_grid.add_widget(self.returnpage)
        self.returnpage.bind(on_press=self.press2)

        self.add_widget(self.a_grid)
        self.add_widget(self.bt_grid)
        self.add_widget(self.tp_grid)
        self.pressed = 1


    def press2(self, instance):
        self.clear_widgets()
        self.add_widget(mainpage())

    def press1( self , instance):
        self.clear_widgets()
        self.pressed = 1
        self.add_widget(circlepage())

    def press(self , instance):
        try:
            op1 = self.op1.text
            h = int(self.h.text)
            op2 = self.op2.text
            k = int(self.k.text)
            r2 = int(self.r2.text)
            ex = h
            dy = k

            if (op1 == '+'):
                h = h*-1
            if (op2 == '+'):
                k = k*-1
            if (op1 == '-'):
                h = h
            if (op2 == '-'):
                k = k

            r = sqrt(r2)
            Ex = 2*ex
            Dy = 2*dy
            f = (r2*-1)+(ex*ex)+(dy*dy)
            if f < 0:
                op3 = '-'
                f*-1
            if f > 0:
                op3 = '+'
            if self.pressed != 0:
                self.a_grid.add_widget(Label(text=f'\n\ncenter: ({h},{k})\nradius: {r}\nGeneral form: x²+y²{op1}{Ex}x{op2}{Dy}y{op3}{f}=0' ,color = ( 0,1,0,1)))
                #self.a_grid.add_widget(Label(text=f'radius: {r}',color = ( 0,1,0,1)))
                #self.a_grid.add_widget(Label(text=f'General form: x²+y²{op1}{Ex}x{op2}{Dy}y{op3}{f}=0',color = ( 0,1,0,1)))
                #self.a_grid.add_widget(Label(text=' '))

        except (TypeError, ValueError):
            self.a_grid.add_widget(Label(text=f"An error occurred", color=(1, 0, 0, 1)))
        finally:
            self.pressed = 0


class parabolapage(GridLayout):
    def __init__(self, **kwargs):
        self.cols = 1
        super(parabolapage, self).__init__(**kwargs)

        self.a_grid = GridLayout(
            row_force_default=True,
            row_default_height=70,
            col_force_default=True,
            col_default_width=720
            )
        self.tp_grid = GridLayout(
            row_force_default=True,
            row_default_height=70,
            col_force_default=True,
            col_default_width=720
        )
        self.tp_grid.cols = 1

        self.bt_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=60
        )
        self.bt_grid.cols = 12
        self.bt_grid.rows = 2
#background_color=(1,1,1,1)
        self.al = AnchorLayout()
        self.al.anchor_x = 'center'
        self.al.anchor_y = 'top'

        self.a_grid.add_widget(Label(text='Parabola', font_size = 40)) 
        self.a_grid.add_widget(Label(text='      vertex, latus rectum, directrix,\nfocus and parabola orientation finder'))
        self.a_grid.cols = 1

        self.bt_grid.add_widget(Label(text='(',font_size = 32))
        self.v1 = TextInput(multiline = False, font_size = 25)
        self.bt_grid.add_widget(self.v1)
        self.op1 = TextInput(multiline = False, font_size = 25)
        self.bt_grid.add_widget(self.op1)
        self.vv1 = TextInput(multiline = False, font_size = 25)
        self.bt_grid.add_widget(self.vv1)
        self.bt_grid.add_widget(Label(text=')²',font_size = 32))
        self.bt_grid.add_widget(Label(text='=',font_size = 32))
        self.p4 = TextInput(multiline = False, font_size = 25, size_hint_x = None, width = 50)
        self.bt_grid.add_widget(self.p4)
        self.bt_grid.add_widget(Label(text=' (',font_size = 32))
        self.v2 = TextInput(multiline = False, font_size = 25)
        self.bt_grid.add_widget(self.v2)
        self.op2 = TextInput(multiline = False, font_size = 25)
        self.bt_grid.add_widget(self.op2)
        self.vv2 = TextInput(multiline = False, font_size = 25)
        self.bt_grid.add_widget(self.vv2)
        self.bt_grid.add_widget(Label(text=')²',font_size = 32))


        self.add_widget(self.al)

        self.submit = Button(text="Submit Parabola Equation")
        self.tp_grid.add_widget(self.submit)
        self.submit.bind(on_press=self.press)

        self.submit = Button(text="clear")
        self.tp_grid.add_widget(self.submit)
        self.submit.bind(on_press=self.press1)

        self.returnpage = Button(text="Return")
        self.tp_grid.add_widget(self.returnpage)
        self.returnpage.bind(on_press=self.press2)

        self.add_widget(self.a_grid)
        self.add_widget(self.bt_grid)
        self.add_widget(self.tp_grid)
        self.pressed = 1


    def press2(self, instance):
        self.clear_widgets()
        self.add_widget(mainpage())

    def press1( self , instance):
        self.clear_widgets()
        self.pressed = 1
        self.add_widget(parabolapage())

    def press(self, instance):
        try:
            v1 = self.v1.text
            v2 = self.v2.text
            op1 = self.op1.text
            op2 = self.op2.text
            vv1 = int(self.vv1.text)
            vv2 = int(self.vv2.text)
            p4 = int(self.p4.text)

            p = p4 / 4

            if v1 == 'x':
                if op1 == '-':
                    h = vv1
                elif op1 == '+':
                    h = vv1 * -1
                if op2 == '-':
                    k = vv2
                elif op2 == '+':
                    k = vv2 * -1
                directrix = 'y = '
                dx = k - p
                fc2 = k + p
                fc = h
                lra1 = h + (p4 / 2)
                lra2 = k + p
                lrb1 = h - (p4/2)
                lrb2 = k + p
                if p4 < 0:
                    ortn = 'downward'
                if p4 > 0:
                    ortn = 'upward'
            elif v1 == 'y':
                if op1 == '-':
                    k = vv1
                elif op1 == '+':
                    k = vv1 * -1
                if op2 == '-':
                    h = vv2
                elif op2 == '+':
                    h = vv2 * -1
                directrix = 'x = '
                dx = h - p
                fc = h + p
                fc2 = k
                lra1 = h + p
                lra2 = k + (p4 / 2)
                lrb1 = h + p
                lrb2 = k - (p4/4)
                if p4 < 0:
                    ortn = 'leftward'
                if p4 > 0:
                    ortn = 'rightward'

            if self.pressed != 0:
                self.a_grid.add_widget(Label(text=f"\n\nvertex: ({h}, {k})      directrix: {directrix}{dx}\nfocus: ({fc}, {fc2})    orientation: {ortn}\nlatus rectum: L1({lra1}, {lra2}) ,L2({lrb1}, {lrb2})", color = (0,1,0,1)))
        except (ValueError, TypeError):
            self.a_grid.add_widget(Label(text=f"An error occurred", color=(1, 0, 0, 1)))
        finally:
            self.pressed = 0

class ellipsepage(GridLayout): 
    def __init__(self, **kwargs):
        self.cols = 1
        super(ellipsepage, self).__init__(**kwargs)

        self.a_grid = GridLayout(
            row_force_default=True,
            row_default_height=70,
            col_force_default=True,
            col_default_width=720
            )
        self.tp_grid = GridLayout(
            row_force_default=True,
            row_default_height=70,
            col_force_default=True,
            col_default_width=720
        )
        self.tp_grid.cols = 1

        self.bt_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=68
        )
        self.bt_grid.cols = 10
        self.bt_grid.rows = 1
#background_color=(1,1,1,1)
        self.al = AnchorLayout()
        self.al.anchor_x = 'center'
        self.al.anchor_y = 'top'

        self.a_grid.add_widget(Label(text='Ellipse', font_size = 40)) 
        self.a_grid.add_widget(Label(text=' ^ _ ^'))
        self.a_grid.cols = 1
        self.a_grid.rows = 9

        self.bt_grid.add_widget(Label(text='( x', font_size = 32))
        self.op1 = TextInput(multiline = False, font_size = 28)
        self.bt_grid.add_widget(self.op1)
        self.h = TextInput(multiline = False, font_size = 28)
        self.bt_grid.add_widget(self.h)
        self.bt_grid.add_widget(Label(text=')²', font_size = 32))
        self.bt_grid.add_widget(Label(text=' + ', font_size = 32))
        self.bt_grid.add_widget(Label(text='( y', font_size = 32))
        self.op2 = TextInput(multiline = False, font_size = 28)
        self.bt_grid.add_widget(self.op2)
        self.k = TextInput(multiline = False, font_size = 28)
        self.bt_grid.add_widget(self.k)
        self.bt_grid.add_widget(Label(text='  )² =  ', font_size = 32))
        self.r2 = TextInput(multiline = False , font_size = 28)
        self.bt_grid.add_widget(self.r2)
        self.r2.size_hint_y = None  # Disable relative sizing
        self.r2.height = 40  # Set fixed height
        self.r2.size_hint_x = None  # Disable relative sizing
        self.r2.width = 75  # Set fixed width
        self.add_widget(self.al)

        self.submit = Button(text="Submit Ellipse Equation")
        self.tp_grid.add_widget(self.submit)
        self.submit.bind(on_press=self.press)

        self.submit = Button(text="clear")
        self.tp_grid.add_widget(self.submit)
        self.submit.bind(on_press=self.press1)

        self.returnpage = Button(text="Return")
        self.tp_grid.add_widget(self.returnpage)
        self.returnpage.bind(on_press=self.press2)

        self.add_widget(self.a_grid)
        self.add_widget(self.bt_grid)
        self.add_widget(self.tp_grid)
        self.pressed = 1


    def press2(self, instance):
        self.clear_widgets()
        self.add_widget(mainpage())

    def press1( self , instance):
        self.clear_widgets()
        self.pressed = 1
        self.add_widget(ellipsepage())

    def press(self , instance):
        try:
            
            if self.pressed != 0:
                self.a_grid.add_widget(Label(text='coming soon' ,color = ( 0,0,1,1)))
                
        except (TypeError, ValueError):
            self.a_grid.add_widget(Label(text=f"An error occurred", color=(1, 0, 0, 1)))
        finally:
            self.pressed = 0



class hyperbolapage(GridLayout): 
    def __init__(self, **kwargs):
        self.cols = 1
        super(hyperbolapage, self).__init__(**kwargs)

        self.a_grid = GridLayout(
            row_force_default=True,
            row_default_height=70,
            col_force_default=True,
            col_default_width=720
            )
        self.tp_grid = GridLayout(
            row_force_default=True,
            row_default_height=70,
            col_force_default=True,
            col_default_width=720
        )
        self.tp_grid.cols = 1

        self.bt_grid = GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=68
        )
        self.bt_grid.cols = 10
        self.bt_grid.rows = 1
#background_color=(1,1,1,1)
        self.al = AnchorLayout()
        self.al.anchor_x = 'center'
        self.al.anchor_y = 'top'

        self.a_grid.add_widget(Label(text='Hyperbola', font_size = 40)) 
        self.a_grid.add_widget(Label(text=' ^ _ ^'))
        self.a_grid.cols = 1
        self.a_grid.rows = 9

        self.bt_grid.add_widget(Label(text='( x', font_size = 32))
        self.op1 = TextInput(multiline = False, font_size = 28)
        self.bt_grid.add_widget(self.op1)
        self.h = TextInput(multiline = False, font_size = 28)
        self.bt_grid.add_widget(self.h)
        self.bt_grid.add_widget(Label(text=')²', font_size = 32))
        self.bt_grid.add_widget(Label(text=' + ', font_size = 32))
        self.bt_grid.add_widget(Label(text='( y', font_size = 32))
        self.op2 = TextInput(multiline = False, font_size = 28)
        self.bt_grid.add_widget(self.op2)
        self.k = TextInput(multiline = False, font_size = 28)
        self.bt_grid.add_widget(self.k)
        self.bt_grid.add_widget(Label(text='  )² =  ', font_size = 32))
        self.r2 = TextInput(multiline = False , font_size = 28)
        self.bt_grid.add_widget(self.r2)
        self.r2.size_hint_y = None  # Disable relative sizing
        self.r2.height = 40  # Set fixed height
        self.r2.size_hint_x = None  # Disable relative sizing
        self.r2.width = 75  # Set fixed width
        self.add_widget(self.al)

        self.submit = Button(text="Submit Hyperbola Equation")
        self.tp_grid.add_widget(self.submit)
        self.submit.bind(on_press=self.press)

        self.submit = Button(text="clear")
        self.tp_grid.add_widget(self.submit)
        self.submit.bind(on_press=self.press1)

        self.returnpage = Button(text="Return")
        self.tp_grid.add_widget(self.returnpage)
        self.returnpage.bind(on_press=self.press2)

        self.add_widget(self.a_grid)
        self.add_widget(self.bt_grid)
        self.add_widget(self.tp_grid)
        self.pressed = 1


    def press2(self, instance):
        self.clear_widgets()
        self.add_widget(mainpage())

    def press1( self , instance):
        self.clear_widgets()
        self.pressed = 1
        self.add_widget(hyperbolapage())

    def press(self , instance):
        try:
            
            if self.pressed != 0:
                self.a_grid.add_widget(Label(text='coming soon' ,color = ( 0,0,1,1)))
                
        except (TypeError, ValueError):
            self.a_grid.add_widget(Label(text=f"An error occurred", color=(1, 0, 0, 1)))
        finally:
            self.pressed = 0


class CAPS(App):
    def build(self):
        return mainpage()
    
if __name__ == '__main__':
    CAPS().run()
