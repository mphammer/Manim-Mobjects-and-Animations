from manim import * 
import numpy as np

class AllMObjects(ThreeDScene):
    def construct(self):
        t = Text("Manim Objects")
        t.shift(UP*2.5)

        mobject_list = [
            # Geometry
            Annulus(),
            AnnularSector(),
            Arc(),
            Circle(),
            Dot(),
            Ellipse(),
            Arrow(),
            Vector(),
            Square(),
            Star(),
            Triangle(),
            ArrowCircleTip(),
            
            # Frame
            FullScreenRectangle(),
            ScreenRectangle(),

            # Graph
            Graph(vertices=(1,2,3,4,5), edges=[(1,2), (1,3), (4,2), (3,5), (1,5)]),

            # Graphing
            Axes(),
            ComplexPlane(),
            CoordinateSystem(),
            NumberPlane(),
            FunctionGraph(lambda x: (-1.0*x)**2),
            NumberLine(),
            BarChart(values=[1,2,3,4,5]),

            # Logo
            ManimBanner(),

            # Matrix
            DecimalMatrix([[1.0,2.0],[3.0,4.0]]),
            IntegerMatrix([[1,2],[3,4]]),
            Matrix([[1,2],[3,4]]),
            MobjectMatrix([[Circle(),Square()],[Star(),Triangle()]]),

            # Table
            DecimalTable([[1,2,3,4], [5,6,7,8]], row_labels=[Text("Row 1"), Text("Row 2")]),
            MathTable([["+", 0, 5, 10],[0, 0, 5, 10],[2, 2, 7, 12],[4, 4, 9, 14]],include_outer_lines=True),
            MobjectTable( [ [Circle(), Square()] , [Triangle(), Star()] ] ),

            # Text
            Code(file_name="dummy.py", language="Python"),
            DecimalNumber(5.5),
            Integer(5),
            BulletedList("Apple", "Pear", "Grape"),
            MathTex(r"\frac{a}{b} = x^{2}"),
            SingleStringMathTex(r"\frac{a}{b} = x^{2}"),
            Tex("Hello World"),
            Title("Here Is a Ttitle"),
            MarkupText('<span foreground="red" size="x-large">Red text</span> is <i>fire</i>!"'),
            Paragraph('There once was a man', 'that lived in a van', 'with only one right hand'),
            Text("Here is Text"),

            # Types
            Point(color=RED),
            PointCloudDot(),
        ]

        mobject_list_3d = [
            ThreeDAxes(),
            Dodecahedron(),
            Icosahedron(),
            Octahedron(),
            Tetrahedron(edge_length=2),
            Arrow3D(),
            Cone(),
            Cube(),
            Cylinder(),
            Dot3D(),
            Line3D(start=np.array([-3,-3,-3]), end=np.array([3,3,3])),
            Prism(),
            Sphere(),
            Torus(),
        ]

        # Show all 2D MObjects
        self.add(t)
        self.wait(0.2)
        for mobj in mobject_list:
            try:
                self.play(Transform(t,Text(mobj.name).shift(UP*2.5)), FadeIn(mobj), run_time=0.5)
                self.wait(0.5)
                self.remove(mobj)
            except:
                continue
        
        # Show all 3D MObjects
        self.play(Transform(t,Text("Looking at 3D Mobjects...").shift(UP*2.5)), run_time=0.5)
        self.wait(1)

        self.begin_3dillusion_camera_rotation(rate=4)
        self.wait(2)

        for mobj in mobject_list_3d:
            try:
                self.play(Transform(t,Text(mobj.name).shift(UP*2.5)), FadeIn(mobj), run_time=0.5)
                self.wait(1)
                self.remove(mobj)
            except:
                continue
        self.play(FadeOut(t))
        self.wait()
