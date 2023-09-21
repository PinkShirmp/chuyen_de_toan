from manim import *
from manim_slides import Slide
import numpy as np


class TrumVN(Slide,MovingCameraScene,Scene):
    def construct(self):
        TitleTex=Tex(f"NHÓM 6")
        TitleTex.to_edge(ORIGIN)
        self.play(Write(TitleTex))
        self.next_slide()
        self.play(FadeOut(TitleTex))
        PHEPVITUTEXT=Text(f"PHÉP VỊ TỰ",font_size=64)
        PHEPVITUTEXT.to_edge(ORIGIN)    
        self.play(Write(PHEPVITUTEXT))
        self.next_slide()
        self.play(PHEPVITUTEXT.animate.to_corner(UP,0.25))

        tvn=Text("THÀNH VIÊN NHÓM")
        tvn.to_corner(UP,0.15)
        self.play(ReplacementTransform(PHEPVITUTEXT,tvn))
        self.next_slide()
        team_members=[
            "Nguyễn Phương Uyên",
            "Nguyễn Minh Tuệ",
            "Nguyễn Gia Khánh",
            "Trịnh Phương Cường",
            "Nguyễn Vũ Long",
            "Hoàng Nguyễn Phương Anh",
            "Nguyễn Đình Mạnh",
            "Phạm Anh Tú",
            "Tô Vũ Anh",
            "Đỗ Long Nhật"  
        ]
        tex_group = VGroup()
        for member in team_members:
            text = Text(member,font_size=24,color=ORANGE)
            tex_group.add(text)
        tex_group.arrange(DOWN, aligned_edge=LEFT)
        tex_group.to_edge(LEFT)
        tex_group.shift(DOWN*0.5)
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=5,
            y_length=3,
            axis_config={"include_tip": True, "numbers_to_exclude": [0]}
        ).add_coordinates()

        axes.to_edge(RIGHT)
        axes.shift(LEFT*2)
        axis_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        graph = axes.plot(lambda x:np.sin(x) ,x_range=[0,5],color=YELLOW)

        graphing_stuff = VGroup(axes, graph, axis_labels)
        self.play(Write(tex_group),DrawBorderThenFill(axes), Write(axis_labels), run_time=1)
        self.play(Create(graph), run_time=.5)
        self.next_slide()
        self.play(FadeOut(tvn),FadeOut(tex_group),FadeOut(graphing_stuff))
        self.next_slide()
        #baitoanmodau
        tit=Text("BÀI TOÁN MỞ ĐẦU",font_size=35)
        tit.to_edge(UP)
        self.play(Create(tit))
        self.next_slide()
        square_1=Rectangle(width=2.0, height=4.0)
        square_1.to_edge(ORIGIN)

        vertices = square_1.get_vertices()

        decimal_square1=DecimalNumber(num_decimal_places=0)
        decimal_square1.add_updater(lambda d: d.next_to(square_1,DOWN))
        decimal_square1.set_value(8)
        self.play(Create(square_1),Write(decimal_square1))
        self.play(square_1.animate.set_fill(GREEN,opacity=1))
        self.next_slide()
        self.play(square_1.animate.to_edge(LEFT))
        square_2 = Rectangle(width=1.0, height=2.0)
        square_2.to_edge(ORIGIN)

        decimal_square2 = DecimalNumber(num_decimal_places=0,font_size=DEFAULT_FONT_SIZE-5)
        decimal_square2.set_value(2)
        decimal_square2.add_updater(lambda d: d.next_to(square_2,DOWN))
        self.play(Create(square_2), Write(decimal_square2))
        self.play(square_2.animate.set_fill(BLUE, opacity=1))
        self.next_slide()
        dot_B_sq1=self.createDot(1,UP,square_1,"$B'$",WHITE)
        dot_A_sq1=self.createDot(2,UP,square_1,"$A'$",WHITE)
        dot_D_sq1=self.createDot(3,DOWN,square_1,"$D'$",WHITE)
        dot_C_sq1=self.createDot(4,DOWN,square_1,"$C'$",WHITE)
        gr=VGroup(dot_A_sq1[0],dot_B_sq1[0],dot_C_sq1[0],dot_D_sq1[0])
        gr1=VGroup(dot_A_sq1[1],dot_B_sq1[1],dot_C_sq1[1],dot_D_sq1[1])

        dot_B_sq2=self.createDot(1,UP,square_2,"$B$",WHITE)
        dot_A_sq2=self.createDot(2,UP,square_2,"$A$",WHITE)
        dot_D_sq2=self.createDot(3,DOWN,square_2,"$D$",WHITE)
        dot_C_sq2=self.createDot(4,DOWN,square_2,"$C$",WHITE)
      
        gr_2=VGroup(dot_A_sq2[0],dot_B_sq2[0],dot_C_sq2[0],dot_D_sq2[0])
        gr1_2=VGroup(dot_A_sq2[1],dot_B_sq2[1],dot_C_sq2[1],dot_D_sq2[1])

      
        self.play(Create(dot_A_sq1[0]), Create(dot_B_sq1[0]), Create(dot_C_sq1[0]), Create(dot_D_sq1[0]))
        self.play(Create(dot_A_sq2[0]), Create(dot_B_sq2[0]), Create(dot_C_sq2[0]), Create(dot_D_sq2[0]))
        self.play(Write(gr1))
        self.play(Write(gr1_2))

        DECAUA=Text(f"Giải thích vì sao các đường thẳng AA’, BB’, CC’, DD’ cùng đi qua một điểm O?",font_size=25)
        DECAUA.to_corner(DOWN)
        self.play(Write(DECAUA))
     #   self.play(Create(O),Write(Otext))
      #  self.play(Create(lineAtoO), Create(lineAprimetoO),Create(lineBtoO), Create(lineBprimetoO))
        small_factor=0.5
        self.play(
            square_1.animate.scale(small_factor),
            square_2.animate.scale(small_factor),
        )

        self.play(
            square_1.animate.to_edge(LEFT)
        )
        self.play(
            square_2.animate.next_to(square_1,RIGHT*3)
        )

        self.next_slide()
        cm1=Text(f"Gọi O là giao điểm của AA' và BB' ",font_size=24)
        cm1.to_edge(UR)
        cm1.shift(DOWN*2)
        intersection_point = self.calculateIntersection(dot_A_sq1[0].get_center(), dot_A_sq2[0].get_center(), dot_B_sq1[0].get_center(), dot_B_sq2[0].get_center())
        O=Dot(point=intersection_point)
        Otext=Tex("$O$")
        always_redraw(lambda:Otext.next_to(O,UP))
        self.play(Write(cm1))
        self.play(Create(O),Write(Otext))
        lineAtoO = Line(dot_A_sq1[0].get_center(), O.get_center(), color=WHITE)
        lineAprimetoO = Line(dot_A_sq2[0].get_center(), O.get_center(), color=WHITE)
        lineBtoO = Line(dot_B_sq1[0].get_center(), O.get_center(), color=WHITE)
        lineBprimetoO = Line(dot_B_sq2[0].get_center(), O.get_center(), color=WHITE)
        self.play(Create(lineAtoO), Create(lineAprimetoO),Create(lineBtoO), Create(lineBprimetoO))
        self.next_slide()
        cm2=Text(f"Xét tam giác OA'B' có AB // A'B', theo Thales, ta có:",font_size=24)
        cm2.next_to(cm1,DOWN,buff=0.25)
        cm2.shift(LEFT*1.5)
        self.play(Write(cm2))
        self.play(
               lineAtoO.animate.set_color(RED),
        lineAprimetoO.animate.set_color(RED),
          lineBtoO.animate.set_color(RED),
             lineBprimetoO.animate.set_color(RED),
        )
       # Plo=Polygon(dot_A_sq1[0].get_center(),dot_A_sq2[0].get_center(),dot_B_sq1[0].get_center(),dot_B_sq2[0].get_center(),O.get_center(),stroke_width=5,fill_color = ORANGE, fill_opacity=0.5)
      #  Plo1=Polygon(dot_A_sq1[0].get_center(),dot_B_sq1[0].get_center(),dot_A_sq2[0].get_center(),stroke_width=5,fill_color = ORANGE, fill_opacity=0.5)
      #  self.play(Create(Plo),Create(Plo1))

        self.next_slide()
        cm3 = Tex(r"$$\frac{OA}{OA'}=\frac{OB}{OB'}=\frac{1}{2}$$", font_size=24)
        cm3.next_to(cm2,DOWN,buff=0.25)
        self.play(Write(cm3))


        lineDprimetoD = Line(dot_D_sq2[0].get_center(), dot_D_sq1[0].get_center(), color=WHITE)

# Animate the line connecting D' to D
        self.play(Create(lineDprimetoD))

# Create the line connecting D to O
        lineDtoO = Line(dot_D_sq1[0].get_center(), O.get_center(), color=WHITE)

# Animate the line connecting D to O
        self.play(Create(lineDtoO))

        

    def createDot(self,index,dir,sq,text,colorA):
        dot=always_redraw(lambda:Dot(sq.get_vertices()[index-1],color=colorA))
        texttt=Tex(text)
        always_redraw(lambda:texttt.next_to(dot,dir))
        return [dot,texttt]
    def calculateIntersection(self, point1, point2, point3, point4):
        x1, y1 = point1[0], point1[1]
        x2, y2 = point2[0], point2[1]
        x3, y3 = point3[0], point3[1]
        x4, y4 = point4[0], point4[1]

        intersection_x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        intersection_y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))

        return np.array([intersection_x, intersection_y, 0])

