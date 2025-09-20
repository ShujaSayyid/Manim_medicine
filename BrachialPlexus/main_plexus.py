from manim import *
import numpy as np

class BrachialPlexusScene(Scene):
    def construct(self):
        # Distinct, colorblind-friendly mapping for roots C5–T1
        COLORS = {
            "C5": RED,        # or hex: #D55E00
            "C6": YELLOW,     # #E69F00
            "C7": GREEN,      # #009E73
            "C8": BLUE,       # #0072B2
            "T1": PURPLE      # #CC79A7
        }

        # ---------- Layout coordinates ----------
        # Roots (left)
        P_ROOT = {
            "C5": np.array([-6.0,  2.0, 0]),
            "C6": np.array([-6.0,  1.0, 0]),
            "C7": np.array([-6.0,  0.0, 0]),
            "C8": np.array([-6.0, -1.0, 0]),
            "T1": np.array([-6.0, -2.0, 0]),
        }

        # Trunks
        P_TRUNK = {
            "UP": np.array([-4.8,  1.5, 0]),   # Superior (C5–C6)
            "MID": np.array([-4.8,  0.0, 0]),  # Middle (C7)
            "LOW": np.array([-4.8, -1.5, 0]),  # Inferior (C8–T1)
        }

        # Divisions (each trunk splits into anterior/posterior)
        P_DIV = {
            "UP_ANT":  np.array([-3.6,  1.2, 0]),
            "UP_POST": np.array([-3.6,  1.8, 0]),
            "MID_ANT": np.array([-3.6,  0.0, 0]),
            "MID_POST":np.array([-3.6,  0.6, 0]),
            "LOW_ANT": np.array([-3.6, -1.2, 0]),
            "LOW_POST":np.array([-3.6, -1.8, 0]),
        }

        # Cords around the axillary artery
        P_CORD = {
            "LAT": np.array([-2.2,  0.8, 0]),
            "POST":np.array([-2.2,  0.0, 0]),
            "MED": np.array([-2.2, -1.2, 0]),
        }

        # Terminal nerve endpoints (right)
        P_NERVE_END = {
            "MCN":   np.array([2.2,  1.1, 0]),  # Musculocutaneous
            "AX":    np.array([2.2,  0.5, 0]),  # Axillary
            "MEDIAN":np.array([2.2, -0.3, 0]),  # Median
            "RAD":   np.array([2.2, -0.9, 0]),  # Radial
            "ULN":   np.array([2.2, -1.5, 0]),  # Ulnar
        }

        # ---------- Legend for colors ----------
        legend_items = VGroup()
        for i, root in enumerate(["C5", "C6", "C7", "C8", "T1"]):
            box = Square(side_length=0.25).set_fill(COLORS[root], opacity=1).set_stroke(width=0)
            label = Text(root, font_size=28, color=WHITE).next_to(box, RIGHT, buff=0.15)
            row = VGroup(box, label).arrange(RIGHT, buff=0.15)
            row.move_to(np.array([-6.4, 2.5 - 0.5*i, 0]))
            legend_items.add(row)

        title = Text("Brachial Plexus (C5–T1)", font_size=36, color=WHITE).to_edge(UP)

        # ---------- Build segments as Lines ----------
        # Roots -> Trunks
        line_C5 = Line(P_ROOT["C5"], P_TRUNK["UP"], color=COLORS["C5"])
        line_C6 = Line(P_ROOT["C6"], P_TRUNK["UP"], color=COLORS["C6"])
        line_C7 = Line(P_ROOT["C7"], P_TRUNK["MID"], color=COLORS["C7"])
        line_C8 = Line(P_ROOT["C8"], P_TRUNK["LOW"], color=COLORS["C8"])
        line_T1 = Line(P_ROOT["T1"], P_TRUNK["LOW"], color=COLORS["T1"])

        # Trunks -> Divisions (split)
        up_to_ant   = Line(P_TRUNK["UP"],  P_DIV["UP_ANT"]).set_color_by_gradient(COLORS["C5"], COLORS["C6"])
        up_to_post  = Line(P_TRUNK["UP"],  P_DIV["UP_POST"]).set_color_by_gradient(COLORS["C5"], COLORS["C6"])
        mid_to_ant  = Line(P_TRUNK["MID"], P_DIV["MID_ANT"]).set_color(COLORS["C7"])
        mid_to_post = Line(P_TRUNK["MID"], P_DIV["MID_POST"]).set_color(COLORS["C7"])
        low_to_ant  = Line(P_TRUNK["LOW"], P_DIV["LOW_ANT"]).set_color_by_gradient(COLORS["C8"], COLORS["T1"])
        low_to_post = Line(P_TRUNK["LOW"], P_DIV["LOW_POST"]).set_color_by_gradient(COLORS["C8"], COLORS["T1"])

        # Divisions -> Cords (regroup)
        # Anterior divisions -> Lateral & Medial cords
        ant_to_lat_1 = Line(P_DIV["UP_ANT"],  P_CORD["LAT"]).set_color_by_gradient(COLORS["C5"], COLORS["C6"])
        ant_to_lat_2 = Line(P_DIV["MID_ANT"], P_CORD["LAT"]).set_color(COLORS["C7"])
        ant_to_med   = Line(P_DIV["LOW_ANT"], P_CORD["MED"]).set_color_by_gradient(COLORS["C8"], COLORS["T1"])
        # Posterior divisions -> Posterior cord (all 3)
        post_to_post_1 = Line(P_DIV["UP_POST"],  P_CORD["POST"]).set_color_by_gradient(COLORS["C5"], COLORS["C6"])
        post_to_post_2 = Line(P_DIV["MID_POST"], P_CORD["POST"]).set_color(COLORS["C7"])
        post_to_post_3 = Line(P_DIV["LOW_POST"], P_CORD["POST"]).set_color_by_gradient(COLORS["C8"], COLORS["T1"])

        # Cords -> Terminal branches
        lat_to_mcn   = Line(P_CORD["LAT"],  P_NERVE_END["MCN"]).set_color_by_gradient(COLORS["C5"], COLORS["C6"], COLORS["C7"])
        lat_to_median= Line(P_CORD["LAT"],  P_NERVE_END["MEDIAN"]).set_color_by_gradient(COLORS["C6"], COLORS["C7"])  # lateral root of median
        med_to_uln   = Line(P_CORD["MED"],  P_NERVE_END["ULN"]).set_color_by_gradient(COLORS["C8"], COLORS["T1"])
        med_to_median= Line(P_CORD["MED"],  P_NERVE_END["MEDIAN"]).set_color_by_gradient(COLORS["C8"], COLORS["T1"])  # medial root of median
        post_to_ax   = Line(P_CORD["POST"], P_NERVE_END["AX"]).set_color_by_gradient(COLORS["C5"], COLORS["C6"])
        post_to_rad  = Line(P_CORD["POST"], P_NERVE_END["RAD"]).set_color_by_gradient(COLORS["C5"], COLORS["C6"], COLORS["C7"], COLORS["C8"], COLORS["T1"])

        # ---------- Labels ----------
        lab_roots = VGroup(*[
            Text(k, font_size=26, color=COLORS[k]).next_to(P_ROOT[k], LEFT, buff=0.2)
            for k in ["C5", "C6", "C7", "C8", "T1"]
        ])

        lab_trunks = VGroup(
            Text("Superior trunk", font_size=24).next_to(P_TRUNK["UP"], UP, buff=0.15),
            Text("Middle trunk",   font_size=24).next_to(P_TRUNK["MID"], DOWN, buff=0.15),
            Text("Inferior trunk", font_size=24).next_to(P_TRUNK["LOW"], DOWN, buff=0.15),
        )

        lab_cords = VGroup(
            Text("Lateral cord",   font_size=22).next_to(P_CORD["LAT"], UP, buff=0.1),
            Text("Posterior cord", font_size=22).next_to(P_CORD["POST"], UP, buff=0.1),
            Text("Medial cord",    font_size=22).next_to(P_CORD["MED"], DOWN, buff=0.1),
        )

        lab_nerves = VGroup(
            Text("Musculocutaneous", font_size=22).next_to(P_NERVE_END["MCN"], RIGHT, buff=0.15),
            Text("Axillary",         font_size=22).next_to(P_NERVE_END["AX"], RIGHT, buff=0.15),
            Text("Median",           font_size=22).next_to(P_NERVE_END["MEDIAN"], RIGHT, buff=0.15),
            Text("Radial",           font_size=22).next_to(P_NERVE_END["RAD"], RIGHT, buff=0.15),
            Text("Ulnar",            font_size=22).next_to(P_NERVE_END["ULN"], RIGHT, buff=0.15),
        )

        # Section headers (optional visual anchors)
        hdr_roots     = Text("Roots",     font_size=28).move_to(np.array([-6.0, 3.0, 0]))
        hdr_trunks    = Text("Trunks",    font_size=28).move_to(np.array([-4.8, 3.0, 0]))
        hdr_divisions = Text("Divisions", font_size=28).move_to(np.array([-3.6, 3.0, 0]))
        hdr_cords     = Text("Cords",     font_size=28).move_to(np.array([-2.2, 3.0, 0]))
        hdr_branches  = Text("Branches",  font_size=28).move_to(np.array([ 2.2, 3.0, 0]))

        # ---------- Animation ----------
        self.play(FadeIn(title), FadeIn(legend_items))
        self.play(FadeIn(hdr_roots))
        # Roots
        self.play(*[Create(m) for m in [line_C5, line_C6, line_C7, line_C8, line_T1]], run_time=1.6)
        self.play(FadeIn(lab_roots, shift=RIGHT), run_time=0.8)

        # Trunks
        self.play(FadeIn(hdr_trunks))
        self.play(FadeIn(lab_trunks), run_time=0.6)

        # Divisions
        self.play(FadeIn(hdr_divisions))
        self.play(
            Create(up_to_ant), Create(up_to_post),
            Create(mid_to_ant), Create(mid_to_post),
            Create(low_to_ant), Create(low_to_post),
            run_time=1.4
        )

        # Cords
        self.play(FadeIn(hdr_cords))
        self.play(
            Create(ant_to_lat_1), Create(ant_to_lat_2), Create(ant_to_med),
            Create(post_to_post_1), Create(post_to_post_2), Create(post_to_post_3),
            run_time=1.6
        )
        self.play(FadeIn(lab_cords), run_time=0.7)

        # Branches
        self.play(FadeIn(hdr_branches))
        self.play(Create(lat_to_mcn), Create(post_to_ax), run_time=0.8)
        self.play(Create(post_to_rad), Create(med_to_uln), run_time=1.0)
        self.play(Create(lat_to_median), Create(med_to_median), run_time=0.8)
        self.play(FadeIn(lab_nerves), run_time=0.8)

        self.wait(2)