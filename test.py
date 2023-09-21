from manim import *

class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6, 0, 0])
        x_end = np.array([6, 0, 0])

        y_start = np.array([-4, -2, 0])
        y_end = np.array([-4, 2, 0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4, 0, 0])
        self.curve_start = np.array([-3, 0, 0])

    def add_x_labels(self):
        x_labels = [
            MathTex("\pi"), MathTex("2 \pi"),
            MathTex("3 \pi"), MathTex("4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2 * i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x, y, 0]), color=YELLOW_A, stroke_width=2)

        self.curve = VGroup()
        self.curve.add(Line(self.curve_start, self.curve_start))
        def get_curve():
            last_line = self.curve[-1]
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            new_line = Line(last_line.get_end(), np.array([x, y, 0]), color=YELLOW_D)
            self.curve.add(new_line)

            return self.curve

        dot.add_updater(go_around_circle)

        origin_to_circle_line = always_redraw(get_line_to_circle)
        dot_to_curve_line = always_redraw(get_line_to_curve)
        sine_curve_line = always_redraw(get_curve)

        self.add(dot)
        self.add(orbit, origin_to_circle_line, dot_to_curve_line, sine_curve_line)
        self.wait(8.5)

        dot.remove_updater(go_around_circle)

class TeamMemberIntroduction(Scene):
    def construct(self):
        # Create the team member introduction content
        team_members = [
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
            text = Text(member, font_size=24)
            tex_group.add(text)
        tex_group.arrange(DOWN, aligned_edge=LEFT)
        tex_group.to_edge(LEFT)

        # Add the team member introduction to the scene
        self.play(Write(tex_group))

    def construct(self):
        self.show_sine_curve()

    def show_sine_curve(self):
        # Create the sine curve scene
        sine_curve_scene = SineCurveUnitCircle()
        self.add(sine_curve_scene)

        # Adjust the position of the sine curve scene
        sine_curve_scene.scale(0.5)  # Scale it down if needed
        sine_curve_scene.to_corner(UL)  # Position it in the top left corner

        # Play the animation
        self.play(sine_curve_scene.animate.run_time(8.5))

if __name__ == "__main__":
    module_name = file_writer_config.get_module_name(__file__)
    scene = TeamMemberIntroduction()
    scene.render()
